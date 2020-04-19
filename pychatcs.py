import configparser
from  main_func import *


def change(type1):

	config = configparser.ConfigParser()
	config['COMMAND'] = {'TYPE': type1}


	with open('autocmdsender.ini', 'w') as configfile:
		config.write(configfile)
