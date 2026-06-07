# Nama File : Main.py
# Pembuat : Aswalila Adha Putri Telaumbanua - 24060124120014
# Kelas : C / Informatika 2024

from Hadiah import input_hadiah, input_budget, input_jumlah_hadiah
from Backtracking import jalankan_backtracking
from dynamicProgramming import jalankan_dp
from hillClimbing import jalankan_hill_climbing
from Visualisasi import cetak_tabel, buat_grafik, buat_radar_chart

def main():
    print("========= OPTIMASI PEMILIHAN HADIAH ULANG TAHUN =========")
    hasil = []
    skenario_ke = 1
    lanjut = True

    while lanjut:
        print(f"\n~ SKENARIO {skenario_ke} ~")
        n = input_jumlah_hadiah()
        hadiah = input_hadiah(n)
        budget = input_budget()
        print("\nMenjalankan ketiga algoritma...")

        bt_skor, bt_waktu = jalankan_backtracking(hadiah, budget)
        dp_skor, dp_waktu = jalankan_dp(hadiah, budget)
        hc_skor, hc_waktu = jalankan_hill_climbing(hadiah, budget)

        hasil.append({
            "skenario": f"Skenario {skenario_ke}", "bt_skor": bt_skor, "bt_waktu": bt_waktu, "dp_skor": dp_skor, "dp_waktu": dp_waktu, "hc_skor": hc_skor, "hc_waktu": hc_waktu
        })

        print(f"\nHasil Skenario {skenario_ke}:")
        print(f"Backtracking        -> Skor: {bt_skor} | Waktu: {bt_waktu} ms")
        print(f"Dynamic Programming -> Skor: {dp_skor} | Waktu: {dp_waktu} ms")
        print(f"Hill Climbing       -> Skor: {hc_skor} | Waktu: {hc_waktu} ms")

        tambah = input("\nMau tambah skenario lagi? (y/n): ").strip().lower()
        if tambah == "y":
            skenario_ke += 1 
        else:
            lanjut = False

    cetak_tabel(hasil)
    buat_grafik(hasil)
    buat_radar_chart(hasil)

if __name__ == "__main__":
    main()