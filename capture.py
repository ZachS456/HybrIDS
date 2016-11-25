#!/usr/bin/env python

import sys
from scapy.all import *

def cap():
   sniff(iface = 'eth0', prn=processPacket, store=0)

def processPacket(pkt):
   rules = pullRules()
   pktInfo = processHeader(pkt)
   pktInfo['content'] = str(pkt).encode("HEX")
   processData(pktInfo, rules)

def processHeader(pkt):
   if IP in pkt:
      ipSrc = pkt[IP].src
      ipDst = pkt[IP].dst
   if TCP in pkt:
      proto = 'tcp'
      sPort = pkt[TCP].sport
      dPort = pkt[TCP].dport
   elif UDP in pkt:
      proto = 'tcp'
      sPort = pkt[UDP].sport
      dPort = pkt[UDP].dport

   info['proto'] = proto
   info['srcip'] = ipSrc
   info['srcport'] = sPort
   info['dstip'] = ipDst
   info['dstport'] = dPort

   return info
      #print 'IP src = ' + str(ipSrc)
      #print 'IP dst = ' + str(ipDst)
      #print 'Source port = ' + str(sPort)
      #print 'Destination Port = ' + str(dPort)
      #print ' '

def processData(pkt, rules):
   idx = {}
   for key in rules.keys():
      if pkt[key] in rules[key]:
         idx{key] = index(pkt[key])

   #gotta play with more stuff   
