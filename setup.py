# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# Read dependencies from requirements.txt
with open('requirements.txt') as f:
    install_requires = [pkg for pkg in f.read().splitlines() if pkg.strip()]

# Get version from zk_integration/__init__.py
from zk_integration import __version__ as version

setup(
    name='zk_integration',
    version=version,
    description='Zk Device Integration',
    author='Peter',
    author_email='eng.peter.maged@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
