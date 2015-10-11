import click

from helpers import base_data


@click.command()
@click.option('--lang', help="Specify the language here.",default='ALL')

def cli(lang):
	'''
	A command line utility to see the trending repositories and developers on Github
	'''

	base_data(lang.upper())


if __name__ == '__main__':
	cli()