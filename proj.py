#!/usr/bin/env python

import os
import sys
from fsc import fsCheck

print 'Welcome to HybrIDS'

reply = raw_input('Would you like to monitor file system?{y/n}\n')

if reply == 'y':
	fsCheck('/home/fps305', 10)
else:
	print 'DONE'
