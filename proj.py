#!/usr/bin/env python

import os
import sys
from fsc import fsCheck
from fsc import sysScan
from crontab import CronTab

if sys.platform != 'linux2' and sys.platform != 'linux': 
	print sys.platform  + " is not supported."
	exit(0)
	
print 'Welcome to HybrIDS v0.1'

if not os.path.isfile("saver.p"):
	try:
		reply = raw_input('We noticed that you have not run the initial scan\nWould you like run it now?\n')
		if reply == 'y' or reply == 'yes':
			fsCheck('/home/Zach')
		else:
			print 'Nothing to be done'
	except KeyboardInterrupt:
		print "Have a nice day."
		exit(0)
else:
	path = os.path.realpath(__file__)
	print "What would you like to do?\n"
	print "init - Initialize a snapshot of your system"
	print "scannow - Perform a scan of the system against the system snapshot"
	print "setscan - Set a perodic scan of your system"
	print "exit - terminate the program"
	try:
		reply = raw_input('\n')
		while True:
			if(reply == 'init'):
				fsCheck('/home/Zach')
				break
			elif(reply == 'scannow'):
				sysScan('/home/Zach')
				break
			elif(reply == 'setscan'):
				answer = raw_input('How often would you like to scan\n')
				user_cron = CronTab()
				job = user_cron.new(command='echo sysScan | ' + path)
				job.minute.every(int(answer))
				if(job.is_valid):
					job.enable()
					user_cron.write_to_user(user=True)
					print "The job has been created and will run every " + answer
					exit(0)
				else:
					print "There was an error creating the job"
					exit()
			elif(reply == 'exit'):
				print "Have a nice day."
				exit(0)
			else:
				print 'that is not an option please try again'
				reply = raw_input()
	except KeyboardInterrupt:
		print "Have a nice day."
		exit(0)
	  
