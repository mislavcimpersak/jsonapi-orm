#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'munch',
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Mislav Cimperšak",
    author_email='mislav.cimpersak@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Quick and dirty ORM that maps JSON:API responses to object attributes.",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='jsonapi-orm',
    name='jsonapi-orm',
    packages=find_packages(include=['jsonapi-orm']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mislavcimpersak/jsonapi-orm',
    version='0.1.5',
    zip_safe=False,
)
