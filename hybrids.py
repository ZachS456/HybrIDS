#!/usr/bin/env python

import sys
import time
import cPickle as pickle
import os
import hashlib
import datetime
import subprocess
import datetime
#from crontab import CronTab
from scapy.all import *
from fsc import *
from capture import *
from hostComp import *
from rules import *
from logger import *
from multiprocessing import Process

print 'Welcome to HybrIDS'

tasks = raw_input('Start host and network components?\n')

if tasks == 'y' or tasks == 'yes':
   hidsProc = Process(target=hComp)
   nidsProc = Process(target=cap)
   hidsProc.start()
   nidsProc.start()
else:
   tasks = raw_input('Which individual component to start?')
   if tasks == 'host':
      hidsProc = Process(target=hComp)
      hidsProc.start()
   elif tasks == 'network':
      nidsProc = Process(target=cap)
      nidsProc.start()
   else:
      print 'Hybrids not started'
      print 'Exiting...'
      exit(-1)

logProc = Process(target=logCheck)
logProc.start()
