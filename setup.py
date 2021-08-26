from setuptools import setup
import os
import sys


setup(
    name='somepackage',
    version="0.1.0",
    author='Stephen Smith',
    license='MPL-2.0',
    packages=['sample'],
   install_requires=[
       'mantid'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
    )
