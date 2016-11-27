#!/usr/bin/env python

import os
import sys

def hComp():
   if sys.platform != 'linux2' and sys.platform != 'linux': 
   	print sys.platform  + " is not supported."
   	exit(0)
   if os.geteuid() == 0:
   	direct = '/'
   else:
   	direct = os.path.expanduser('~')
   
   print 'Welcome to HybrIDS v0.1'
   
   if not os.path.isfile("saver.p"):
   	try:
   		reply = raw_input('We noticed that you have not run the initial scan. Would you like run it now?\n')
   		if reply == 'y' or reply == 'yes':
   			fsCheck(os.path.expanduser('~'))
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
   				fsCheck(direct)
   				break
   			elif(reply == 'scannow'):
   				print direct
   				sysScan(direct)
   				break
   			elif(reply == 'setscan'):
   				answer = raw_input('How often would you like to scan\n')
   				user_cron = CronTab(user=True)
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
   	  
