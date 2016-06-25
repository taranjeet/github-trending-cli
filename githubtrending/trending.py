# -*- coding: utf-8 -*-
import requests
from lxml import etree

import click

from .helpers import base_data

requests.packages.urllib3.disable_warnings()

def replace_new_lines_and_strip(s):
    return s.replace('\n', '').replace('\r', '').strip()


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
    return repo_desc

def get_trending_repo_meta(tree):
    repo_meta = tree.xpath('//p[@class="repo-list-meta"]')
    return repo_meta

def get_trending_repo_stars_and_languages(repo_meta):
    dot = '•'.decode('utf8').encode('utf8')
    repo_stars_and_langauges = []
    for each in repo_meta:
        meta = each.text.strip().encode('utf8')
        stars, language = '', 'unknown'
        if dot in meta:
            temp = meta.split(dot)
            for each_option in temp:
                if "stars" in each_option:
                    stars = replace_new_lines_and_strip(each_option)
                elif "built by" not in each_option.lower() and "stars" not in each_option.lower():
                    language = replace_new_lines_and_strip(each_option)
            repo_stars_and_langauges.append([stars, language])
    return repo_stars_and_langauges

@click.command()
@click.option(
    '--repo', '-r', is_flag=True,
    help="Lists the trending repositories.")
@click.option(
    '--dev', '-d', is_flag=True,
    help="Lists the trending developers.")
def cli(repo, dev):
    '''
    A command line utility to see the trending repositories
    and developers on Github
    '''
    try:
        if repo:
            base_data('REPO')
            return
        if dev:
            base_data('DEV')
            return
        # if the user does not passes any argument then list the trending repo
        if not(repo and dev):
            base_data('REPO')
            return
    except Exception as e:
        click.secho(e.message, fg="red", bold=True)

if __name__ == '__main__':
    cli()
