class AlatTulis:
    def __init__(self):
        self.nama = ""
        self.stok = 0
        self.harga_satuan = 0
        self.harga = 0

    # Setter untuk memasukkan data
    def set_data(self, nama, stok, harga_satuan):
        self.nama = nama
        self.stok = stok
        self.harga_satuan = harga_satuan
        self.harga = stok * harga_satuan

    # Getter untuk menampilkan data
    def get_data(self):
        print(f"Nama: {self.nama}")
        print(f"Stok Tersisa: {self.stok}")
        print(f"Harga Satuan: Rp {self.harga_satuan}")
        print(f"Total Harga: Rp {self.harga}")

    # Setter dan Getter untuk total harga
    def set_total_harga(self, stok_terjual):
        if stok_terjual > self.stok:
            print("Stok tidak mencukupi!")
        else:
            self.stok -= stok_terjual
            total_harga = stok_terjual * self.harga_satuan
            print(f"Transaksi berhasil! Total penjualan: Rp {total_harga}")

# Objek untuk setiap alat tulis
bolpoin = AlatTulis()
pensil = AlatTulis()
penghapus = AlatTulis()

# Memasukkan data masing-masing alat tulis
bolpoin.set_data("Bolpoin", 10, 2000)
pensil.set_data("Pensil", 10, 1000)
penghapus.set_data("Penghapus", 10, 500)

# Menampilkan data
print("TOKO MULYONO BERKAH")
print("Data Barang:")
bolpoin.get_data()
pensil.get_data()
penghapus.get_data()

# Contoh transaksi penjualan
print("\nTransaksi Penjualan:")
bolpoin.set_total_harga(int(input("Masukkan jumlah bolpoin yang terjual: ")))
pensil.set_total_harga(int(input("Masukkan jumlah pensil yang terjual: ")))
penghapus.set_total_harga(int(input("Masukkan jumlah penghapus yang terjual: ")))

# Menampilkan data setelah transaksi
print("\nData Barang Setelah Transaksi:")
bolpoin.get_data()
pensil.get_data()
penghapus.get_data()