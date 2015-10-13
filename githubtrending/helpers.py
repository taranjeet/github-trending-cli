from __future__ import ( 
						absolute_import, 
						division, 
						print_function)

import requests
import json
import click
import os
import textwrap

URL = 'http://github-trending.appspot.com'

USER_REQUEST = {
	'REPO'		: 'TRENDINGREPO',
	'DEV'		: 'TRENDINGDEV',
}

FUNCTION_LIST = {
	'REPO'		: 'write_console_repo',
	'DEV'		: 'write_console_dev',
}

def parse_page():

	r = None

	try:
		r = requests.get(URL)
	except Exception as e:
		print ('Error in retriving info. Check your net connection')

	if r.status_code == 200:
		return json.loads(r.text)
	return None

def get_console_size():

	return map(int,os.popen('stty size', 'r').read().split())

def get_print_size_repo():
	
	R,C =  get_console_size()

	idx = 3
	name = 21
	lang = 6
	stars = 5
	desc = 0

	if C <= 80:
		desc = C - 35			# 35 is the sum of idx + name + lang + stars
	elif C>80:

		D = C - 80

		if D < 49:
			half = D/2
		else:
			half = 24			# giving max 45 width to name, rest to desc
		name+=half
		desc+=(D-half)

	size = dict({

		"IDX" 		: -idx,
		"NAME"		: -name,
		"LANG" 		: -lang,
		"STARS"		: -stars,
		"DESC"		: -desc
		}
	)

	return type('Enum',(),size)

def get_print_size_dev():

	R,C = get_console_size()

	idx = 3
	C-=idx
	name = int(C/3)
	desc = C - name

	size = dict({
		"IDX"		: -idx,
		"NAME"		: -name,
		"DESC"		: -desc
		})

	return type('Enum',(),size)



def get_color_code_repo():

	''' color code for the trending repositories'''

	color = dict({

		"IDX" 		: "white",
		"NAME"		: "yellow",
		"LANG" 		: "red",
		"STARS"		: "green",
		"DESC"		: "blue"

		})

	return type('Enum',(),color)

def get_color_code_dev():

	''' color code for the trending developers'''

	color = dict({

		"IDX" 		: "white",
		"NAME"		: "yellow",
		"DESC"		: "blue"

		})

	return type('Enum',(),color)

def write_console_repo(repos):
	
	# NO NAME LANGUAGES STARS DESCRIPTION

	SIZE = get_print_size_repo()
	COLOR = get_color_code_repo()
	click.echo()
	click.secho("%*s" % (SIZE.IDX,'#'), nl=False, bold=True)
	click.secho("%*s" % (SIZE.NAME,"USER/REPO"), nl=False, bold=True)
	click.secho("%*s" % (SIZE.LANG,"LANG"), nl=False, bold=True)
	click.secho("%*s" % (SIZE.STARS,"STAR"), nl=False, bold=True)
	click.secho("%*s" % (SIZE.DESC,"DESCRIPTION"), nl=False, bold=True)

	for idx,eachRepo in enumerate(repos):
		click.echo()
		click.secho("%*s" % (SIZE.IDX,str(idx+1)), nl=False, bold=True,fg=COLOR.IDX)
		click.secho("%*s" % (SIZE.NAME,eachRepo['NAME']), nl=False, bold=True,fg=COLOR.NAME)
		click.secho("%*s" % (SIZE.LANG,eachRepo['LANG']), nl=False, bold=True,fg=COLOR.LANG)
		click.secho("%*s" % (SIZE.STARS,eachRepo['STAR']), nl=False, bold=True,fg=COLOR.STARS)
		click.secho("%*s" % (SIZE.DESC,eachRepo['DESC']), bold=True,fg=COLOR.DESC)

def write_console_dev(devs):
	
	# NO NAME DESC

	SIZE = get_print_size_dev()
	COLOR =  get_color_code_dev()

	click.echo()
	click.secho("%*s" % (SIZE.IDX,'#'), nl=False, bold=True)
	click.secho("%*s" % (SIZE.NAME,"USER/REPO"), nl=False, bold=True)
	click.secho("%*s" % (SIZE.DESC,"DESCRIPTION"), nl=False, bold=True)

	for idx,eachDev in enumerate(devs):
		click.echo()
		click.secho("%*s" % (SIZE.IDX,str(idx+1)), nl=False, bold=True,fg=COLOR.IDX)
		click.secho("%*s" % (SIZE.NAME,eachDev['NAME']), nl=False, bold=True,fg=COLOR.NAME)
		click.secho("%*s" % (SIZE.DESC,eachDev['DESC']), bold=True,fg=COLOR.DESC)


def base_data(lang):
	result =  parse_page()
	eval(FUNCTION_LIST[lang]+'({0})'.format(result[USER_REQUEST[lang]]))
	# write_console_repo(repos[USER_REQUEST[lang]])

if __name__ == '__main__':
	base_data('REPO')

