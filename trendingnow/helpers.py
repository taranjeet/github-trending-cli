import requests
import json
import click
import os
import textwrap

URL = 'http://github-trending.appspot.com'

USER_REQUEST = {
	'ALL'		: 'TRENDINGREPO'
}

def parse_page():

	r = None

	try:
		r = requests.get(URL)
	except Exception,e:
		print 'Error in retriving info. Check your net connection'

	if r.status_code == 200:
		return json.loads(r.text)
	return None

def get_print_size():
	
	R,C =  map(int,os.popen('stty size', 'r').read().split())

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

def get_color_code():

	color = dict({

		"IDX" 		: "white",
		"NAME"		: "yellow",
		"LANG" 		: "red",
		"STARS"		: "green",
		"DESC"		: "blue"

		})

	return type('Enum',(),color)



def base_data(lang):
	repos =  parse_page()
	write_console(repos[USER_REQUEST[lang]])

def write_console(repos):
	
	# NO NAME LANGUAGES STARS DESCRIPTION

	SIZE = get_print_size()
	COLOR = get_color_code()
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





