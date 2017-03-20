graph = {'Alun-Alun': ['Jalan Semeru', 'Wijaya Kusuma','Jogoyudan'],
             'Wijaya Kusuma': ['Jalan Semeru','Jalan Juanda'],
             'Jalan Semeru': ['Wijaya Kusuma','Jalan Juanda','Perum Tukum','Jogoyudan','Perum Suko Asri'],
             'Jogoyudan': ['Jalan Semeru','Perum Tukum'],
             'Perum Tukum': ['Jalan Semeru','Perum Suko Asri'],
             'Jalan Juanda': ['Jalan Semeru','Perum Suko Asri'],
             'Perum Suko Asri': ['Jalan Semeru','Jalan Juanda','Perum Tukum'],
         }
def jalur_terpendek(graph, awal, tujuan, jalur=[]):
        jalur = jalur + [awal]
        if awal == tujuan:
            return jalur
        if not graph.has_key(awal):
            return None
        jalurpendek = None
        for node in graph[awal]:
            if node not in jalur:
                newjalur = jalur_terpendek(graph, node, tujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
print("Jalur Alun-Alun Perum Sukoasri Kota Lumajang")
print ("Alun-Alun,Wijaya Kusuma,Jalan Semeru,Jogoyudan,Perum Suko Asri)")
print ("\n")
awal = raw_input("Masukan Awal : ")
tujuan = raw_input("Masukan Tujuan : ")
hasil = jalur_terpendek(graph, awal, tujuan, jalur=[])
print "Jalur Terpendek", hasil
