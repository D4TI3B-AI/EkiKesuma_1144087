import sys
print("Langkah Benar 2-3-4-5-6-7-4-5-8\n")
print (" 1.Petani Menyebrang\n 2.Petani Kembali\n 3.Ayam Menyeberang\n 4.Ayam Kembali\n 5.Gabah Menyebrang\n 6.Gabah Kembali\n 7.Harimau Menyebrang\n 8.Harimau Kembali")
def game():
    print('Posisi Kiri : (p,a,g,h) (1,1,1,1)\nPosisi Kanan : (p,a,g,h) (0,0,0,0)')
    a = input("Langkah 1 : ")
    if a == '2'    : b = input("Posisi Kiri : (p,a,g,h) (0,0,1,1)\nPosisi Kanan : (p,a,g,h) (1,1,0,0)\n Langkah 2 : ")
    else           : print('Game Over')
    if b == '3'    : c = input("Posisi Kiri : (p,a,g,h) (1,0,1,1)\nPosisi Kanan : (p,a,g,h) (0,1,0,0)\nLangkah 3 : ")
    else           : print('Game Over')
    if c == '4'    : d = input("Posisi Kiri : (p,a,g,h) (0,0,1,0)\nPosisi Kanan : (p,a,g,h) (1,1,0,1)\nLangkah 4 : ")
    else           : print('Game Over')
    if d == '5'    : e = input("Posisi Kiri : (p,a,g,h) (1,1,1,0)\nPosisi Kanan : (p,a,g,h) (0,0,0,1)\nLangkah 5 : ")
    else           : print('Game Over')
    if e == '6'    : f = input("Posisi Kiri : (p,a,g,h) (0,1,0,0)\nPosisi Kanan : (p,a,g,h) (1,0,1,1)\nLangkah 6 : ")
    else           : print('Game Over')
    if f == '7'    : g = input("Posisi Kiri : (p,a,g,h) (1,1,0,0)\nPosisi Kanan : (p,a,g,h) (0,0,1,1)\nLangkah 7 : ")
    else           : print('Game Over')
    if g == '4'    : h = input("Posisi Kiri : (p,a,g,h) (1,1,0,0)\nPosisi Kanan : (p,a,g,h) (1,1,1,0)\nLangkah 7 : ")
    else           : print('Game Over')
    if h == '5'    : i = input("Posisi Kiri : (p,a,g,h) (1,1,0,0)\nPosisi Kanan : (p,a,g,h) (0,0,1,0)\nLangkah 7 : ")
    else           : print('Game Over')
    if i == '8'    : print("Posisi Kiri : (p,a,g,h) (0,0,0,0)\nPosisi Kanan : (p,a,g,h) (1,1,1,1)\nSelamat Anda Berhasil !!")
game()
