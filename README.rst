Github Trending Cli
===================

[![PyPI version](https://badge.fury.io/py/github-trending.svg)](https://badge.fury.io/py/github-trending)

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
