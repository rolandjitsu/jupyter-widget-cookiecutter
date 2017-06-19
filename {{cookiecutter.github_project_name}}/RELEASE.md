# Release steps

To release a new version of **{{ cookiecutter.python_package_name }}** on PyPI:

1. Update `version.py` (set release version, remove 'dev');
2. `git add` and `git commit` the changes;
3. `python setup.py sdist upload`;
4. `python setup.py bdist_wheel upload`;
5. `git tag -a X.X.X -m 'some comments about the release'`;
6. Update `version.py` (add 'dev' and increment minor);
7. `git add` and `git commit` the changes;
8. `git push`:
9. `git push --tags`.

To release a new version of **{{ cookiecutter.npm_package_name }}** on [NPM](https://www.npmjs.com):

1. Remove `dist` and `node_modules`;
2. `git clean -fdx`;
3. `npm install`;
4. `npm publish`.
