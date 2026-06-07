# Nama File : Backtracking.py
# Pembuat : Aswalila Adha Putri Telaumbanua - 24060124120014
# Kelas : C / Informatika 2024

import time
from Skor import hitung_skor

def cariBacktracking(hadiah, budget, index, skor_saat_ini, harga_saat_ini, terbaik):
    if index == len(hadiah):
        if skor_saat_ini > terbaik["skor"]:
            terbaik["skor"] = skor_saat_ini
        return
    h = hadiah[index]
    # mencoba mengambil hadiah ini kalo budgetnya masih cukup
    if harga_saat_ini + h["harga"] <= budget:
        cariBacktracking(hadiah, budget, index + 1, skor_saat_ini + hitung_skor(h, budget), harga_saat_ini + h["harga"], terbaik)

    # jika tidak mengambil, maka lanjut ke hadiah berikutnya
    cariBacktracking(hadiah, budget, index + 1, skor_saat_ini, harga_saat_ini, terbaik)

def jalankan_backtracking(hadiah, budget):
    terbaik = {"skor": 0}
    start = time.time()
    cariBacktracking(hadiah, budget, 0, 0, 0, terbaik)
    durasi = (time.time() - start) * 1000
    return round(terbaik["skor"], 4), round(durasi, 2)