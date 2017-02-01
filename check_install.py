#!/bin/env python3

print('Run Python installation test for PCut code')

import os
import sys
major, minor = sys.version_info.major, sys.version_info.minor

if major is not 3:
    raise Exception('please use Python 3, you have Python {}.'.format(major))

try:
    import numpy
    import jupyter
    import scipy

except:
    print('A package is missing.')
    print('Install the package below with the necessary '
          'package manager s.a. pip or conda, brew, apt-get, yum, pacman, etc.')
    raise

print('Successful installation of Python {}.{} and '
      'most of the packages required to run the code.'.format(major, minor))
