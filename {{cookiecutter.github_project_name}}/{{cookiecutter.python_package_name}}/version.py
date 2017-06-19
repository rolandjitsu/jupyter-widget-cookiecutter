"""The version of the {{ cookiecutter.python_package_name }} package."""

# NOTE: This version should be updated whenever the package.json version gets updated.
npm_package_version = '{{ cookiecutter.npm_package_version }}'

version_info = (0, 1, 0, 'dev')
__version__ = '.'.join(map(str, version_info))
version = __version__
