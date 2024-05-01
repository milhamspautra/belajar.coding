import time 
import random
print("selamat datang di game tebak angka")
print("di game ini anda harus bisa menebak")
print("angka yang dipilih oleh komputer")
print("yang berkisar antara 0-10")

for x in range(3):
    time.sleep(1)
    print("mohon tunggu...",x)
print("mari mulai permainan")

lanjut = True
while lanjut : 
    komputer = random.randint(1,10)
    tebakan = 0 

    while tebakan != komputer:
        tebakan = int(input("masukkan angka: "))
        if tebakan == komputer :
            print("anda benar, maka yang saya pilih", komputer)
        else :
            print("jawaban anda salah")

    stop = input("apakah anda ingin lanjut ? y/n")
    if stop == "y":
        lanjut=False 
print("permainan selesai") 







