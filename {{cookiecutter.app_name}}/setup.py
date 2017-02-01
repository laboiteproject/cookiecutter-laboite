# coding: utf-8
from __future__ import unicode_literals

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='laboite.apps.{{cookiecutter.app_name}}',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    license='AGPL v3',
    description='{{cookiecutter.app_description}}',
    long_description=README,
    url='{{cookiecutter.url}}',
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    namespace_packages=('laboite', 'laboite.apps',),
    classifiers=(
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ),
)
