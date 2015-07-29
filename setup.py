#!/usr/bin/env python

from distutils.core import setup
from iotop.version import VERSION

setup(name='iotop',
      version=VERSION,
      description='Per process I/O bandwidth monitor',
      long_description=
'''Iotop is a Python program with a top like UI used to show of behalf of which
process is the I/O going on.''',
      author='Guillaume Chazarain',
      author_email='guichaz@gmail.com',
      url='http://guichaz.free.fr/iotop',
      scripts=['bin/iotop'],
      data_files=[('share/man/man1', ['iotop.1'])],
      packages=['iotop'],
      license='GPL'
)
