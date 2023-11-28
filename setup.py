# setup.py

from setuptools import setup, find_packages

setup(
    name='your-package-name',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'tqdm==4.62.2',
        # add other dependencies here
    ],
)
