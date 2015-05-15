#!/usr/bin/env python

from setuptools import setup, find_packages

import numpy as np
from Cython.Build import cythonize

include_path = [np.get_include()]

ext_modules = cythonize('pyembree/*.pyx', language='c++', 
                        include_dirs=include_path)
for ext in ext_modules:
    ext.include_dirs = include_path
    ext.libraries = ["embree"]

setup(
    name="pyembree",
    ext_modules=ext_modules,
    packages=find_packages(),
    package_data = {'pyembree': ['*.pxd']}
)
