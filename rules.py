#!/usr/bin/env python

import sys
import re
import socket

def getRules(fileName):

   fin = open(fileName, 'r')
   lines = fin.readlines()
   rulesD = checkRules(lines)
   #print str(rulesD)
   return rulesD

def checkRules(lines):
   rulesList = {'proto': [],
                'srcip': [],
                'srcport': [],
                'dstip': [],
                'dstport': [],
                'content': [],
                'msg': []
   }

   for line in lines:
      if '#' in line:
         continue
      tokens = line.split(' ', 6)
      if len(tokens) < 7:
         sys.stderr.write("Rule syntax error!");
         exit(-1);
      elif not isinstance(tokens[6], str):
         sys.stderr.write("Incorrect message!");
         exit(-1)
      else:
         rulesList['proto'].append(tokens[0])
         if tokens[1] == 'local':
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("utsa.edu", 80))
            ip = s.getsockname()[0]
            rulesList['srcip'].append(str(ip))
         else:
            rulesList['srcip'].append(tokens[1])
         rulesList['srcport'].append(tokens[2])
         rulesList['dstip'].append(tokens[3])
         rulesList['dstport'].append(tokens[4])
         if tokens[5].startswith('"') and tokens[5].endswith('"'):
            ruleContent = tokens[5][1:-1]
            rulesList['content'].append(ruleContent)
         else:
            rulesList['content'].append(tokens[5])
         ruleMsg = tokens[6][1:-2]
         rulesList['msg'].append(ruleMsg)
   return rulesList
