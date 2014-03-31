# -*- coding: utf-8 -*-

import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import switch


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--doctest-modules', 'switch']
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='switch',
    version=switch.__version__,
    author='Dariusz Górecki',
    author_email='darek.krk@gmail.com',
    url='https://github.com/canni/switch',
    description='The missing switch statement',
    packages=find_packages(exclude=['*.tests']),
    keywords=['switch'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    license='BSD License',
    test_suite='switch.tests',
    tests_require=['pytest'],
    cmdclass = {'test': PyTest},
    zip_safe=True,
    platforms=['any'],
)
