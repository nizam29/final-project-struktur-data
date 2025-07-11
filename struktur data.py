import csv
import os

DATA_FILE = 'keuangan.csv'

# Fungsi membaca data
def read_data():
    with open(DATA_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Fungsi menambahkan catatan keuangan
def tambah_catatan():
    tanggal = input("Tanggal (YYYY-MM-DD): ")
    tipe = input("Tipe (pemasukan/pengeluaran): ")
    jumlah = input("Jumlah (Rp): ")
    kategori = input("Kategori: ")
    deskripsi = input("Deskripsi: ")
    
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tanggal, tipe, jumlah, kategori, deskripsi])
    print("Data berhasil ditambahkan!")

# Fungsi menampilkan data
def tampilkan_data():
    data = read_data()
    for i, row in enumerate(data, start=1):
        print(f"{i}. {row['tanggal']} | {row['tipe']} | {row['jumlah']} | {row['kategori']} | {row['deskripsi']}")

# Fungsi menghitung total pemasukan dan pengeluaran
def laporan_total():
    data = read_data()
    total_pemasukan = sum(int(row['jumlah']) for row in data if row['tipe'] == 'pemasukan')
    total_pengeluaran = sum(int(row['jumlah']) for row in data if row['tipe'] == 'pengeluaran')
    print(f"\nTotal Pemasukan: Rp{total_pemasukan}")
    print(f"Total Pengeluaran: Rp{total_pengeluaran}")
    print(f"Saldo: Rp{total_pemasukan - total_pengeluaran}")

# Menu utama
def menu():
    while True:
        print("\n=== APLIKASI KEUANGAN PRIBADI ===")
        print("1. Tambah Catatan")
        print("2. Tampilkan Semua Catatan")
        print("3. Laporan Total")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tambah_catatan()
        elif pilihan == '2':
            tampilkan_data()
        elif pilihan == '3':
            laporan_total()
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid!")

# Pastikan file csv ada
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["tanggal", "tipe", "jumlah", "kategori", "deskripsi"])

menu()

