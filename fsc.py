#!/usr/bin/env python

import os
import hashlib
import sys
import time
import pickle
import datetime
import subprocess

def fsCheck(directory):

	digests = {}

	rootdir = directory

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

	try:
		pickle.dump(digests, open('saver.p', 'wb'))
	except:
		print "There was an error initializing"
		exit(-1)

	print "Initial hash complete"

def sysScan(directory):
	try:
		digests = pickle.load(open('saver.p', 'rb'))
	except:
		print "There was an error loading the DB"
		exit(-1)
	
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%m-%d-%Y %H:%M:%S')
	try:
		if not os.path.exists('./logs'):
			subprocess.call(['mkdir', './logs'])
		log = open('./logs/' + st + '.log', 'wb+')
	except Exception,e:
		print e
		print "There was an error opening the logfile"
		exit(-1)
	flag = 0
	rootdir = directory
	query = {}
	log.write('Scan performed on ' + st + '\n')
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
			log.write('WARNING: ' + key + ' removed from file system!!\n')

	log.write('\n')
	for key in query:
		if key not in digests:
			print 'WARNING: %s added to file system!!' % (key)
			log.write('WARNING: ' + key + ' added to file system!!\n')
	log.write('\n')
	for key in digests:
		if key in digests and key in query:
			if digests[key] != query[key]:
				print 'WARNING: %s was changed!!' % (key)
				log.write('WARNING: ' + key + ' was changed!!\n')
	log.write('\n')
	log.close()
	print "Check complete!"
