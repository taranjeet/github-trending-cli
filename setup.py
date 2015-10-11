#!/usr/bin/env python

from setuptools import setup
import sys

setup(
    name='github-trending',
    version='1.0',
    description='Trending repos and developers on Github',
    author='Taranjeet Singh',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stablegit
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords = "github trending repo now developers trending-repo",
    author_email='reachtotj@gmail.com',
    url='https://github.com/staranjeet/github-trending-cli',
    packages=['githubtrending'],
    install_requires=[
        "click>=5.0",
        "requests>=2.7.0"
    ] + (["colorama==0.3.3"] if "win" in sys.platform else []),
    entry_points = {
        'console_scripts': [
            'githubtrending = githubtrending.trending:cli'
      ],
    }
)
