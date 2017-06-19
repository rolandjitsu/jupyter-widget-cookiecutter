"""
Example widget.

See widget docs at: http://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Custom.html.
"""

from ipywidgets import DOMWidget, register
from traitlets import Unicode

from .package import npm_pkg_name
from .version import npm_package_version


@register('{0}.Hello'.format(npm_pkg_name))
class HelloWorld(DOMWidget):
    """Hello widget model."""

    _view_module = Unicode(npm_pkg_name).tag(sync=True)
    _model_module = Unicode(npm_pkg_name).tag(sync=True)
    _view_module_version = Unicode(npm_package_version).tag(sync=True)
    _model_module_version = Unicode(npm_package_version).tag(sync=True)
    _model_name = Unicode('HelloModel').tag(sync=True)
    _view_name = Unicode('HelloView').tag(sync=True)

    value = Unicode('Hello World :)').tag(sync=True)
