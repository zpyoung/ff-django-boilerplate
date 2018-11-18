# Thorgate's Django template (SPA variant)

[![Build status](https://gitlab.com/thorgate-public/django-project-template/badges/spa/pipeline.svg)](https://gitlab.com/thorgate-public/django-project-template/commits/spa)

[Django](https://www.djangoproject.com/) project template that we use at [Thorgate](https://thorgate.eu).

Best suited for single page web applications.

See also the [default](https://gitlab.com/thorgate-public/django-project-template/tree/master)
and [Bootstrap 4](https://gitlab.com/thorgate-public/django-project-template/tree/bootstrap4) variants.

_(note that the primary repo is in [Gitlab](https://gitlab.com/thorgate-public/django-project-template), with mirror in [Github](https://github.com/thorgate/django-project-template))_


## Migrating to SPA version 3.0

3.0 brings support for env based settings.

- Upgrade template
- Move all required bits to new `app` directory
- Test that everything is still working
- Commit changes
- Servers
    - Update Django to new settings
        - Convert `<root>/<project>/settings/local.py` to `<root>/<project>/django.env`
        - Or remove `DJANGO_PRODUCTION_MODE` and `DJANGO_SETTINGS_MODULE` env reference from `Dockerfile-django.production`
    - Copy `<root>/app/env/node.env.example` to `<root>/app/env/node.env`
        - Update Node settings in `<root>/app/env/node.env`
            - `SITE_URL`
            - `DJANGO_SITE_URL`
            - `ALLOWED_HOSTS`
            - `RAVEN_PUBLIC_DSN`
            - `RAVEN_BACKEND_DSN`

## Features

- Django-based storage API backend (accessible from port `3000` for local development)

    - [Django](https://www.djangoproject.com/) 1.11 (because it's LTS)
    - Separate settings for different environments (local/staging/production)
    - Python 3.6+

- Frontend app with JavaScript (ES2015), React, Koa, and Sass (accessible from port `8000` for local development)

    - Latest JavaScript features from [ES2015](https://babeljs.io/docs/learn-es2015/) and beyond, transpiled with
      [Babel](https://babeljs.io/)
    - [React](https://facebook.github.io/react/) 16.2 for fast modular user interfaces
    - [Sass](http://sass-lang.com/), [PostCSS](http://postcss.org/) and
      [Autoprefixer](https://github.com/postcss/autoprefixer) for more convenient styling
    - [Webpack](https://webpack.github.io/) 2.3 is used to bundle and minify JavaScript and styles

- Batteries

    - Docker / Docker Compose integration
    - Linting of Python, JavaScript and Sass code with [Prospector](http://prospector.landscape.io/),
      [ESLint](http://eslint.org/) and [stylelint](https://stylelint.io/)
    - [py.test](http://pytest.org/) and [coverage](https://coverage.readthedocs.io/) integration
    - Deploy helpers, using [Fabric](http://www.fabfile.org/)
    - Out-of-the-box configuration for nginx, gunicorn, and logrotate
    - Includes [PyCharm](https://www.jetbrains.com/pycharm/) project config


## Usage

To use this template, first ensure that you have
[Cookiecutter](http://cookiecutter.readthedocs.org/en/latest/readme.html) available.
You should probably create additional python3 virtual environment for cookiecutter, activate it
and then install following packages by running following command:
`pip install cookiecutter cookiecutter_repo_extensions fqdn`


Then just execute:

    cookiecutter dir/to/django-project-template/

It will ask you a few questions, e.g. project's name.

After generation completes, search for any TODOs in the code and make appropriate changes where needed.

See README.md in the generated project for instructions on how to set up your development environment.


## Upgrading project template

First ensure you have a python3 interpreter with `cookiecutter` installed.

To upgrade an existing project, change the current working directory to the root of the project you want to upgrade. i.e. `cd project-to-upgrade`. Ensure your are not in the `template` branch.

Then run `python ~/path/to/django-project-template/upgrade-template.py`

This will make a commit to the branch `template` in your project with the updates to the project template. Then merge the `template` branch.
