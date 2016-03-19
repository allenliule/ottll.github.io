#! /usr/bin/env python
#coding=utf8
import os
import sys

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print 'USAGE: commit message'
		sys.exit()
	
	commit_msg = sys.argv[1]
	os.system('git pull origin master')
	os.system('git status')
	os.system('git add ./')
	os.system('git commit * -m "%s"'%commit_msg)
	os.system('git push origin master')