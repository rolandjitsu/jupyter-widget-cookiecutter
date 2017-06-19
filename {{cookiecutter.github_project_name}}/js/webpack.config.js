const path = require('path');
const webpack = require('webpack');
const version = require('./package.json')
    .version;

const pckgPath = path.resolve(__dirname, '../{{ cookiecutter.python_package_name }}/static');
const distPath = path.resolve(__dirname, './dist/');

const loaders = [
    {
        test: /\.json$/,
        loader: 'json-loader'
    },
    // Transpile TS to AMD using ts-loader (https://github.com/TypeStrong/ts-loader).
    {
        test: /\.ts$/,
        exclude: /node_modules/,
        use: [
            {
                loader: 'ts-loader'
            }
        ]
    }
];
const devtool = 'source-map';

// Optimize dist package
// https://webpack.js.org/guides/production-build
const plugins = [
    new webpack.optimize.UglifyJsPlugin({
        sourceMap: devtool.indexOf('sourcemap') >= 0 || devtool.indexOf('source-map') >= 0,
        compress: {screw_ie8: true},
        comments: false
    })
];

const externals = ['jupyter-js-widgets'];
const resolve = {
    extensions: ['.ts', '.js']
};


module.exports = [
    {
        /**
         * Notebook extension
         *
         * This bundle only contains the part of the JavaScript that is run on load of the notebook.
         * This section generally only performs some configuration for requirejs,
         * and provides the legacy "load_ipython_extension" function which is required for any notebook extension.
         */
        resolve,
        plugins,
        entry: './src/extension.ts',
        output: {
            filename: 'extension.js',
            libraryTarget: 'amd',
            path: pckgPath
        },
        module: {loaders}
    },
    {
        /**
         * Bundle for the notebook containing the custom widget views and models.
         * This bundle contains the implementation for the custom widget views and custom widget.
         * NOTE: It must be an amd module.
         */
        devtool,
        externals,
        resolve,
        plugins,
        entry: './src/index.ts',
        output: {
            filename: 'index.js',
            libraryTarget: 'amd',
            path: pckgPath
        },
        module: {loaders}
    },
    {
        /**
         * Embeddable bundle
         *
         * This bundle is generally almost identical to the notebook bundle containing the custom widget views and models.
         * The only difference is in the configuration of the webpack public path for the static assets.
         *
         * It will be automatically distributed by unpkg to work with the static widget embedder.
         *
         * The target bundle is always `dist/index.js`,
         * which is the path required by the custom widget embedder.
         */
        devtool,
        externals,
        resolve,
        plugins,
        entry: './src/embed.ts',
        output: {
            filename: 'index.js',
            libraryTarget: 'amd',
            path: distPath,
            publicPath: `https://unpkg.com/{{ cookiecutter.npm_package_name }}@${version}/dist/`
        },
        module: {loaders}
    }
];
