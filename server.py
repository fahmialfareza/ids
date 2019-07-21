from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ryu.lib import pcaplib
from ryu.lib.packet import packet
from bloom_filter import BloomFilter
from threading import Thread
from sys import argv
import hashlib, socket,signal,sys, struct,json, datetime, os, errno, select, signal, time

data = BloomFilter()

class L2Switch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(L2Switch, self).__init__(*args, **kwargs)
        self.pcap_writer = pcaplib.Writer(open('dump.pcap', 'wb'))
        master_server = MasterServer(7999)
        master_server.start()

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        # Dump Packet
        self.pcap_writer.write_pkt(ev.msg.data)

        # Hash
        m = hashlib.md5()
        m.update(str(ev.msg.data).encode("HEX"))
        data.add(str(m.hexdigest()))
        # End Hash

        msg = ev.msg
        dp = msg.datapath
        ofp = dp.ofproto
        ofp_parser = dp.ofproto_parser

        actions = [ofp_parser.OFPActionOutput(ofp.OFPP_FLOOD)]
        out = ofp_parser.OFPPacketOut(
            datapath=dp, buffer_id=msg.buffer_id, in_port=msg.in_port,
            actions=actions)
        dp.send_msg(out)

class ServerTask(Thread):

    def __init__(self, server, client_socket):
        Thread.__init__(self)
        self.server = server
        self.client_socket = client_socket

    def run(self):
        try:
            while True:
                message = self.client_socket.recv(5128)
                if (len(message)>0):
                    message = message.decode("utf-8")
                    message = json.loads(message)

                    message = {'status': str(message['hash']) in data}
                    self.client_socket.sendall((json.dumps(message)).encode('utf-8'))
                time.sleep(1)
        except Exception, e:
            print 'client break'
            client_sockets = self.server.client_sockets
            client_socket = self.client_socket
            client_sockets.remove(client_socket)
            print e

class MasterServer(Thread):
    '''
    server for master, shows that it is alive
    '''
    def __init__(self, port):
        Thread.__init__(self)
        self.client_sockets = []
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', port))

    def run(self):

        self.server_socket.listen(5)
        while True:
            (client_socket, addr) = self.server_socket.accept()
            self.client_sockets.append(client_socket)
            server_task = ServerTask(self, client_socket)
            server_task.start()
