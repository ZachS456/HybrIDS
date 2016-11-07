#!/usr/bin/env python

import os
import hashlib
import sys
import time

def fsCheck(directory, rate):

	digests = {'' : ''}
	flag = 0

	rootdir = directory
	interval = float(rate)

	print "Initializing..."

	for root, dirs, files in os.walk(rootdir):
		for eaFile in files:
			fileName = os.path.join(root, eaFile)
			if os.path.isfile(fileName):
				try:
					fpin = open(fileName, 'r')
				except IOError:
					#print '%s:\tAccess denied!' % (fileName)
					continue
				try:
					contents = fpin.read()
				except:
					#print '%s:\tUnable to read from file' % (fileName)
					file.close(fpin)
					continue
				file.close(fpin)
				algo = hashlib.sha256()
				algo.update(contents)
				digests[fileName] = algo.hexdigest()

	print "Initial hash complete"

	while True:
		query = {'' : ''}
		for root, dirs, files in os.walk(rootdir):
			for eaFile in files:
				fileName = os.path.join(root, eaFile)
				if os.path.isfile(fileName):
					try:
						fpin = open(fileName, 'r')
					except IOError:
						#print '%s:\tAccess denied!' % (fileName)
						continue
					try:
						contents = fpin.read()
					except:
						#print '%s:\tCould not read from file' % (fileName)
						file.close(fpin)
						continue
					file.close(fpin)
					algo = hashlib.sha256()
					algo.update(contents)
					query[fileName] = algo.hexdigest()
    
		for key in digests:
			if key not in query:
				print 'WARNING: %s removed from file system!!' % (key)
				flag = 1
  
		for key in query:
			if key not in digests:
				print 'WARNING: %s added to file system!!' % (key)
				flag = 1

		for key in digests:
			if key in digests and key in query:
				if digests[key] != query[key]:
					print 'WARNING: %s was changed!!' % (key)
					flag = 1

		print "Check complete!" 
		if flag:
			break

		time.sleep(interval)
