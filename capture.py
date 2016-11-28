#!/usr/bin/env python

from scapy.all import *
from rules import *
from logger import *
from pidfind import *

def cap():
   rules = getRules('./rules.file')
   sniff(iface = 'eth0', prn=customPrn(rules), store=0)

def customPrn(rules):
   def processPacket(pkt):
      pktInfo = processHeader(pkt)
      pktInfo['content'] = str(pkt).encode("HEX")
      pktInfo['msg'] = ''
      alert = processData(pktInfo, rules)
      if alert:
         print pktInfo['msg']
         pidNum = pidfind(pktInfo)
         logNetAlert(pktInfo, pidNum)
   return processPacket

def processHeader(pkt):
   info = {}
   proto = ''
   ipSrc = 0
   sPort = 0
   ipDst = 0
   dPort = 0

   if IP in pkt:
      ipSrc = pkt[IP].src
      ipDst = pkt[IP].dst
   if TCP in pkt:
      proto = 'tcp'
      sPort = pkt[TCP].sport
      dPort = pkt[TCP].dport
   elif UDP in pkt:
      proto = 'udp'
      sPort = pkt[UDP].sport
      dPort = pkt[UDP].dport

   info['proto'] = str(proto)
   info['srcip'] = str(ipSrc)
   info['srcport'] = str(sPort)
   info['dstip'] = str(ipDst)
   info['dstport'] = str(dPort)

   return info

def processData(pkt, rules):
   indices = []
   idx = {}
   for key in rules.keys():
      idx[key] = getIdx(rules[key], pkt[key])
      for num in idx[key]:
         indices.append(num)

   ruleIdx = set(indices)
   for i in ruleIdx:
      hitCount = 0
      for key in rules.keys():
         if pkt[key] == rules[key][i] or rules[key][i] == '*':
            hitCount = hitCount + 1
         elif key == 'content':
            if rules[key][i].encode("HEX") in pkt[key]:
               hitCount = hitCount + 1
      if hitCount == 6:
         pkt['msg'] = rules['msg'][i]
	      #pidfind(pkt)
         return True

def getIdx(refList, qry):
   idx = [i for i, x in enumerate(refList) if x == qry]
   return idx
