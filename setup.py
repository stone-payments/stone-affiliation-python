"""
Modulo para setup de distribuição
"""
from setuptools import setup, find_packages

setup(name="stone_affiliation",
      version="0.4.0",
      description="Stone Affiliation API client",
      long_description=open("README.md").read().strip(),
      author="Dev RC",
      author_email="devrc@stone.com.br",
      url="https://github.com/stone-payments/stone-affiliation-python/",
      py_modules=["stone_affiliation"],
      packages=find_packages(exclude=["tests"]),
      license="MIT License",
      zip_safe=False,
      keywords="stone affiliation client",
      classifiers=["sdk", "client"])
