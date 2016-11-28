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
from multiprocessing import *

print 'Welcome to HybrIDS'

tasks = raw_input('Start host and network components?[yes/no]\n')

if tasks == 'y' or tasks == 'yes':
   #hidsProc = threading.Thread(target=hComp)
   #nidsProc = threading.Thread(target=cap)
   flag = 3
   hidsProc = Process(target=hComp, args=(sys.stdin.fileno(), ))
   nidsProc = Process(target=cap)
   hidsProc.start()
   nidsProc.start()
   

else:
   tasks = raw_input('Which individual component to start?[network/host/none]\n')
   if tasks == 'host':
      flag = 2
      #hidsProc = threading.Thread(target=hComp)
      hidsProc = Process(target=hComp, args=(sys.stdin.fileno(),))
      hidsProc.start()
      #hidsProc.join()
   elif tasks == 'network':
      flag = 1
      #nidsProc = threading.Thread(target=cap)
      nidsProc = Process(target=cap)
      nidsProc.start()
   else:
      print 'Hybrids not started'
      print 'Exiting...'
      exit(-1)

#logProc = threading.Thread(target=logCheck)
logProc = Process(target=logCheck)
logProc.start()

while True:
   quit = raw_input('To kill program type "kill"\n')
   if quit == 'kill':
      if flag == 3:
         hidsProc.terminate()
         nidsProc.terminate()
         logProc.terminate()
         sys.exit(0)
      elif flag == 2:
         hidsProc.terminate()
         logProc.terminate()
         exit(0)
      elif flag == 1:
         nidsProc.terminate()
         logProc.terminate()
         exit(0)
   else:
      print 'Error: type kill, not %s\n' % (quit)
      continue
