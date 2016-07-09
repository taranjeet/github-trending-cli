import click

from . import utils


def print_title(is_repo=True):
    rows, cols = utils.get_console_size()
    title = "TRENDING {} ON GITHUB".format("REPOSITORIES" if is_repo else "DEVELOPERS")
    click.echo()
    click.secho("%s" % ('#'*cols), bold=True)
    click.secho("%*s" % (cols//2, title), bold=True)
    click.secho("%s" % ('#'*cols), bold=True)


def print_headers(print_size, is_repo=True):

    print_title(is_repo)
    click.echo()

    if is_repo:
        click.secho(
            "%*s" % (print_size["IDX"], '#'),
            nl=False, bold=True)
        click.secho(
            "%*s" % (print_size["NAME"], "USER/REPO"),
            nl=False, bold=True)
        click.secho(
            "%*s" % (print_size["LANG"], "LANG"),
            nl=False, bold=True)
        click.secho(
            "%*s" % (print_size["STAR"], "STAR"),
            nl=False, bold=True)
        click.secho(
            " %s" % ("DESCRIPTION"),
            nl=False, bold=True)
    else:
        click.secho("%*s" % (print_size["IDX"], '#'), nl=False, bold=True)
        click.secho("%*s" % (print_size["DEV"], "DEV"), nl=False, bold=True)
        click.secho("%*s" % (print_size["REPO"], "REPO"), nl=False, bold=True)
        click.secho(" %s" % ("DESCRIPTION"), nl=False, bold=True)


def print_trending_repos(data):

    print_size = utils.get_print_size_for_repo(data)
    COLOR = utils.get_color_code()

    print_headers(print_size)

    for idx, each in enumerate(data):
        repo_name = each.get('repo_name')
        description = each.get('description')
        stars = each.get('stars')
        language = each.get('language')
        click.echo()
        click.secho(
            "%*s" % (print_size["IDX"], str(idx+1)),
            nl=False, bold=True, fg=COLOR['IDX'])
        click.secho(
            "%*s" % (print_size["NAME"], repo_name),
            nl=False, bold=True, fg=COLOR['NAME'])
        click.secho(
            "%*s" % (print_size["LANG"], language),
            nl=False, bold=True, fg=COLOR['LANG'])
        click.secho(
            "%*s" % (print_size["STAR"], stars),
            nl=False, bold=True, fg=COLOR['STARS'])
        click.secho(
            " %s" % (description),
            nl=False, bold=True, fg=COLOR['DESC'])
    print('')


def print_trending_devs(data):

    print_size = utils.get_print_size_for_dev(data)
    COLOR = utils.get_color_code()

    print_headers(print_size, is_repo=False)

    for idx, each in enumerate(data):
        click.echo()
        dev_name = each.get('dev_name')
        repo_name = each.get('repo_name')
        description = each.get('description')
        click.secho(
            "%*s" % (print_size["IDX"], str(idx+1)),
            nl=False, bold=True, fg=COLOR['IDX'])
        click.secho(
            "%*s" % (print_size["DEV"], dev_name),
            nl=False, bold=True, fg=COLOR['NAME'])
        click.secho(
            "%*s" % (print_size["REPO"], repo_name),
            nl=False, bold=True, fg=COLOR['REPO'])
        click.secho(
            " %s" % (description),
            nl=False, bold=True, fg=COLOR['DESC'])
    print('')
