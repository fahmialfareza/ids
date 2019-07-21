from scapy.all import *
import telnetlib
import sys
from random import randint
from scapy.layers.inet import *
import hashlib
import socket,random,json,time

# random
# Fungsi untuk handle packet masuk
def handle_packet(packet) :

    m = hashlib.md5()
    m.update(str(packet).encode("HEX"))

    data = {'hash':m.hexdigest()}

    return data
sniff(iface="h2-eth0", filter="ip", prn=handle_packet)
time.sleep(0.1)