# === FILE: konsepoop.py ===
from abc import ABC, abstractmethod
import random
import time
import os

# === ABSTRACTION ===
class Pengguna(ABC):
    def __init__(self, nama, email, nomer_hp):
        self._nama = nama
        self._email = email
        self._nomer_hp = nomer_hp

    @abstractmethod
    def tampilkan_info(self):
        pass

# === ENCAPSULATION + POLYMORPHISM ===
class produk:
    daftar_produk = []

    def __init__(self, NamaProduk, harga, varian, kategori, kuantitasProduk, lokasiToko):
        self.__NamaProduk = NamaProduk
        self.__harga = harga
        self.__varian = varian
        self.__kategori = kategori
        self.__kuantitas = kuantitasProduk
        self.__lokasi = lokasiToko
        produk.daftar_produk.append(self)

    def get_nama(self): return self.__NamaProduk
    def get_harga(self): return self.__harga
    def get_varian(self): return self.__varian
    def get_kategori(self): return self.__kategori
    def get_kuantitas(self): return self.__kuantitas
    def get_lokasi(self): return self.__lokasi

    def kurangi_kuantitas(self, jumlah):
        if jumlah <= self.__kuantitas:
            self.__kuantitas -= jumlah

    def tampilkan_info_produk(self):
        return [
            self.__NamaProduk,
            f"Rp{self.__harga}",
            self.__varian,
            self.__kategori,
            str(self.__kuantitas),
            self.__lokasi
        ]

    @classmethod
    def tampilkan_semua_produk(cls):
        headers = ["No", "Nama Produk", "Harga", "Varian", "Kategori", "Stok", "Lokasi"]
        print("\n" + "="*80)
        print("{:<4} {:<20} {:<10} {:<10} {:<12} {:<6} {:<20}".format(*headers))
        print("="*80)
        for i, p in enumerate(cls.daftar_produk, 1):
            data = [str(i)] + p.tampilkan_info_produk()
            print("{:<4} {:<20} {:<10} {:<10} {:<12} {:<6} {:<20}".format(*data))
        print("="*80)

# === INHERITANCE ===
class Pembeli(Pengguna):
    def __init__(self, nama, email, nomer_hp, alamat):
        super().__init__(nama, email, nomer_hp)
        self.__alamat = alamat
        self.__keranjang = []
        self.__pesanan_dikirim = []

    def tampilkan_info(self):
        print(f"Pembeli: {self._nama}, Email: {self._email}, Alamat: {self.__alamat}")

    def tambah_keranjang(self, produk, jumlah):
        if jumlah > produk.get_kuantitas():
            print("Stok tidak cukup!")
        else:
            self.__keranjang.append((produk, jumlah))
            print(f"{produk.get_nama()} x{jumlah} ditambahkan ke keranjang.")

    def checkout(self):
        if not self.__keranjang:
            print("Keranjang kosong!")
            return

        print("\n=== Checkout ===")
        total = 0
        print("\nDetail Belanja:")
        for i, (p, jml) in enumerate(self.__keranjang, 1):
            subtotal = p.get_harga() * jml
            total += subtotal
            print(f"{i}. {p.get_nama()} x{jml} - Rp{subtotal}")

        print(f"Total Belanja: Rp{total}")
        konfirmasi = input("Lanjutkan checkout? (y/n): ")
        if konfirmasi.lower() != 'y':
            print("Checkout dibatalkan.")
            return

        metode = input("Metode pembayaran (Transfer/Tunai): ")
        if metode.lower() == "transfer":
            kode = ''.join([str(random.randint(0, 9)) for _ in range(4)])
            print(f"\nSilakan transfer ke rekening XYZ123 sejumlah Rp{total}")
            print(f"Kode verifikasi: {kode}")
            while True:
                verifikasi = input("Masukkan kode verifikasi: ")
                if verifikasi == kode:
                    print("Pembayaran berhasil.")
                    break
                else:
                    print("Kode salah. Coba lagi.")
        elif metode.lower() == "tunai":
            try:
                bayar = int(input(f"Masukkan jumlah uang tunai (Rp): "))
                if bayar >= total:
                    print(f"Pembayaran diterima. Kembalian: Rp{bayar - total}")
                else:
                    print("Uang tidak cukup. Checkout dibatalkan.")
                    return
            except ValueError:
                print("Input tidak valid.")
                return
        else:
            print("Metode tidak dikenal. Checkout dibatalkan.")
            return

        for p, j in self.__keranjang:
            p.kurangi_kuantitas(j)
            self.__pesanan_dikirim.append({"produk": p, "jumlah": j, "status": "Dalam Pengiriman"})
        self.__keranjang.clear()
        print("\nCheckout berhasil! Pesanan sedang diproses.")

    def tracking_produk(self):
        if not self.__pesanan_dikirim:
            print("Tidak ada produk yang dikirim.")
            return

        status_list = ["Dikemas", "Dikirim ke gudang", "Menuju alamat", "Sampai tujuan"]
        for status in status_list:
            print(f"Status: {status}")
            for x in self.__pesanan_dikirim:
                x['status'] = status
            time.sleep(1)

    def terima_produk(self):
        for item in self.__pesanan_dikirim:
            item['status'] = f"Tiba di alamat {self.__alamat}"
            print("Produk diterima.")
        self.__pesanan_dikirim.clear()

    def lihat_keranjang(self):
        if not self.__keranjang:
            print("Keranjang kosong.")
        else:
            for i, (p, j) in enumerate(self.__keranjang, 1):
                print(f"{i}. {p.get_nama()} x{j} - Rp{p.get_harga() * j}")

# === LOGIN SYSTEM ===
class Akun(ABC):
    def __init__(self, email, password):
        self._email = email
        self.__password = password

    def verifikasi_password(self, password):
        return self.__password == password

    @abstractmethod
    def tampilkan_info(self):
        pass

class AkunPembeli(Akun, Pembeli):
    def __init__(self, nama, email, nomer_hp, alamat, password):
        Akun.__init__(self, email, password)
        Pembeli.__init__(self, nama, email, nomer_hp, alamat)

    def tampilkan_info(self):
        super().tampilkan_info()

class ManajemenAkun:
    daftar_akun = []

    @classmethod
    def tambah_akun(cls, akun):
        cls.daftar_akun.append(akun)
        cls.simpan_akun_ke_file()

    @classmethod
    def login(cls, email, password):
        for akun in cls.daftar_akun:
            if akun._email == email and akun.verifikasi_password(password):
                return akun
        return None

    @classmethod
    def simpan_akun_ke_file(cls, filename="akun.txt"):
        with open(filename, "w") as file:
            for akun in cls.daftar_akun:
                data = f"{akun._nama},{akun._email},{akun._nomer_hp},{akun._Pembeli__alamat},{akun._Akun__password}\n"
                file.write(data)

    @classmethod
    def muat_akun_dari_file(cls, filename="akun.txt"):
        if not os.path.exists(filename):
            return
        with open(filename, "r") as file:
            for baris in file:
                nama, email, nomer_hp, alamat, password = baris.strip().split(",")
                akun = AkunPembeli(nama, email, nomer_hp, alamat, password)
                cls.daftar_akun.append(akun)