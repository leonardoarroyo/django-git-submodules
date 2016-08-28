# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-submodule',
    version='0.1.0',
    author=u'Leonardo Arroyo',
    author_email='contato@leonardoarroyo.com',
    packages=['dj_git_submodule'],
    url='',
    license='MIT license, see LICENSE.',
    description='Adds packages to syspath so they can be' + \
                ' used as git submodules instead of pip' + \
                ' packages. Should be only used in development.',
    long_description=open('README.rst', encoding='utf-8').read(),
    zip_safe=False,
)