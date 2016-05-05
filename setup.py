#!/usr/bin/env python
import os

from setuptools import setup, find_packages
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

readme = read('README.rst')

setup(
  name = 'pyelasticache_client',
  packages = ['pyelasticache_client'],
  version = '0.1',
  packages=find_packages(),
  install_requires=['six', 'sortedcontainers'],
  description = 'A comprehensive, fast, pure Python memcached client',
  long_description=readme,
  author = 'David Fierro, Guillermo Menéndez, N. Angulo y Charles Gordon',
  author_email = 'backend@touchvie.com',
  url = 'https://github.com/touchvie/pyelasticache_client',
  keywords = ['AWS', 'elasticache', 'memcache', 'autodiscovery'],
  classifiers=[
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: Implementation :: PyPy',
    'License :: OSI Approved :: Apache Software License',
    'Topic :: Database',
 ],
)
