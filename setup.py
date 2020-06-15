"""
pyrtf-ng - The next generation in Rich Text Format documents for Python.

pyrtf-ng is a pure python module for the efficient creation and parsing of rich
text format documents. Supports styles, tables, cell merging, jpg and png
images and tries to maintain compatibility with as many RTF readers as
possible. 
"""

import os
import sys
from distutils.core import setup
from setuptools import setup, find_packages

classifiers = """\
        Development Status :: 4 - Beta
        Topic :: Text Editors :: Text Processing
        Topic :: Software Development :: Libraries :: Python Modules
        Intended Audience :: Developers
        Programming Language :: Python
        License :: OSI Approved :: MIT
"""

doclines = __doc__.split("\n")

setup(
    name='pyrtf-ng',
    version=open('VERSION').read().strip(),
    author='vildritt',
    author_email='maslennikov.alex.g@gmail.com',
    url='https://github.com/vildritt/pyrtf',
    license='MIT',
    platforms=['Any'],
    install_requires=['PyParsing'],
    description=doclines[0],
    long_description='\n'.join( doclines[2:]),
    keywords=('RTF', 'Rich Text', 'Rich Text Format', 'documents',
        'word'),
    packages=find_packages(),
    classifiers=[_line for _line in classifiers.split('\n') if _line],
)
