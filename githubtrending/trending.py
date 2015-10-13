import click

from .helpers import base_data


@click.command()
@click.option('--repo', '-r', is_flag=True, help="Lists the trending repositories.")
@click.option('--dev', '-d', is_flag=True, help="Lists the trending developers.")
def cli(repo,dev):
	'''
	A command line utility to see the trending repositories and developers on Github
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