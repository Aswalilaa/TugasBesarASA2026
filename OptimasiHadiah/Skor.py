# Nama File : Skor.py
# Pembuat : Aswalila Adha Putri Telaumbanua - 24060124120014
# Kelas : C / Informatika 2024

def hitung_skor(hadiah, budget):
    p = hadiah["preferensi"]
    k = hadiah["kesan"]
    d = hadiah["kedekatan"]
    h = hadiah["harga"]
    return 0.30 * p + 0.30 * k + 0.30 * d + 0.10 * (1 - h / budget)