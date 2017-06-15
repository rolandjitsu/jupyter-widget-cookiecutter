# {{ cookiecutter.github_project_name }}

> {{ cookiecutter.project_short_description }}


### Install
-----------
If you wish to install, use pip:
```bash
pip install {{ cookiecutter.python_package_name }}
jupyter nbextension enable --py --sys-prefix {{ cookiecutter.python_package_name }}
```

For a development installation (requires [NPM](https://www.npmjs.com)), use the following:
```bash
git clone https://github.com/{{ cookiecutter.github_organization_name }}/{{ cookiecutter.github_project_name }}.git
cd {{ cookiecutter.github_project_name }}
pip install -e .
jupyter nbextension install --py --symlink --sys-prefix {{ cookiecutter.python_package_name }}
jupyter nbextension enable --py --sys-prefix {{ cookiecutter.python_package_name }}
```
