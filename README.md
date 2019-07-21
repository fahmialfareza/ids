# ids_python
Tugas Akhir Sistem Forensik Digital menggunakan IDS

Alat yang harus digunakan.
> Mininet
> Ryu Controller
> VSCode

Cara penggunaan
- Bentuk topologi SDN pada mininet
- Sambungkan topologi pada mininet dengan controller
- Jalankan controller ryu dengan kode dari file server.py
  ryu-manager server.py
- Jalankan topologi mininet
- ping host1 ke host2
  h1 ping h2
- pada host 2 jalankan kode client.py
  h2 python client.py
- ambil satu hash yang keluar dari program client.py
- Jalankan kode client-dummy.py pada komputer asli diluar host mininet, dengan parameter salah satu hash
  python client-dummy.py 39kj2nh4j3nj2nk432n4jk232
- Jika hash ada maka akan mengembalikan result True, jika hash tidak ada maka akan mengembalikan result False
