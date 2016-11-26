#!/usr/bin/env python

import sys
import re

def getRules(fileName):

   fin = open(fileName, 'r')
   lines = fin.readlines()
   rulesD = checkRules(lines)
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
         rulesList['srcip'].append(tokens[1])
         rulesList['srcport'].append(tokens[2])
         rulesList['dstip'].append(tokens[3])
         rulesList['dstport'].append(tokens[4])
         rulesList['content'].append(tokens[5])
         rulesList['msg'].append( tokens[6])
   return rulesList
