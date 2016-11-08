#!/usr/bin/env python

import os
import sys
from fsc import fsCheck

fstype = ""

if sys.platform == 'linux2' or sys.platform == 'linux': # sets the root directory and logfile location based on the current os
	fstype = '/'
elif sys.platform == 'win32':
	fstype = 'C:/'
else:
	print sys.platform  + " is not supported." # if the os used is not linux or windows and error is thrown
	exit(0)
	
print 'Welcome to HybrIDS'

reply = raw_input('Would you like to monitor file system?{y/n}\n')

if reply == 'y':
	fsCheck('/home/fps305', 10)
else:
	print 'DONE'
