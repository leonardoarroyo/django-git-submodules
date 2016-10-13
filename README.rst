=====
Django Git Submodules
=====

Django Submodules is a simple Django app that allows you
to manage apps as git submodules instead of pip.
This allows you to have a local development version of
third-party packages and merge changes from upstream.

Ideally should only be used in development.
These changes should be pushed back to the package repository
and installed with pip on production.

Quick start
-----------
1. Install django-git-submodules::

    pip install django-git-submodules

2. Clone the the package you want on your project root::

    git clone https://github.com/tomchristie/django-rest-framework.git

3. Import the app in your `settings.py`::

    from dj_git_submodule import submodule
    submodule.add('django-rest-framework')

4. Now you should be able to add the app to `INSTALLED_APPS` and have django find it successfully.

5. If you need to import multiple apps, you can use wildcards(through glob)::

    from dj_git_submodule import submodule
    submodule.add(submodule.register('custom-apps-*'))
