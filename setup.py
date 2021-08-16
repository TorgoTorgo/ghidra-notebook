#!/usr/bin/env python3
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

def main():
    setup(
        name='ghidra-notebook',
        version='1.0.0',
        description='Jupyter kernel for Ghidra\'s Python Interpreter',
        author='torgo',
        author_email='torgo@torgo.me',
        license='MIT',
        install_requires=[
            'IPython',
            'ipykernel',
            'jupyter_client',
            'ghidra-bridge',
            'jupyter',
        ],
        packages=find_packages()
    )

if __name__ == '__main__':
    main()
