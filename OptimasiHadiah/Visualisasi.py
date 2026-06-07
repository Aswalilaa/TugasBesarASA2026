# Nama File : Visualisasi.py
# Pembuat : Aswalila Adha Putri Telaumbanua - 24060124120014
# Kelas : C / Informatika 2024

import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

def cetak_tabel(hasil):
    print("========== HASIL PERBANDINGAN ALGORITMA ==========")
    header = ["Skenario", "Algoritma", "Skor", "Waktu (ms)"]
    rows = []
    for h in hasil:
        rows.append([h["skenario"], "Backtracking", h["bt_skor"], h["bt_waktu"]])
        rows.append(["", "Dynamic Programming", h["dp_skor"], h["dp_waktu"]])
        rows.append(["", "Hill Climbing", h["hc_skor"], h["hc_waktu"]])
        rows.append(["-"*20, "-"*20, "-"*10, "-"*10])
    print(tabulate(rows, headers=header, tablefmt="grid"))

def buat_grafik(hasil):
    skenario = [h["skenario"] for h in hasil]
    bt_waktu = [h["bt_waktu"] for h in hasil]
    dp_waktu = [h["dp_waktu"] for h in hasil]
    hc_waktu = [h["hc_waktu"] for h in hasil]
    bt_skor = [h["bt_skor"] for h in hasil]
    dp_skor = [h["dp_skor"] for h in hasil]
    hc_skor = [h["hc_skor"] for h in hasil]

    x = list(range(len(skenario)))
    width = 0.25
    warna_bt = "#FF9AA2"
    warna_dp = "#A8D8EA"
    warna_hc = "#B5EAD7"

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    fig.patch.set_facecolor("#F8F9FA")
    fig.canvas.manager.set_window_title("Aswalila Adha Putri - Comparison Chart")

    # Grafik waktu eksekusi
    ax1.set_facecolor("#FFFFFF")
    ax1.plot(x, bt_waktu, marker="o", linewidth=2, markersize=7, label="Backtracking", color=warna_bt)
    ax1.plot(x, dp_waktu, marker="s", linewidth=2, markersize=7, label="Dynamic Programming", color=warna_dp)
    ax1.plot(x, hc_waktu, marker="^", linewidth=2, markersize=7, label="Hill Climbing", color=warna_hc)
    ax1.set_title("Perbandingan Waktu Eksekusi", fontsize=14, fontweight="bold", pad=15, color="#333133")
    ax1.set_xlabel("Skenario", fontsize=11)
    ax1.set_ylabel("Waktu (ms)", fontsize=11)
    ax1.set_xticks(x)
    ax1.set_xticklabels(skenario, rotation=30, ha="right", fontsize=9)
    ax1.legend(fontsize=9, loc="upper left")
    ax1.grid(True, linestyle="--", alpha=0.5)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    # Grafik perbandingan skor
    ax2.set_facecolor("#FFFFFF")
    bar1 = ax2.bar([i - width for i in x], bt_skor, width, label="Backtracking", color=warna_bt, alpha=0.85)
    bar2 = ax2.bar([i for i in x], dp_skor, width, label="Dynamic Programming", color=warna_dp, alpha=0.85)
    bar3 = ax2.bar([i + width for i in x], hc_skor, width, label="Hill Climbing", color=warna_hc, alpha=0.85)

    for bar in [bar1, bar2, bar3]:
        for rect in bar:
            tinggi = rect.get_height()
            ax2.annotate(f"{tinggi:.2f}", xy=(rect.get_x() + rect.get_width() / 2, tinggi), xytext=(0, 5), textcoords="offset points", ha="center", va="bottom", fontsize=8)

    ax2.set_title("Perbandingan Skor Algoritma", fontsize=14, fontweight="bold", pad=15, color="#333133")
    ax2.set_xlabel("Skenario", fontsize=11)
    ax2.set_ylabel("Skor Total", fontsize=11)
    ax2.set_xticks(x)
    ax2.set_xticklabels(skenario, rotation=30, ha="right", fontsize=9)
    ax2.legend(fontsize=9, loc="upper right")
    ax2.grid(True, linestyle="--", alpha=0.5, axis="y")
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    plt.suptitle("Hasil Perbandingan Algoritma pada Optimasi Pemilihan Hadiah", fontsize=13, fontweight="bold", y=0.92, fontfamily="DejaVu Sans", color="#0A0A0B")
    plt.tight_layout(rect=[0, 0, 1, 0.90])
    plt.savefig("hasil_perbandingan.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("\nGrafik disimpan sebagai 'hasil_perbandingan.png'")

def buat_radar_chart(hasil):
    kategori = ["Skor", "Kecepatan", "Skalabilitas"]
    N = len(kategori)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]

    warna_bt = "#FF9AA2"
    warna_dp = "#A8D8EA"
    warna_hc = "#B5EAD7"

    fig, axes = plt.subplots(1, len(hasil), figsize=(6 * len(hasil), 6), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor("#F8F9FA")
    fig.canvas.manager.set_window_title("Aswalila Adha Putri - Radar Chart")

    if len(hasil) == 1:
        axes = [axes]

    for idx, h in enumerate(hasil):
        ax = axes[idx]
        max_skor = max(h["bt_skor"], h["dp_skor"], h["hc_skor"])
        bt_nilai = min(h["bt_skor"] / max_skor, 1.0)
        dp_nilai = min(h["dp_skor"] / max_skor, 1.0)
        hc_nilai = min(h["hc_skor"] / max_skor, 1.0)

        max_waktu = max(h["bt_waktu"], h["dp_waktu"], h["hc_waktu"])
        bt_kecepatan = 1 - (h["bt_waktu"] / max_waktu) if max_waktu > 0 else 1
        dp_kecepatan = 1 - (h["dp_waktu"] / max_waktu) if max_waktu > 0 else 1
        hc_kecepatan = 1 - (h["hc_waktu"] / max_waktu) if max_waktu > 0 else 1

        # Skalabilitas ini sudah ditentukan berdasarkan karakteristik masing-masing algoritma
        bt_skalabilitas = 0.3
        dp_skalabilitas = 0.7
        hc_skalabilitas = 1.0

        data_bt = [bt_nilai, bt_kecepatan, bt_skalabilitas]
        data_dp = [dp_nilai, dp_kecepatan, dp_skalabilitas]
        data_hc = [hc_nilai, hc_kecepatan, hc_skalabilitas]

        data_bt += data_bt[:1]
        data_dp += data_dp[:1]
        data_hc += data_hc[:1]

        ax.plot(angles, data_bt, linewidth=2, color=warna_bt, label="Backtracking")
        ax.fill(angles, data_bt, alpha=0.25, color=warna_bt)
        ax.plot(angles, data_dp, linewidth=2, color=warna_dp, label="Dynamic Programming")
        ax.fill(angles, data_dp, alpha=0.25, color=warna_dp)
        ax.plot(angles, data_hc, linewidth=2, color=warna_hc, label="Hill Climbing")
        ax.fill(angles, data_hc, alpha=0.25, color=warna_hc)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(kategori, fontsize=10, fontweight="bold", color="#E576D3")
        ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
        ax.set_yticklabels(["0.2", "0.4", "0.6", "0.8", "1.0"], fontsize=7, color="grey")
        ax.set_ylim(0, 1)
        ax.set_title(h["skenario"], fontsize=13, fontweight="bold", pad=20)
        ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1), fontsize=8)
        ax.grid(color="grey", linestyle="--", linewidth=0.5, alpha=0.5)
        ax.set_facecolor("#FFFFFF")

    plt.suptitle("Radar Chart Perbandingan Algoritma pada Optimasi Pemilihan Hadiah", fontsize=13, fontweight="bold", y=0.92, fontfamily="DejaVu Sans", color="#0A0A0B")
    plt.tight_layout(rect=[0, 0, 1, 0.90])
    plt.savefig("radar_chart.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("\nRadar chart disimpan sebagai 'radar_chart.png'")