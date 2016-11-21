#!/usr/bin/env python

import sys
from scapy.all import *

def cap():
   sniff(iface = 'eth0', prn=processPacket, store=0)

def processPacket(pkt):
   processHeader(pkt)
   processData(pkt)

def processHeader(pkt):
   if IP in pkt:
      ipSrc = pkt[IP].src
      ipDst = pkt[IP].dst
   if TCP in pkt:
      sPort = pkt[TCP].sport
      dPort = pkt[TCP].dport

      print 'IP src = ' + str(ipSrc)
      print 'IP dst = ' + str(ipDst)
      print 'Source port = ' + str(sPort)
      print 'Destination Port = ' + str(dPort)
      print ' '

def processData(pkt):
   ruleText = "Secret"
   hexText = ruleText.encode("HEX")
   hexData = str(pkt).encode("HEX")

   regex = re.compile(hexText)
   ret = regex.findall(hexData)

   if len(ret) > 1:
      print 'WARNING'
      exit(0)
