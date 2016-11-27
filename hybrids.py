#!/usr/bin/env python

import sys
import time
import cPickle as pickle
import os
import hashlib
import datetime
import subprocess
import datetime
import threading
#from crontab import CronTab
from scapy.all import *
from fsc import *
from capture import *
from hostComp import *
from rules import *
from logger import *
from multiprocessing import Process

print 'Welcome to HybrIDS'

tasks = raw_input('Start host and network components?[yes/no]\n')

if tasks == 'y' or tasks == 'yes':
   hidsProc = threading.Thread(target=hComp)
   nidsProc = threading.Thread(target=cap)
   hidsProc.start()
   nidsProc.start()

else:
   tasks = raw_input('Which individual component to start?[network/host/none]\n')
   if tasks == 'host':
      hidsProc = threading.Thread(target=hComp)
      hidsProc.start()
   elif tasks == 'network':
      nidsProc = threading.Thread(target=cap)
      nidsProc.start()
   else:
      print 'Hybrids not started'
      print 'Exiting...'
      exit(-1)

logProc = threading.Thread(target=logCheck)
logProc.start()
