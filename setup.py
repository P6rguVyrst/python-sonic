#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open


# Get the long description from the README file
with open('README.rst'), encoding='utf-8') as f:
    long_description = f.read()

requirements = [
    'python-osc',
]

setup_requirements = [
    'pytest-runner',
    # TODO(P6rguVyrst): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]


setup(
    name='python-sonic',
    version='0.3.1',
    description='Programming Music with Sonic Pi or Supercollider',
    long_description=long_description,
    url='https://github.com/gkvoelkl/python-sonic',
    author='gkvoelkl',
    author_email='gkvoelkl@nelson-games.de',
    packages=find_packages(include=['psonic']),
    include_package_data=True,
    install_requires=requirements,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Sound/Audio',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords= [
       'music',
       'sonic pi',
       'raspberry pi',
       'audio',
       'music composition',
       'scsynth',
       'supercollider',
       'synthesis'
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
