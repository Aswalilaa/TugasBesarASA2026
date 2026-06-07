# Nama File : hillClimbing.py
# Pembuat : Aswalila Adha Putri Telaumbanua - 24060124120014
# Kelas : C / Informatika 2024

import time
from Skor import hitung_skor

def jalankan_hill_climbing(hadiah, budget):
    n = len(hadiah)
    dipilih = [False] * n
    harga_total = 0
    skor_total = 0

    # Inisialisasi soluasi awal dengan memilih hadiah secara berurutan samoai budget habis
    for i in range(n):
        if harga_total + hadiah[i]["harga"] <= budget:
            dipilih[i] = True
            harga_total += hadiah[i]["harga"]
            skor_total += hitung_skor(hadiah[i], budget)

    start = time.time()
    ada_perbaikan = True
    while ada_perbaikan:
        ada_perbaikan = False
        for i in range(n):
            for j in range(n):
                # Mengecek apakah hadiah j lebih bagus dari hadiah i
                if dipilih[i] and not dipilih[j]:
                    harga_baru = harga_total - hadiah[i]["harga"] + hadiah[j]["harga"]
                    skor_baru = skor_total - hitung_skor(hadiah[i], budget) + hitung_skor(hadiah[j], budget)
                    
                    # Melakukan pertukaran jika skornya naik dan budgetnya masih cukup
                    if harga_baru <= budget and skor_baru > skor_total:
                        dipilih[i] = False
                        dipilih[j] = True
                        harga_total = harga_baru
                        skor_total = skor_baru
                        ada_perbaikan = True

    durasi = (time.time() - start) * 1000
    return round(skor_total, 4), round(durasi, 2)