Github Trending Cli
===================

[![PyPI version](https://badge.fury.io/py/github-trending.svg)](https://badge.fury.io/py/github-trending)

This python package lists the trending repositories from github.
A Cli for Github trending repositories

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

```

Licence
====
Open sourced under [MIT License](LICENSE.txt)

Package Link
============

Pypi [link](https://pypi.python.org/pypi/github-trending)

