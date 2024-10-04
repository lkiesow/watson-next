#!/usr/bin/env python
"""Setup file for the Watson distribution."""

import os.path
from os.path import join

from setuptools import setup

# read package meta-data from version.py
pkg = {}
mod = join('watson', 'version.py')
exec(compile(open(mod).read(), mod, 'exec'), {}, pkg)


def read(filename):
    path = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(path, filename), encoding='utf-8') as f:
        return f.read()


def parse_requirements(requirements, ignore=('setuptools',)):
    """Read dependencies from requirements file (with version numbers if any)

    Note: this implementation does not support requirements files with extra
    requirements
    """
    with open(requirements) as f:
        packages = set()
        for line in f:
            line = line.strip()
            if line.startswith(('#', '-r', '--')):
                continue
            if '#egg=' in line:
                line = line.split('#egg=')[1]
            pkg = line.strip()
            if pkg not in ignore:
                packages.add(pkg)
        return tuple(packages)


setup(
    name='watson-next',
    version=pkg['version'],
    description='A wonderful CLI to track your time!',
    url='https://github.com/lkiesow/watson-next',
    packages=['watson'],
    author='Lars Kiesow',
    author_email='lkiesow@uos.de',
    license='MIT',
    license_files=('LICENSE'),
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    install_requires=parse_requirements('requirements.txt'),
    python_requires='>=3.6',
    tests_require=parse_requirements('requirements-dev.txt'),
    entry_points={
        'console_scripts': [
            'watson = watson.__main__:cli',
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Customer Service",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Office/Business",
        "Topic :: Utilities",
    ],
    keywords='watson time-tracking time tracking monitoring report',
)
