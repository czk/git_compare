import os, sys
from gitDiff import *
def parse_config(file_name):
    config_item = ''
    config_list = {}
    f = open(file_name, 'r')
    for line in f:
        tuple = line.split('=')
        if len(tuple) == 2:
            config_list[tuple[0]] = tuple[1][0:(len(tuple[1])-1)]
    return config_list





if __name__=='__main__':
    config = parse_config('config.ini')
    show_diff(config, sys.argv[1:])
