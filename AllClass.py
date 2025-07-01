# === FILE: konsepoop.py ===

# Mengimpor modul-modul yang diperlukan.
from abc import ABC, abstractmethod  # Untuk membuat kelas abstrak (Abstraction).
import random  # Untuk menghasilkan angka acak (digunakan di checkout).
import time  # Untuk memberikan jeda waktu (digunakan di tracking).
import os  # Untuk berinteraksi dengan sistem operasi (mengecek file).


# === ABSTRACTION ===
# Mendefinisikan kelas abstrak 'Pengguna' sebagai blueprint dasar.
class Pengguna(ABC):
    # Metode constructor yang dijalankan saat objek Pengguna dibuat.
    def __init__(self, nama, email, nomer_hp):
        self._nama = nama  # Inisialisasi atribut nama (protected).
        self._email = email  # Inisialisasi atribut email (protected).
        self._nomer_hp = nomer_hp  # Inisialisasi atribut nomor HP (protected).

    # Mendefinisikan metode abstrak 'tampilkan_info'.
    @abstractmethod
    def tampilkan_info(self):
        pass


# === ENCAPSULATION & CLASS STRUCTURE ===
# Mendefinisikan kelas 'produk' untuk merepresentasikan produk di e-commerce.
class produk:
    # Atribut kelas (class attribute) untuk menyimpan semua instance produk yang dibuat.
    daftar_produk = []

    # Metode constructor yang dijalankan saat objek produk dibuat.
    def __init__(self, NamaProduk, harga, varian, kategori, kuantitasProduk, lokasiToko):
        self.__NamaProduk = NamaProduk  # Inisialisasi atribut nama produk (private).
        self.__harga = harga  # Inisialisasi atribut harga (private).
        self.__varian = varian  # Inisialisasi atribut varian (private).
        self.__kategori = kategori  # Inisialisasi atribut kategori (private).
        self.__kuantitas = kuantitasProduk  # Inisialisasi atribut kuantitas (private).
        self.__lokasi = lokasiToko  # Inisialisasi atribut lokasi toko (private).
        self.__ratings = []  # <<< TAMBAHKAN INI: Untuk menyimpan semua rating (contoh: [5, 4, 5])
        produk.daftar_produk.append(self)  # Menambahkan instance produk baru ke dalam 'daftar_produk'.

    # Metode 'getter' untuk mendapatkan nama produk (Encapsulation).
    def get_nama(self): return self.__NamaProduk
    # Metode 'getter' untuk mendapatkan harga produk (Encapsulation).
    def get_harga(self): return self.__harga
    # Metode 'getter' untuk mendapatkan varian produk (Encapsulation).
    def get_varian(self): return self.__varian
    # Metode 'getter' untuk mendapatkan kategori produk (Encapsulation).
    def get_kategori(self): return self.__kategori
    # Metode 'getter' untuk mendapatkan kuantitas produk (Encapsulation).
    def get_kuantitas(self): return self.__kuantitas
    # Metode 'getter' untuk mendapatkan lokasi toko (Encapsulation).
    def get_lokasi(self): return self.__lokasi

    # Metode untuk menambahkan rating baru.
    def tambah_rating(self, rating):
        # Validasi agar rating antara 1 dan 5
        if 1 <= rating <= 5:
            self.__ratings.append(rating)
            print(f"Terima kasih atas rating {rating} untuk produk {self.get_nama()}!")
        else:
            print("Rating harus antara 1 dan 5.")

    # Metode 'getter' untuk mendapatkan rata-rata rating.
    def get_rata_rata_rating(self):
        if not self.__ratings:
            return 0.0  # Jika belum ada rating, kembalikan 0.0
        # Menghitung rata-rata dan memformat menjadi 1 angka di belakang koma.
        return round(sum(self.__ratings) / len(self.__ratings), 1)

    # Metode untuk mengurangi kuantitas produk setelah dibeli.
    def kurangi_kuantitas(self, jumlah):
        # Memeriksa apakah jumlah yang diminta tidak melebihi stok.
        if jumlah <= self.__kuantitas:
            # Jika stok cukup, kurangi kuantitas.
            self.__kuantitas -= jumlah

    # Metode untuk menampilkan informasi satu produk dalam bentuk list.
    def tampilkan_info_produk(self):
        # Mengembalikan list berisi detail produk.
        return [
            self.__NamaProduk,
            f"Rp{self.__harga}",
            self.__varian,
            self.__kategori,
            str(self.__kuantitas),
            self.__lokasi
        ]

    # Metode kelas (class method) untuk menampilkan semua produk dalam format tabel.
    @classmethod
    def tampilkan_semua_produk(cls):
        # Mendefinisikan header tabel. (TAMBAHKAN "RATING")
        headers = ["No", "Nama Produk", "Harga", "Varian", "Kategori", "Stok", "Rating", "Lokasi"]
        print("\n" + "="*90) # Sesuaikan panjang garis
        # Update format string untuk header
        print("{:<4} {:<20} {:<10} {:<10} {:<12} {:<6} {:<8} {:<20}".format(*headers))
        print("="*90) # Sesuaikan panjang garis

        for i, p in enumerate(cls.daftar_produk, 1):
            # Mendapatkan data produk
            data_produk = p.tampilkan_info_produk()
            # Sisipkan data rating ke dalam list data
            data_produk.insert(5, str(p.get_rata_rata_rating())) # Sisipkan rating
            data = [str(i)] + data_produk

            # Update format string untuk data
            print("{:<4} {:<20} {:<10} {:<10} {:<12} {:<6} {:<8} {:<20}".format(*data))
        print("="*90) # Sesuaikan panjang garis


# === INHERITANCE ===
# Mendefinisikan kelas 'Pembeli' yang merupakan turunan dari kelas 'Pengguna'.
class Pembeli(Pengguna):
    # Metode constructor untuk kelas 'Pembeli'.
    def __init__(self, nama, email, nomer_hp, alamat):
        # Memanggil constructor dari kelas induk ('Pengguna') untuk inisialisasi atribut dasar.
        super().__init__(nama, email, nomer_hp)
        # Inisialisasi atribut khusus untuk Pembeli (alamat, keranjang, pesanan).
        self.__alamat = alamat  # Atribut alamat (private).
        self.__keranjang = []  # Atribut keranjang belanja (private).
        self.__pesanan_dikirim = []  # Atribut untuk pesanan yang sedang dikirim (private).
        self.__riwayat_pembelian = [] # <<< TAMBAHKAN INI

    # Implementasi konkret dari metode abstrak 'tampilkan_info' (Polymorphism).
    def tampilkan_info(self):
        # Mencetak informasi dasar dari pembeli.
        print(f"Pembeli: {self._nama}, Email: {self._email}, Alamat: {self.__alamat}")

    # Metode untuk menambahkan produk ke keranjang belanja.
    def tambah_keranjang(self, produk, jumlah):
        # Memeriksa apakah jumlah yang diminta melebihi stok produk.
        if jumlah > produk.get_kuantitas():
            # Jika tidak cukup, tampilkan pesan error.
            print("Stok tidak cukup!")
        else:
            # Jika cukup, tambahkan produk dan jumlahnya ke dalam list keranjang.
            self.__keranjang.append((produk, jumlah))
            # Tampilkan pesan konfirmasi.
            print(f"{produk.get_nama()} x{jumlah} ditambahkan ke keranjang.")

    # Metode untuk proses checkout.
    def checkout(self):
        # Memeriksa apakah keranjang kosong.
        if not self.__keranjang:
            # Jika ya, tampilkan pesan dan hentikan proses.
            print("Keranjang kosong!")
            return

        # Menampilkan judul bagian checkout.
        print("\n=== Checkout ===")
        # Inisialisasi total belanja.
        total = 0
        # Menampilkan detail belanja dari keranjang.
        print("\nDetail Belanja:")
        # Melakukan iterasi pada keranjang untuk menampilkan setiap item.
        for i, (p, jml) in enumerate(self.__keranjang, 1):
            # Menghitung subtotal untuk setiap item.
            subtotal = p.get_harga() * jml
            # Menambahkan subtotal ke total belanja.
            total += subtotal
            # Mencetak detail item.
            print(f"{i}. {p.get_nama()} x{jml} - Rp{subtotal}")

        # Mencetak total belanja keseluruhan.
        print(f"Total Belanja: Rp{total}")
        # Meminta konfirmasi dari pengguna untuk melanjutkan.
        konfirmasi = input("Lanjutkan checkout? (y/n): ")
        # Jika pengguna tidak mengetik 'y', batalkan checkout.
        if konfirmasi.lower() != 'y':
            print("Checkout dibatalkan.")
            return

        # Meminta input metode pembayaran.
        metode = input("Metode pembayaran (Transfer/Tunai): ")
        # Jika metode adalah 'transfer'.
        if metode.lower() == "transfer":
            # Membuat kode verifikasi acak 4 digit.
            kode = ''.join([str(random.randint(0, 9)) for _ in range(4)])
            # Memberikan instruksi pembayaran.
            print(f"\nSilakan transfer ke rekening XYZ123 sejumlah Rp{total}")
            print(f"Kode verifikasi: {kode}")
            # Loop untuk validasi kode verifikasi.
            while True:
                # Meminta input kode verifikasi.
                verifikasi = input("Masukkan kode verifikasi: ")
                # Jika kode benar, lanjutkan.
                if verifikasi == kode:
                    print("Pembayaran berhasil.")
                    break
                # Jika kode salah, minta input lagi.
                else:
                    print("Kode salah. Coba lagi.")
        # Jika metode adalah 'tunai'.
        elif metode.lower() == "tunai":
            # Menggunakan try-except untuk menangani input non-angka.
            try:
                # Meminta jumlah uang yang dibayarkan.
                bayar = int(input(f"Masukkan jumlah uang tunai (Rp): "))
                # Memeriksa apakah uang cukup.
                if bayar >= total:
                    # Jika cukup, tampilkan kembalian.
                    print(f"Pembayaran diterima. Kembalian: Rp{bayar - total}")
                else:
                    # Jika tidak cukup, batalkan checkout.
                    print("Uang tidak cukup. Checkout dibatalkan.")
                    return
            except ValueError:
                # Jika input bukan angka, batalkan.
                print("Input tidak valid.")
                return
        # Jika metode pembayaran tidak dikenal.
        else:
            print("Metode tidak dikenal. Checkout dibatalkan.")
            return

        # Loop untuk memproses setiap item setelah pembayaran berhasil.
        for p, j in self.__keranjang:
            # Mengurangi kuantitas produk yang terjual.
            p.kurangi_kuantitas(j)
            # Memindahkan item dari keranjang ke daftar pesanan dikirim.
            self.__pesanan_dikirim.append({"produk": p, "jumlah": j, "status": "Dalam Pengiriman"})
        # Mengosongkan keranjang belanja.
        self.__keranjang.clear()
        # Menampilkan pesan konfirmasi checkout berhasil.
        print("\nCheckout berhasil! Pesanan sedang diproses.")
    
    def lihat_riwayat_pembelian(self):
        print("\n=== Riwayat Pembelian ===")
        if not self.__riwayat_pembelian:
            print("Anda belum memiliki riwayat pembelian.")
            return

        for i, item in enumerate(self.__riwayat_pembelian, 1):
            produk = item['produk']
            jumlah = item['jumlah']
            # tanggal = item['tanggal_selesai']
            print(f"{i}. Produk: {produk.get_nama()} (x{jumlah})")
            # print(f"   Tanggal Selesai: {tanggal}")
        print("-" * 30)

    # Tambahkan metode untuk mendapatkan list pesanan yang sudah dikirim tapi belum diterima
    def get_pesanan_dikirim(self):
        return self.__pesanan_dikirim

    # Metode untuk melacak status pengiriman produk.
    def tracking_produk(self):
        # Memeriksa apakah ada pesanan yang sedang dikirim.
        if not self.__pesanan_dikirim:
            # Jika tidak ada, tampilkan pesan.
            print("Tidak ada produk yang dikirim.")
            return

        # Daftar status pengiriman.
        status_list = ["Dikemas", "Dikirim ke gudang", "Menuju alamat", "Sampai tujuan"]
        # Loop untuk mensimulasikan perubahan status.
        for status in status_list:
            # Menampilkan status saat ini.
            print(f"Status: {status}")
            # Mengupdate status pada setiap item pesanan.
            for x in self.__pesanan_dikirim:
                x['status'] = status
            # Memberi jeda 1 detik untuk simulasi.
            time.sleep(1)

    # Metode untuk mengonfirmasi penerimaan produk.
    def terima_produk(self):
        if not self.__pesanan_dikirim:
            print("Tidak ada pesanan untuk diterima.")
            return False # Kembalikan False jika tidak ada pesanan

        # Pindahkan semua item dari pesanan_dikirim ke riwayat_pembelian
        for item in self.__pesanan_dikirim:
            item['status'] = 'Selesai'
            # Tambahkan timestamp kapan pesanan selesai
            # item['tanggal_selesai'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.__riwayat_pembelian.append(item)

        print("Semua produk telah diterima dan dipindahkan ke riwayat pembelian.")
        self.__pesanan_dikirim.clear() # Kosongkan pesanan yang sedang dikirim
        return True # Kembalikan True jika berhasil

    # Metode untuk melihat isi keranjang belanja.
    def lihat_keranjang(self):
        # Memeriksa apakah keranjang kosong.
        if not self.__keranjang:
            # Jika ya, tampilkan pesan.
            print("Keranjang kosong.")
        else:
            # Jika ada isi, loop dan tampilkan setiap item.
            for i, (p, j) in enumerate(self.__keranjang, 1):
                # Mencetak detail item di keranjang.
                print(f"{i}. {p.get_nama()} x{j} - Rp{p.get_harga() * j}")


# === LOGIN SYSTEM & MULTIPLE INHERITANCE ===
# Mendefinisikan kelas abstrak 'Akun' untuk logika login.
class Akun(ABC):
    # Metode constructor untuk kelas Akun.
    def __init__(self, email, password):
        self._email = email  # Atribut email (protected).
        self.__password = password  # Atribut password (private).

    # Metode untuk memverifikasi password yang diinput.
    def verifikasi_password(self, password):
        # Mengembalikan True jika password cocok, False jika tidak.
        return self.__password == password

    # Mendefinisikan metode abstrak yang harus diimplementasikan oleh kelas turunan.
    @abstractmethod
    def tampilkan_info(self):
        pass

# Kelas 'AkunPembeli' mewarisi dari 'Akun' dan 'Pembeli' (Multiple Inheritance).
class AkunPembeli(Akun, Pembeli):
    # Metode constructor untuk AkunPembeli.
    def __init__(self, nama, email, nomer_hp, alamat, password):
        # Memanggil constructor dari kelas induk 'Akun'.
        Akun.__init__(self, email, password)
        # Memanggil constructor dari kelas induk 'Pembeli'.
        Pembeli.__init__(self, nama, email, nomer_hp, alamat)

    # Implementasi konkret dari metode 'tampilkan_info'.
    def tampilkan_info(self):
        # Memanggil metode 'tampilkan_info' dari kelas induknya ('Pembeli').
        super().tampilkan_info()


# Kelas 'ManajemenAkun' untuk mengelola semua akun pengguna.
class ManajemenAkun:
    # Atribut kelas untuk menyimpan semua objek akun.
    daftar_akun = []

    # Metode kelas untuk menambahkan akun baru.
    @classmethod
    def tambah_akun(cls, akun):
        # Menambahkan objek akun ke 'daftar_akun'.
        cls.daftar_akun.append(akun)
        # Menyimpan perubahan ke file teks.
        cls.simpan_akun_ke_file()

    # Metode kelas untuk proses login.
    @classmethod
    def login(cls, email, password):
        # Loop melalui setiap akun di 'daftar_akun'.
        for akun in cls.daftar_akun:
            # Memeriksa apakah email dan password cocok.
            if akun._email == email and akun.verifikasi_password(password):
                # Jika cocok, kembalikan objek akun tersebut.
                return akun
        # Jika tidak ada akun yang cocok, kembalikan None.
        return None

    # Metode kelas untuk menyimpan data akun ke file teks.
    @classmethod
    def simpan_akun_ke_file(cls, filename="akun.txt"):
        # Membuka file dengan mode 'write' (menimpa isi lama).
        with open(filename, "w") as file:
            # Loop melalui setiap akun.
            for akun in cls.daftar_akun:
                # Membuat string data yang dipisahkan koma.
                data = f"{akun._nama},{akun._email},{akun._nomer_hp},{akun._Pembeli__alamat},{akun._Akun__password}\n"
                # Menulis data ke file.
                file.write(data)

    # Metode kelas untuk memuat data akun dari file teks.
    @classmethod
    def muat_akun_dari_file(cls, filename="akun.txt"):
        # Memeriksa apakah file 'akun.txt' ada.
        if not os.path.exists(filename):
            # Jika tidak ada, hentikan proses.
            return
        # Membuka file dengan mode 'read'.
        with open(filename, "r") as file:
            # Loop melalui setiap baris di file.
            for baris in file:
                # Memecah baris menjadi beberapa bagian berdasarkan koma.
                nama, email, nomer_hp, alamat, password = baris.strip().split(",")
                # Membuat objek AkunPembeli dari data yang dibaca.
                akun = AkunPembeli(nama, email, nomer_hp, alamat, password)
                # Menambahkan objek akun ke 'daftar_akun'.
                cls.daftar_akun.append(akun)
