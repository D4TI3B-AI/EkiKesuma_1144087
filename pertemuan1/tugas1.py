import time
start_time = time.time()
print("Menghitung nilai rumus matematika menggunakan bahasa jawa")
e = input("Masukan Nilai 1 : ")
k = input("Masukan Nilai 2 : ")
i = input("Masukan Nilai 3 : ")
s = input("Masukan Nilai 4 : ")

if e == 'siji':
	e=1

if e == 'loro':
	e=2

if e == 'telu':
	e=3

if e == 'papat':
	e=4

if e == 'limo':
	e=5

if e == 'enem':
	e=6

if e == 'pitu':
	e=7

if e == 'wolu':
	e=8

if e == 'songo':
	e=9

if e == 'nol':
	e=0


if k == 'siji':
	k=1

if k == 'loro':
	k=2

if k == 'telu':
	k=3

if k == 'papat':
	k=4

if k == 'limo':
	k=5

if k == 'enem':
	k=6

if k == 'pitu':
	k=7

if k == 'wolu':
	k=8

if k == 'songo':
	k=9

if k == 'nol':
	k=0


if i == 'siji':
	i=1

if i == 'loro':
	i=2

if i == 'telu':
	i=3

if i == 'papat':
	i=4

if i == 'limo':
	i=5

if i == 'enem':
	i=6

if i == 'pitu':
	i=7

if i == 'wolu':
	i=8

if i == 'songo':
	i=9

if i == 'nol':
	i=0


if s == 'siji':
	s=1

if s == 'loro':
	s=2

if s == 'telu':
	s=3

if s == 'papat':
	s=4

if s == 'limo':
	s=5

if s == 'enem':
	s=6

if s == 'pitu':
	s=7

if s == 'wolu':
	s=8

if s == 'songo':
	s=9

if s == 'nol':
	s=0

jumlah = ((e * k)*i) / ((i + s)*k)
print('hasil penjumlahan' ,jumlah)
print("time : %s detik " % (time.time() - start_time))