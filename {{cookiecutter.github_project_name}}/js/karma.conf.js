module.exports = function (config) {
    config.set({
        frameworks: [
            'jasmine',
            'karma-typescript'
        ],
        reporters: ['spec'],
        preprocessors: {
            '**/*.ts': ['karma-typescript']
        },
        files: [
            // Shims
			{pattern: 'node_modules/core-js/client/shim.min.js.map', included: false, served: true},
			'node_modules/core-js/client/shim.min.js',
            // Specs
            {pattern: 'src/**/*.ts'}
        ],
        karmaTypescriptConfig: {
            tsconfig: './tsconfig.spec.json',
            bundlerOptions: {
                entrypoints: /\.spec\.ts$/,
                transforms: []
            }
        },
        logLevel: config.LOG_INFO,
        browsers: [
            'Chrome'
        ]
    });
};
