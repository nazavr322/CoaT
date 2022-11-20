from setuptools import setup


setup(
  name='coatlib',
  version='0.1.0',
  packages=find_packages(include=['coatlib', 'coatlib.*']),
  install_requires=['timm', 'einops']
)
