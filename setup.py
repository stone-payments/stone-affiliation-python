"""
Modulo para setup de distribuição
"""
from setuptools import setup, find_packages

setup(name='affiliation_sdk',
      version='0.0.1',
      description='Stone Affiliation API client',
      long_description=open('README.md').read().strip(),
      author='Dev RC',
      author_email='devrc@stone.com.br',
      url='https://github.com/stone-payments/affiliation_sdk/',
      py_modules=['affiliation_sdk'],
      packages=find_packages(exclude=['tests']),
      license='MIT License',
      zip_safe=False,
      keywords='stone affiliation client',
      classifiers=['sdk', 'client'])
