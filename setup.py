from setuptools import setup, find_packages


setup(
  name='coatlib',
  version='0.1.0',
  packages=find_packages(include=['coatlib', 'coatlib.*']),
  install_requires=['timm == 1.0.9', 'einops']
)
