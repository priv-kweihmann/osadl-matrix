# SPDX-FileCopyrightText: 2021 Konrad Weihmann
# SPDX-License-Identifier: Unlicensed

import setuptools

with open('README.md') as i:
    _long_description = i.read()

with open('VERSION') as i:
    _version = i.read().strip()

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

requirements_dev = []
with open('requirements-dev.txt') as f:
    requirements_dev = f.read().splitlines()

setuptools.setup(
    name='osadl-matrix',
    version=_version,
    author='Konrad Weihmann',
    author_email='kweihmann@outlook.com',
    description='OSADL license compatibility matrix',
    long_description=_long_description,
    long_description_content_type='text/markdown',
    license_files=('LICENSE.ccby40', 'LICENSE.Unlicensed'),
    packages=['osadl_matrix'],
    package_data={
        'osadl_matrix': ['*.csv', '*.json'],
    },
    install_requires=requirements,
    extras_require={
        'dev': requirements_dev,
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Legal Industry',
        'License :: OSI Approved :: The Unlicense (Unlicense)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
    ],
)
