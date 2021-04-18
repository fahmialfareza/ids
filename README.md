# IDS with Python

Final Project of Digital Forensics System Course with IDS in my campus

Tools that used:

> Mininet
> Ryu Controller
> VSCode

How to use this code:

- The shape of the SDN topology on the mininet
- Connect the topology to the mininet with the controller
- Run the ryu controller with the code from the server.py file
  ryu-manager server.py
- Run mininet topology
- ping host1 to host2
  h1 ping h2
- on host 2 run client.py code
  h2 python client.py
- get a hash that comes out of the client.py program
- Run client-dummy.py code on a real machine outside the mininet host, with a parameter of one of the hashes
  python client-dummy.py 39kj2nh4j3nj2nk432n4jk232
- If the hash exists it will return the result True, if the hash does not exist it will return the result False
