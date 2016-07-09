# -*- coding: utf-8 -*-
import click
import requests
import webbrowser
from lxml import etree

from . import writers

TRENDING_REPO_URL = 'http://github.com/trending'
TRENDING_DEV_URL = 'http://github.com/trending/developers'
HOME_PAGE = 'https://github.com'

requests.packages.urllib3.disable_warnings()


def replace_new_lines_and_strip(s):
    return s.strip()


def replace_new_lines_and_multiple_spaces(s):
    return ' '.join(s.replace('\n', '').split())


def read_page(url, timeout=5):

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0'}
    try:
        response = requests.get(url, timeout=timeout, headers=headers)
    except requests.exceptions.ConnectionError as e:  # noqa
        return(None, False)

    return(response, response.status_code)


def make_etree(url):
    response, status_code = read_page(url)
    if status_code == 200:
        response = etree.HTML(response.text)
    return (response, status_code)


def get_trending_repo_names(tree):
    repos = tree.xpath('//h3[@class="repo-list-name"]/a/@href')
    return repos


def get_trending_repo_description(tree):
    repo_desc = tree.xpath('//p[@class="repo-list-description"]')
    repo_desc = [" ".join([x for x in each.itertext()]) for each in repo_desc]
    repo_desc = [replace_new_lines_and_strip(each) for each in repo_desc]
    return repo_desc


def get_trending_repo_meta(tree):
    repo_meta = tree.xpath('//p[@class="repo-list-meta"]')
    return repo_meta


def get_trending_repo_stars_and_languages(repo_meta):
    dot = u'•'.encode('utf8')
    repo_stars_and_langauges = []
    for each in repo_meta:
        meta = each.text.strip().encode('utf8')
        stars, language = '', 'unknown'
        if dot in meta:
            temp = meta.split(dot)
            for each_option in temp:
                if b"stars" in each_option:
                    stars = replace_new_lines_and_strip(each_option).decode('utf8')
                elif b"built by" not in each_option.lower() and b"stars" not in each_option.lower():
                    language = replace_new_lines_and_strip(each_option).decode('utf8')
            repo_stars_and_langauges.append([stars, language])
    return repo_stars_and_langauges


def get_trending_repos(**kwargs):
    repos = []
    language = kwargs.get('language', None)
    timespan = kwargs.get('timespan', None)
    url = TRENDING_REPO_URL
    if language:
        url = url + '/' + language
    if timespan:
        url = url + '?since={}'.format(timespan)
    tree, status_code = make_etree(url)
    if status_code == 200:
        repo_names = get_trending_repo_names(tree)
        repo_desc = get_trending_repo_description(tree)
        repo_meta = get_trending_repo_meta(tree)
        repo_stars_and_languages = get_trending_repo_stars_and_languages(repo_meta)
        repos = list(zip(repo_names, repo_desc, repo_stars_and_languages))
        repos = [{'repo_name': repo_name,
                  'description': description,
                  'stars': stars,
                  'language': lang,
                  'url': HOME_PAGE + str(repo_name)}
                 for repo_name, description, [stars, lang] in repos]
    return repos


def get_trending_dev_names(tree):
    devs = tree.xpath('//h2[@class="user-leaderboard-list-name"]')
    devs = [" ".join([x for x in each.itertext()]) for each in devs]
    devs = [replace_new_lines_and_multiple_spaces(replace_new_lines_and_strip(each)) for each in devs]
    return devs


def get_trending_dev_repo_names(tree):
    dev_repo_names = tree.xpath('//span[@class="repo"]')
    dev_repo_names = [" ".join([x for x in each.itertext()]) for each in dev_repo_names]
    dev_repo_names = [replace_new_lines_and_strip(each) for each in dev_repo_names]
    return dev_repo_names


def get_trending_dev_repo_desc(tree):
    dev_repo_desc = tree.xpath('//span[@class="repo-snipit-description css-truncate-target"]')
    dev_repo_desc = [" ".join([x for x in each.itertext()]) for each in dev_repo_desc]
    dev_repo_desc = [replace_new_lines_and_strip(each) for each in dev_repo_desc]
    return dev_repo_desc


def get_trending_devs(**kwargs):
    devs = []
    language = kwargs.get('language', None)
    timespan = kwargs.get('timespan', None)
    url = TRENDING_DEV_URL
    if language:
        url = url + '/' + language
    if timespan:
        url = url + '?since={}'.format(timespan)
    tree, status_code = make_etree(url)
    if status_code == 200:
        dev_names = get_trending_dev_names(tree)
        dev_repo_names = get_trending_dev_repo_names(tree)
        dev_repo_desc = get_trending_dev_repo_desc(tree)
        devs = list(zip(dev_names, dev_repo_names, dev_repo_desc))
        devs = [{'dev_name': dev_name,
                 'repo_name': repo_name,
                 'description': description,
                 'url': HOME_PAGE + '/' + dev_name.split(' ')[0]}
                for dev_name, repo_name, description in devs]
    return devs


@click.command()
@click.option(
    '--repo', '-r', is_flag=True,
    help="Lists the trending repositories.")
@click.option(
    '--dev', '-d', is_flag=True,
    help="Lists the trending developers.")
@click.option('--lang', '-l', help='Specify the language')
@click.option('--week', 'timespan', flag_value='weekly')
@click.option('--month', 'timespan', flag_value='monthly')
@click.argument('goto', nargs=1, required=False, type=click.INT)
def main(repo, dev, lang, timespan, goto):
    '''
    A command line utility to see the trending repositories
    and developers on Github
    '''
    language = None
    if lang:
        language = str(lang)
    opts = {
        'language': language,
        'timespan': timespan,
    }
    try:
        if repo:
            repos = get_trending_repos(**opts)
            if goto:
                webbrowser.open(repos[goto-1]['url'], new=2)
                return
            else:
                writers.print_trending_repos(repos)
        if dev:
            devs = get_trending_devs(**opts)
            if goto:
                webbrowser.open(devs[goto-1]['url'], new=2)
                return
            else:
                writers.print_trending_devs(devs)
        # if the user does not passes any argument then list the trending repo
        if not repo and not dev:
            repos = get_trending_repos(**opts)
            if goto:
                webbrowser.open(repos[goto-1]['url'], new=2)
                return
            else:
                writers.print_trending_repos(repos)
        return
    except Exception as e:
        click.secho(e.message, fg="red", bold=True)

if __name__ == '__main__':
    main()
