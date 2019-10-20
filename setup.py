from setuptools import setup, find_packages

import myproject

setup(
    name='myproject',
    version=myproject.__version__,
    url='https://github.com/maet3608/minimal-python-project',
    author='Stefan Maetschke',
    author_email='stefan.maetschke@gmail.com',
    description='Template and example for a minimal Python project',
    packages=find_packages(),
    install_requires=[],
)
