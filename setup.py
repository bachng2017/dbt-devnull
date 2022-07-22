#!/usr/bin/env python
from setuptools import find_namespace_packages, setup
from os import path

package_name = "dbt-devnull"
# make sure this always matches dbt/adapters/devnull/__version__.py
package_version = "1.1.0b1"
description = """The devnull adapter plugin for dbt"""

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=package_name,
    version=package_version,
    license='Apache',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="bachng",
    author_email="bachng@gmail.com",
    url="https://github.com/bachng2017/dbt-devnull",
    packages=find_namespace_packages(include=['dbt', 'dbt.*']),
    include_package_data=True,
    install_requires=[
        "dbt-core==1.1.0",
    ]
)
