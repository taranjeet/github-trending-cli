Github Trending Cli
===================

[![PyPI version](https://badge.fury.io/py/github-trending.svg)](https://badge.fury.io/py/github-trending) [![Build Status](https://travis-ci.org/staranjeet/github-trending-cli.svg?branch=master)](https://travis-ci.org/staranjeet/github-trending-cli) [![Coverage Status](https://coveralls.io/repos/github/staranjeet/github-trending-cli/badge.svg?branch=master)](https://coveralls.io/github/staranjeet/github-trending-cli?branch=master)

A cli which lists the trending repositories and developers from Github.

Install
=======

* Using `pip`
```
$ pip install github-trending
```

* From source

```
$ git clone https://github.com/staranjeet/github-trending-cli
$ cd github-trending-cli
$ python setup.py install
```

Usage
=====

```
$ githubtrending 				# list 25 trending repositories on github
$ githubtrending --repo or -r   # list 25 trending repositories on github
$ githubtrending --dev or -d    # list 25 trending developers on github
$ githubtrending --lang=python or -l=python
                                # list 25 trending repositories for a particular language on github
$ githubtrending --week         # list 25 trending repositories on github since a week
$ githubtrending --month        # list 25 trending repositories on github since a month

```

Examples
=========

```
$ githubtrending --repo --lang=python --week        # lists 25 trending repositories of python since a week
$ githubtrending --dev --lang=javascript --month    # lists 25 trending developers of javascript since a month
$ githubtrending --repo --week                      # lists 25 repositories since a week
```

Available Options
=================

```

 --help 				Lists the help and option available
 -r, --repo 			Lists 25 trending repositories
 -d, --dev 				Lists 25 trending developers
 -l, --lang             Takes language as a parameter and lists repo of that language
 --week                 Lists trending repos/devs since a week
 --month                Lists trending repos/devs since a month

```

Licence
====
Open sourced under [MIT License](LICENSE.txt)

Package Link
============

Pypi [link](https://pypi.python.org/pypi/github-trending)
