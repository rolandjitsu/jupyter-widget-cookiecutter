# {{ cookiecutter.github_project_name }}

> {{ cookiecutter.project_short_description }}


### Install
-----------
Prerequisites:
- [node.js](http://nodejs.org/)

To install run:
```bash
npm install --save {{ cookiecutter.npm_package_name }}
```


### Test
--------
For testing, the following tools are provided:
- [Karma](https://github.com/karma-runner/karma)
- [Jasmine](https://jasmine.github.io/2.0/introduction.html)
- [TSLint](https://github.com/palantir/tslint)

**NOTE**: [core-js](https://github.com/zloirock/core-js) is loaded during unit tests in order to provide polyfills for ES6 features that may not be available in the browser.

And the following commands are available:
- `npm test` - Runs unit tests on PhantomJS;
- `npm run test:continuous` - Continuously runs unit tests on PhantomJS and Chrome; reruns on file change;
- `npm run lint` - Lints all `.ts` files;
- `npm run lint:fix` - Lints and fixes errors (only works for some rules).
