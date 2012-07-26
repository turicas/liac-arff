# -*- coding: utf-8 -*-

__author__ = 'Renato de Pontes Pereira'
__author_email__ = 'renato.ppontes@gmail.com'
__version__ = '1.0'
__date__ = '2012 07 25'

try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

from setuptools import setup, find_packages

f = open('README.rst','rU')
long_description = f.read()
f.close()

setup(
    name = 'liac-arff',
    version = __version__,
    author = __author__,
    license='MIT License',
    description = 'A library for read and write ARFF files in Python',
    long_description=long_description,
    url = 'http://inf.ufrgs.br/~rppereira',
    download_url = 'https://github.com/renatopp/liac-arff',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        ('Topic :: Software Development :: Libraries :: Python Modules'),
        ('Topic :: Scientific/Engineering :: Artificial Intelligence'),
    ],
    keywords='arff weka parser liac python',
    py_modules=['arff'],
    )