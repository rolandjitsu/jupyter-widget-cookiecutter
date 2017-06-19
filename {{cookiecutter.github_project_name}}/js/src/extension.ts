/**
 * This file contains the javascript that is run when the notebook is loaded.
 * It contains some requirejs configuration and the `load_ipython_extension` which is required for any notebook extension.
 */

// NOTE: Without declaring the requirejs `require`,
// TS will complain.
declare interface Window {
    require: {
        config(...args: any[]): any
    };
}

// Configure requirejs
if (window.require) {
    window.require.config({
        map: {
            '*': {
                '{{ cookiecutter.npm_package_name }}': 'nbextensions/{{ cookiecutter.npm_package_name }}/index',
                'jupyter-js-widgets': 'nbextensions/jupyter-js-widgets/extension'
            }
        }
    });
}


// Export the required load_ipython_extension
module.exports = {
    // tslint:disable-next-line: no-empty
    load_ipython_extension() {}
};
