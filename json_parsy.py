#!/usr/bin/env python

'''
Parse JSON data, put content into separate html files, whose names will take the form "alias".html
The files will be organized according to month and year
'''

import sys
import json
import os.path
import datetime
import time

def main():
	#read in data
	json_unclean_string = open(sys.argv[1], 'rU')
	clean_json(json_unclean_string)
	json_data = json.load(json_unclean_string)
	json_unclean_string.close()
	#parse json
	for data in json_data:
		try:
			t = time.strptime(data["modified"], "%Y-%m-%d %H:%M:%S")
		except ValueError:
			t = time.strptime(data["created"], "%Y-%m-%d %H:%M:%S")
		file_path = os.path.join('content', str(t.tm_year), str(t.tm_mon), data["alias"]+'.html')
		dir = os.path.dirname(file_path)
		if not os.path.exists(dir):
			os.makedirs(dir)
		html_file = open(file_path , 'w')
		html_file.write(data["fulltext"].encode('utf-8'))
		html_file.close()

def clean_json(doc_text):
	sarray = []
	for line in doc_text :
        	sarray.append(line.rstrip('\n\r\t'))
   	output = open("clean.json", "w")
	output.write(''.join(sarray))
	#return ''.join(sarray)

if __name__ == "__main__":
	main()
