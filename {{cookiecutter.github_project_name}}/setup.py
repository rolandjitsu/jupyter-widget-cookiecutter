from __future__ import print_function
from setuptools import setup, find_packages, Command
from setuptools.command.sdist import sdist
from setuptools.command.build_py import build_py
from setuptools.command.egg_info import egg_info
from subprocess import check_call
from distutils import log

from pip.req import parse_requirements
from pip.download import PipSession
from optparse import Option

import os
import sys


here = os.path.dirname(os.path.abspath(__file__))
node_root = os.path.join(here, 'js')
is_repo = os.path.exists(os.path.join(here, '.git'))

npm_path = os.pathsep.join([
    os.path.join(node_root, 'node_modules', '.bin'),
    os.environ.get('PATH', os.defpath),
])


log.set_verbosity(log.DEBUG)
log.info('Run setup.py')
log.info('$PATH=%s' % os.environ['PATH'])

LONG_DESCRIPTION = '{{ cookiecutter.project_short_description }}'


def js_prerelease(command, strict=False):
    """Decorator for building minified js/css prior to another command."""
    class DecoratedCommand(command):
        def run(self):
            jsdeps = self.distribution.get_command_obj('jsdeps')
            if not is_repo and all(os.path.exists(t) for t in jsdeps.targets):
                # sdist, nothing to do
                command.run(self)
                return

            try:
                self.distribution.run_command('jsdeps')
            except Exception as e:
                missing = [t for t in jsdeps.targets if not os.path.exists(t)]
                if strict or missing:
                    log.warn('Rebuilding js and css failed')
                    if missing:
                        log.error('Missing files: %s' % missing)
                    raise e
                else:
                    log.warn('Rebuilding js and css failed (not a problem)')
                    log.warn(str(e))
            command.run(self)
            update_package_data(self.distribution)
    return DecoratedCommand


def update_package_data(distribution):
    """Update package_data to catch changes during setup."""
    build_py = distribution.get_command_obj('build_py')
    # distribution.package_data = find_package_data()
    # re-init build_py options which load package_data
    build_py.finalize_options()


class NPM(Command):
    description = 'Install package.json dependencies using npm'
    user_options = []
    node_modules = os.path.join(node_root, 'node_modules')

    targets = [
        os.path.join(here, '{{ cookiecutter.python_package_name }}', 'static', 'extension.js'),
        os.path.join(here, '{{ cookiecutter.python_package_name }}', 'static', 'index.js')
    ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def has_npm(self):
        try:
            check_call(['npm', '--version'])
            return True
        except:
            return False

    def should_run_npm_install(self):
        package_json = os.path.join(node_root, 'package.json')
        node_modules_exists = os.path.exists(self.node_modules)
        return self.has_npm()

    def run(self):
        has_npm = self.has_npm()
        if not has_npm:
            log.error('`npm` command in unavailable. Make sure NPM is installed.')

        env = os.environ.copy()
        env['PATH'] = npm_path

        if self.should_run_npm_install():
            log.info('Installing build dependencies with npm. This may take a while ...')
            check_call(['npm', 'install'], cwd=node_root, stdout=sys.stdout, stderr=sys.stderr)
            os.utime(self.node_modules, None)

        for t in self.targets:
            if not os.path.exists(t):
                msg = 'Missing file: %s' % t
                if not has_npm:
                    msg += '\nnpm is required to build a development version of widgetsnbextension'
                raise ValueError(msg)

        # update package data in case this created new files
        update_package_data(self.distribution)


def parse_reqs(reqs_file):
    """Parse the project requirements."""
    options = Option('--workaround')
    options.skip_requirements_regex = None
    options.isolated_mode = True
    install_reqs = parse_requirements(reqs_file, options=options, session=PipSession())
    return [str(ir.req) for ir in install_reqs]


version_ns = {}
with open(os.path.join(here, '{{ cookiecutter.python_package_name }}', 'version.py')) as f:
    exec(f.read(), {}, version_ns)

# Parse install and extra requirements from file(s)
install_requirements = parse_reqs(os.path.join(here, 'requirements.txt'))

EXTRA_REQUIREMENTS_PREFIX = 'requirements_'
extra_requirements = {}
for file_name in os.listdir(here):
    if not file_name.startswith(EXTRA_REQUIREMENTS_PREFIX):
        continue
    base_name = os.path.basename(file_name)
    (extra, _) = os.path.splitext(base_name)
    extra = extra[len(EXTRA_REQUIREMENTS_PREFIX):]
    extra_requirements[extra] = parse_reqs(file_name)

setup_args = {
    'name': '{{ cookiecutter.python_package_name }}',
    'version': version_ns['__version__'],
    'description': '{{ cookiecutter.project_short_description }}',
    'long_description': LONG_DESCRIPTION,
    'include_package_data': True,
    'data_files': [
        ('share/jupyter/nbextensions/{{ cookiecutter.npm_package_name }}', [
            '{{ cookiecutter.python_package_name }}/static/extension.js',
            '{{ cookiecutter.python_package_name }}/static/index.js',
            '{{ cookiecutter.python_package_name }}/static/index.js.map'
        ])
    ],
    'install_requires': install_requirements,
    'extras_require': extra_requirements,
    'packages': find_packages(),
    'zip_safe': False,
    'cmdclass': {
        'build_py': js_prerelease(build_py),
        'egg_info': js_prerelease(egg_info),
        'sdist': js_prerelease(sdist, strict=True),
        'jsdeps': NPM
    },

    'author': '{{ cookiecutter.author_name }}',
    'author_email': '{{ cookiecutter.author_email }}',
    'url': 'http://jupyter.org',
    'keywords': [
        'ipython',
        'jupyter',
        'widgets'
    ],
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Multimedia :: Graphics',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
}

setup(**setup_args)
