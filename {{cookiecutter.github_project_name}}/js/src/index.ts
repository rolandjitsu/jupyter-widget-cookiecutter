// tslint:disable: no-var-requires
/**
 * Entry point for the notebook bundle containing custom model definitions.
 * Setup notebook base URL.
 * NOTE: The base url for the notebook is not known at build time and is therefore computed dynamically.
 * Some static assets may be required by the custom widget javascript.
 */
const body: HTMLBodyElement = document.querySelector('body') as HTMLBodyElement;

// NOTE: Declare the Webpack private global var,
// otherwise TS will complain about it.
declare let __webpack_public_path__: string;
__webpack_public_path__ = `${body.getAttribute('data-base-url')}nbextensions/{{ cookiecutter.npm_package_name }}/`;


// Export widget models and views,
// and the npm package version number.
module.exports = require('./example');
module.exports.version = require('../package.json')
	.version;
