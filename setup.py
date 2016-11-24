#!/usr/bin/env/python
import os
from setuptools import setup

setup(  name='schemegen',
        version='0.1',
        description='Color scheme generator and config manager',
        author='NBonaparte',
        license='GPL 3.0',
        url='https://github.com/NBonaparte/schemegen',
        package_dir = {'': 'py'},
        py_modules=['coloranalyze'],
        scripts=['py/schemegen']
)
