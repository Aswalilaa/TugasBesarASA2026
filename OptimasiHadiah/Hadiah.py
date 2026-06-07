# Nama File : Hadiah.py
# Pembuat : Aswalila Adha Putri Telaumbanua - 24060124120014
# Kelas : C / Informatika 2024

def input_hadiah(n):
    hadiah = []
    print(f"\nMasukkan data {n} hadiah:")
    for i in range(n):
        print(f"\nHadiah ke-{i+1}:")
        nama = input("Nama hadiah : ")
        harga = int(input("Harga(Rp) : ").replace(".", "").replace(",", ""))
        preferensi = float(input("Preferensi (1-5) : "))
        kesan = float(input("Nilai kesan (1-5) : "))
        kedekatan = float(input("Kedekatan (1-5) : "))
        hadiah.append({
            "nama": nama,
            "harga": harga, 
            "preferensi": preferensi / 5,
            "kesan": kesan / 5,
            "kedekatan": kedekatan / 5
        }) 
    return hadiah

def input_budget():
    return int(input("\nMasukkan budget(Rp): ").replace(".", "").replace(",", ""))

def input_jumlah_hadiah():
    return int(input("Jumlah kandidat hadiah:"))