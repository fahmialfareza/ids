from scapy.all import *
import hashlib

dict_sender = {}

def handle_packet(paket):
    src_ip = paket[IP].src
    dst_ip = paket[IP].dst

    if ICMP in paket:
        if src_ip not in dict_sender:
            dict_sender[src_ip] = 0
            dict_sender[src_ip] += len(paket[ICMP].payload)
            #print("Fragment ICMP " + str(len(paket[ICMP].payload)))
        else:
            if(dict_sender[src_ip] > 6000):
                m = hashlib.md5()
                m.update(str(paket[ICMP]).encode("HEX"))
                print(" Detect " + str(dict_sender[src_ip]) +"Byte "+" Hash : "+ m.hexdigest())
                dict_sender[src_ip] = 0
                dict_sender[src_ip] += len(paket[ICMP].payload)
    else:
        dict_sender[src_ip] += len(paket[IP].payload)
        #print("Fragment IP " + str(len(paket[IP].payload)))
        #print(paket.show()

sniff(filter="icmp", prn=handle_packet)
