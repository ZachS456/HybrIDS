#!/usr/bin/env python

import time
import cPickle as pickle

def logNetAlert(pkt, mesg):
   logFile = '/var/log/.hyrbids.log'
   fout = open(logFile, 'ab')

   curTime = time.time()

   # insert the pid

   logLine = '%s: %f %d %s %s %s %s\n' % pkt['msg'], curTime, pid, \
      str(pkt['srcip']), str(pkt['srcport']), str(pkt['dstip']), \
      str(pkt['dstport'])

   pickle.dump(logLine, fout)

def logFSAlert():
   print 'FS Alert'

def printLog():
   logFile = '/var/log/.hybrids.log'
   fin = open(logFile, 'rb')

   logs = pickle.load(fin)

   print str(logs)
