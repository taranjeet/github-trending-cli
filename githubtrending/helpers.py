from __future__ import ( 
						absolute_import, 
						division, 
						print_function)

import requests
import json
import click
import os
import textwrap

URL = 'http://localhost:8080/'

USER_REQUEST = {
	'REPO'		: 'TRENDINGREPO',
	'DEV'		: 'TRENDINGDEV',
}

FUNCTION_LIST = {
	'REPO'		: 'write_to_console_repo',
	'DEV'		: 'write_to_console_dev',
}

def L(s):
	'''
	returns length of the string
	'''
	return len(s)

def parse_page():
	'''
	reads the HTML and returns the page source code
	'''

	r = None

	try:
		r = requests.get(URL)
	except Exception as e:
		print ('Error in retriving info. Check your net connection')

	if r.status_code == 200:
		return json.loads(r.text)
	return None

def get_console_size():
	'''
	returns no of rows, no of cols 
	'''
	return map(int,os.popen('stty size', 'r').read().split())

def get_color_code_repo():
	'''
	Color code for the trending repositories
	'''
	color = dict({
		"IDX" 		: "white",
		"NAME"		: "yellow",
		"LANG" 		: "red",
		"STARS"		: "green",
		"DESC"		: "blue"
		})

	return type('Enum',(),color)

def get_color_code_dev():
	'''
	Color code for the trending developers
	'''
	color = dict({
		"IDX" 		: "white",
		"NAME"		: "yellow",
		"DESC"		: "blue"
		})

	return type('Enum',(),color)


def get_col_size(data):
	
	'''
	For each column returns the maximum padding that should be used
	'''

	name, lang, star = [0]*3
	for eachR in data:
		name = max(L(eachR.get("NAME","")),name)
		lang = max(L(eachR.get("LANG","")),lang)
		star = max(L(eachR.get("STAR","")),star)

	return {
		"NAME"	: name+1,
		"LANG"	: lang+1,
		"STAR"	: star+1
	}


def print_each_description(text, descSize, descColor, excludingDescSum, C):
	
	'''
	Special function for printing description in column format
	Implements a bit of string manipulation
	'''

	i = 0

	if L(text) < descSize:
		click.secho("%*s" % (-descSize,text), bold=True, fg=descColor)
	else:
		LN =L(text)

		while i<LN:
			if L(text) < descSize:
				optSize = L(text)
			else:
				# check for space
				if text[descSize] == ' ':
					optSize = descSize
				else:
					lastSpace = text[:descSize+1].rfind(' ')
					if lastSpace == -1:
						lastSpace = descSize
					optSize = lastSpace

			if i == 0:
				click.secho("%*s" % (-descSize,text[:optSize]), bold=True,fg=descColor, nl=False)
			else:
				click.secho("%*s" % (excludingDescSum-1,' '), bold=True,fg=descColor, nl=False)
				click.secho("%*s" % (-C,text[:optSize]), bold=True,fg=descColor)

			text = text[optSize:]
			i+=(optSize+1)


def write_to_console_repo(data):

	''' prints 25 tredning repositories on Github
		NO NAME LANG STARS DESC
	'''
	
	R,C =  get_console_size()

	printSize = get_col_size(data)
	COLOR = get_color_code_repo()

	idx = 3
	name = printSize["NAME"]
	lang = printSize["LANG"]
	star = printSize["STAR"]

	excludingDescSum = idx + name + lang + star
	desc = C - excludingDescSum

	printSize["NAME"] = -name
	printSize["LANG"] = -lang
	printSize["IDX"]  = -idx
	printSize["STAR"] = -star
	printSize["DESC"] = desc
	click.echo()
	click.secho("%*s" % (printSize["IDX"],'#'), nl=False, bold=True)
	click.secho("%*s" % (printSize["NAME"],"USER/REPO"), nl=False, bold=True)
	click.secho("%*s" % (printSize["LANG"],"LANG"), nl=False, bold=True)
	click.secho("%*s" % (printSize["STAR"],"STAR"), nl=False, bold=True)
	click.secho("%*s" % (-printSize["DESC"],"DESCRIPTION"), nl=False, bold=True)
	
	for idx,eachRepo in enumerate(data):
		click.echo()
		click.secho("%*s" % (printSize["IDX"],str(idx+1)), nl=False, bold=True,fg=COLOR.IDX)
		click.secho("%*s" % (printSize["NAME"],eachRepo['NAME']), nl=False, bold=True,fg=COLOR.NAME)
		click.secho("%*s" % (printSize["LANG"],eachRepo['LANG']), nl=False, bold=True,fg=COLOR.LANG)
		click.secho("%*s" % (printSize["STAR"],eachRepo['STAR']), nl=False, bold=True,fg=COLOR.STARS)


		print_each_description(eachRepo["DESC"],printSize["DESC"],COLOR.DESC,excludingDescSum,C)
	

def write_to_console_dev(data):

	''' prints 25 tredning developers on Github
		NO NAME DESC
	'''
	
	R,C =  get_console_size()

	printSize = get_col_size(data)
	COLOR = get_color_code_repo()

	idx = 3
	name = printSize["NAME"]
	lang = printSize["LANG"]
	star = printSize["STAR"]

	excludingDescSum = idx + name + lang + star
	desc = C - excludingDescSum

	printSize["NAME"] = -name
	printSize["LANG"] = -lang
	printSize["IDX"]  = -idx
	printSize["STAR"] = -star
	printSize["DESC"] = desc

	#print the headers
	click.echo()
	click.secho("%*s" % (printSize["IDX"],'#'), nl=False, bold=True)
	click.secho("%*s" % (printSize["NAME"],"USER/REPO"), nl=False, bold=True)
	click.secho("%*s" % (printSize["LANG"],"LANG"), nl=False, bold=True)
	
	for idx,eachRepo in enumerate(data):
		click.echo()
		click.secho("%*s" % (printSize["IDX"],str(idx+1)), nl=False, bold=True,fg=COLOR.IDX)
		click.secho("%*s" % (printSize["NAME"],eachRepo['NAME']), nl=False, bold=True,fg=COLOR.NAME)

		print_each_description(eachRepo["DESC"],printSize["DESC"],COLOR.DESC,excludingDescSum,C)


def base_data(lang):
	result =  parse_page()
	eval(FUNCTION_LIST[lang]+'({0})'.format(result[USER_REQUEST[lang]]))


if __name__ == '__main__':
	base_data('REPO')

