#!/usr/bin/env python
import os
import time
import cPickle as pickle
import subprocess

def logNetAlert(pkt, pid):
   logFile = './logs/net/hybrids.log'
   if os.path.getsize(logFile) > 0:
      fout = open(logFile, 'a')
   else:   
      fout = open(logFile, 'w+')

   curTime = time.time()
   

   if pid == '' or pid is None:
	pid = 'NoPID'
   logLine = '%s: %f %s %s %s %s %s\n' %(pkt['msg'], curTime, pid, \
      str(pkt['srcip']), str(pkt['srcport']), str(pkt['dstip']), \
      str(pkt['dstport']))

   #pickle.dump(logLine, fout)
   fout.write(logLine)

   fout.close()
def printLog():
   logFile = 'logs/net/hybrids.log'
   fin = open(logFile, 'rb')

   logs = pickle.load(fin)

   print str(logs)

def logCheck():
   logFile = 'logs/net/hybrids.log'
   if not os.path.exists(logFile):
      subprocess.call(['touch', logFile])
   fin = open(logFile, 'r')
   initRead = fin.read()
   fin.close()
   time.sleep(10)
   while True:
      fin = open(logFile, 'r')
      contents = fin.read()
      if initRead != contents:
         print 'Alert: Check log file!'
      fin.close()
      time.sleep(10)
