# Nama File : MainTest.py
# Pembuat : Aswalila Adha Putri Telaumbanua - 24060124120014
# Kelas : C / Informatika 2024

import random
from Backtracking import jalankan_backtracking
from dynamicProgramming import jalankan_dp
from hillClimbing import jalankan_hill_climbing
from Visualisasi import cetak_tabel, buat_grafik, buat_radar_chart

# fungsi buat generate hadiah random
def buat_data_hadiah(jumlah, budget):
    daftar = []
    for i in range(jumlah):
        h = random.randint(20000, budget // 2)
        daftar.append({
            "nama": f"Hadiah{i+1}", "harga": h, "preferensi": round(random.uniform(0, 1), 2), "kesan": round(random.uniform(0, 1), 2), "kedekatan": round(random.uniform(0, 1), 2)
        })
    return daftar

semua_hasil = []
print("========= PENGUJIAN OTOMATIS =========\n")

# Skenario 1
data1 = buat_data_hadiah(50, 500000)
skor_bt1, waktu_bt1 = jalankan_backtracking(data1, 500000)
skor_dp1, waktu_dp1 = jalankan_dp(data1, 500000)
skor_hc1, waktu_hc1 = jalankan_hill_climbing(data1, 500000)
print("Skenario: Besar (n=50) - Budget Rp500.000")
print(f"Backtracking        -> Skor: {skor_bt1} | Waktu: {waktu_bt1} ms")
print(f"Dynamic Programming -> Skor: {skor_dp1} | Waktu: {waktu_dp1} ms")
print(f"Hill Climbing       -> Skor: {skor_hc1} | Waktu: {waktu_hc1} ms")
print()
semua_hasil.append({"skenario": "Besar (n=50) - Budget Rp500.000", "bt_skor": skor_bt1, "bt_waktu": waktu_bt1, "dp_skor": skor_dp1, "dp_waktu": waktu_dp1, "hc_skor": skor_hc1, "hc_waktu": waktu_hc1})

# Skenario 2
data2 = buat_data_hadiah(50, 2000000)
skor_bt2, waktu_bt2 = jalankan_backtracking(data2, 2000000)
skor_dp2, waktu_dp2 = jalankan_dp(data2, 2000000)
skor_hc2, waktu_hc2 = jalankan_hill_climbing(data2, 2000000)
print("Skenario: Besar (n=50) - Budget Rp2.000.000")
print(f"Backtracking        -> Skor: {skor_bt2} | Waktu: {waktu_bt2} ms")
print(f"Dynamic Programming -> Skor: {skor_dp2} | Waktu: {waktu_dp2} ms")
print(f"Hill Climbing       -> Skor: {skor_hc2} | Waktu: {waktu_hc2} ms")
print()
semua_hasil.append({"skenario": "Besar (n=50) - Budget Rp2.000.000", "bt_skor": skor_bt2, "bt_waktu": waktu_bt2, "dp_skor": skor_dp2, "dp_waktu": waktu_dp2, "hc_skor": skor_hc2, "hc_waktu": waktu_hc2})

# Skenario 3
data3 = buat_data_hadiah(20, 500000)
skor_bt3, waktu_bt3 = jalankan_backtracking(data3, 500000)
skor_dp3, waktu_dp3 = jalankan_dp(data3, 500000)
skor_hc3, waktu_hc3 = jalankan_hill_climbing(data3, 500000)
print("Skenario: Sedang (n=20) - Budget Rp500.000")
print(f"Backtracking        -> Skor: {skor_bt3} | Waktu: {waktu_bt3} ms")
print(f"Dynamic Programming -> Skor: {skor_dp3} | Waktu: {waktu_dp3} ms")
print(f"Hill Climbing       -> Skor: {skor_hc3} | Waktu: {waktu_hc3} ms")
print()
semua_hasil.append({"skenario": "Sedang (n=20) - Budget Rp500.000", "bt_skor": skor_bt3, "bt_waktu": waktu_bt3, "dp_skor": skor_dp3, "dp_waktu": waktu_dp3, "hc_skor": skor_hc3, "hc_waktu": waktu_hc3})

# Skenario 4
data4 = buat_data_hadiah(20, 2000000)
skor_bt4, waktu_bt4 = jalankan_backtracking(data4, 2000000)
skor_dp4, waktu_dp4 = jalankan_dp(data4, 2000000)
skor_hc4, waktu_hc4 = jalankan_hill_climbing(data4, 2000000)
print("Skenario: Sedang (n=20) - Budget Rp2.000.000")
print(f"Backtracking        -> Skor: {skor_bt4} | Waktu: {waktu_bt4} ms")
print(f"Dynamic Programming -> Skor: {skor_dp4} | Waktu: {waktu_dp4} ms")
print(f"Hill Climbing       -> Skor: {skor_hc4} | Waktu: {waktu_hc4} ms")
print()
semua_hasil.append({"skenario": "Sedang (n=20) - Budget Rp2.000.000", "bt_skor": skor_bt4, "bt_waktu": waktu_bt4, "dp_skor": skor_dp4, "dp_waktu": waktu_dp4, "hc_skor": skor_hc4, "hc_waktu": waktu_hc4})

cetak_tabel(semua_hasil)
buat_grafik(semua_hasil)
buat_radar_chart(semua_hasil)