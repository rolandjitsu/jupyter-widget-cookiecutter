from ipywidgets import Color, DOMWidget, register
from traitlets import Unicode, CFloat

from ._package import npm_pkg_name


NPM_PACKAGE_VERSION = '{{ cookiecutter.npm_package_version }}'


# See widget docs at: http://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Custom.html.
# Cookiecutter source: https://github.com/jupyter-widgets/widget-cookiecutter.
@register('{0}.Hello'.format(npm_pkg_name))
class HelloWorld(DOMWidget):
    """Hello widget model."""
    _view_module = Unicode(npm_pkg_name).tag(sync=True)
    _model_module = Unicode(npm_pkg_name).tag(sync=True)
    _view_module_version = Unicode(NPM_PACKAGE_VERSION).tag(sync=True)
    _model_module_version = Unicode(NPM_PACKAGE_VERSION).tag(sync=True)
    _model_name = Unicode('HelloModel').tag(sync=True)
    _view_name = Unicode('HelloView').tag(sync=True)

    value = Unicode('Hello World :)').tag(sync=True)
