#!/usr/bin/env python

import time
import cPickle as pickle

def logNetAlert(pkt, pid):
   logFile = '/var/log/.hyrbids.log'
   fout = open(logFile, 'ab')

   curTime = time.time()

   if(pid == ''):
      pid = ''

   logLine = '%s: %f %s %s %s %s %s\n' % pkt['msg'], curTime, pid, \
      str(pkt['srcip']), str(pkt['srcport']), str(pkt['dstip']), \
      str(pkt['dstport'])

   pickle.dump(logLine, fout)

def printLog():
   logFile = '/var/log/.hybrids.log'
   fin = open(logFile, 'rb')

   logs = pickle.load(fin)

   print str(logs)

def logCheck():
   logFile = '/var/log/.hybrids.log'
   fin = open(logFile, 'rb')
   initRead = fin.read()
   fin.close()
   time.sleep(10)
   while True:
      fin = open(logFile, 'rb')
      contents = fin.read()
      if initRead != contents:
         print 'Alert: Check log file!'
      fin.close()
      time.sleep(10)
