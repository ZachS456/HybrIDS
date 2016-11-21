#!/usr/bin/env python

import sys

def getRules(fileName):
   
   fin = open(fileName, 'r')
   lines = fin.read()

   checkRules(lines)

   return lines

def checkRules(lines):
   for line in lines:
      tokens = line.split(' ', 6)
      if len(tokens) < 7:
         sys.stderr.write("Rule syntax error!");
         exit(-1);
      elif not isinstance(tokens[6], str):
         sys.stderr.write("Incorrect message!");
         exit(-1)


