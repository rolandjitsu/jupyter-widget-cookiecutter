"""{{ cookiecutter.project_short_description }}"""

from .version import npm_package_version, version, version_info, __version__
from .package import npm_pkg_name, py_pkg_name

from .example import HelloWorld


# Don't include install_nbextension when we import *
__all__ = ['HelloWorld']


def _jupyter_nbextension_paths():
    return [{
        'dest': npm_pkg_name,
        'require': '{0}/extension'.format(npm_pkg_name),
        'section': 'notebook',
        'src': 'static'
    }]
