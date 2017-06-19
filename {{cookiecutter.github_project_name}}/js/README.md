# {{ cookiecutter.github_project_name }}

> {{ cookiecutter.project_short_description }}


### Contribute
--------------
Prerequisites:
- [node.js](http://nodejs.org/)
- [NPM](https://www.npmjs.com) (you get it with the node install)

To install deps run:
```bash
npm install
```

Now start hacking.


### Test
--------
During development, use the following commands to ensure everything is still working and is in line with the coding guidelines:
- `npm test` - Runs unit tests in Chrome;
- `npm run test:continuous` - Continuously runs unit tests in Chrome; reruns on file change;
- `npm run lint` - Lints all `.ts` files;
- `npm run lint:fix` - Lints and fixes errors (only works for some rules).

**NOTE**: [core-js](https://github.com/zloirock/core-js) is loaded during unit tests in order to provide polyfills for ES6 features that may not be available in the browser.

Testing tools:
- [Karma](https://github.com/karma-runner/karma)
- [Jasmine](https://jasmine.github.io/2.0/introduction.html)
- [TSLint](https://github.com/palantir/tslint)
