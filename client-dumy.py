import telnetlib
import sys
from random import randint
import hashlib
import socket,random,json,time

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.connect( ("127.0.0.1", 7999) )

# random
# Fungsi untuk handle packet masuk
def send(hash) :
    data = {'hash':hash}
    tcp_sock.sendall((json.dumps(data)).encode('utf-8'))

    data = tcp_sock.recv(1024)
    data = data.decode('utf-8')
    print(data)

    return data


if __name__ == "__main__":

    if (len(sys.argv) < 2):
        print ("Usage : python client-dumy.py <Hash>")
        exit()

    hash = sys.argv[1]
    send(hash)