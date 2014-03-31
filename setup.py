# -*- coding: utf-8 -*-

from setuptools import setup

import switch

setup(
    name='switch',
    version=switch.__version__,
    author='Dariusz Górecki',
    author_email='darek.krk@gmail.com',
    url='https://github.com/canni/switch',
    description='The missing switch statement',
    py_modules=['switch'],
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
)
