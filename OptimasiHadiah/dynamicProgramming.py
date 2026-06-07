# Nama File : dynamicProgramming.py
# Pembuat : Aswalila Adha Putri Telaumbanua - 24060124120014
# Kelas : C / Informatika 2024

import time
from Skor import hitung_skor

def jalankan_dp(hadiah, budget):
    jumlah_hadiah = len(hadiah)
    batas_budget = budget // 1000
    tabel_skor = [[0.0] * (batas_budget + 1) for baris in range(jumlah_hadiah + 1)]
    
    start = time.time()

    for i in range(1, jumlah_hadiah + 1):
        hadiah_saat_ini = hadiah[i - 1]
        berat = hadiah_saat_ini["harga"] // 1000
        nilai = hitung_skor(hadiah_saat_ini, budget)
        for kapasitas in range(batas_budget + 1):
            # default: tidak ambil hadiah ini
            tabel_skor[i][kapasitas] = tabel_skor[i - 1][kapasitas]
            # mengecek apakah hadiah ini masuk budget atau tidak
            if berat <= kapasitas:
                ambil = tabel_skor[i - 1][kapasitas - berat] + nilai
                if ambil > tabel_skor[i][kapasitas]:
                    tabel_skor[i][kapasitas] = ambil

    durasi = (time.time() - start) * 1000
    return round(tabel_skor[jumlah_hadiah][batas_budget], 4), round(durasi, 2)