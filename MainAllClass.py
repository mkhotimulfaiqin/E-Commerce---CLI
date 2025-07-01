# === FILE: mainkonsepoop.py ===
from AllClass import produk, AkunPembeli, ManajemenAkun

# Tambah Produk Awal
produk("laptop Asus", 9000, "Abu", "Elektronik", 5, "Bandung")
produk("mouse Logitech", 150, "Hitam", "Aksesoris", 20, "Jakarta")
produk("monitor LG", 2000, "Putih", "Elektronik", 10, "Surabaya")

# Muat akun dari file saat program dijalankan
ManajemenAkun.muat_akun_dari_file()

def registrasi():
    print("\n=== Registrasi Akun Pembeli ===")
    nama = input("Nama lengkap     : ")
    email = input("Email            : ")
    nomer_hp = input("Nomor HP         : ")
    alamat = input("Alamat           : ")
    password = input("Password         : ")
    ulangi = input("Ulangi password  : ")

    if password != ulangi:
        print("Password tidak cocok. Gagal registrasi.")
        return None

    for akun in ManajemenAkun.daftar_akun:
        if akun._email == email:
            print("Email sudah digunakan. Silahkan Login Menggunakan akun email yang sudah terdaftar.")
            return None

    akun_baru = AkunPembeli(nama, email, nomer_hp, alamat, password)
    ManajemenAkun.tambah_akun(akun_baru)
    print("Registrasi berhasil! Silakan login.")
    return akun_baru

# Menu awal: Login atau Registrasi
user = None
while not user:
    print("\n=== SELAMAT DATANG DI APLIKASI E-COMMERCE ===")
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar")

    pilih_awal = input("Pilih menu: ")

    if pilih_awal == "1":
        email = input("Email    : ")
        password = input("Password : ")
        user = ManajemenAkun.login(email, password)
        if user:
            print(f"Selamat datang, {user._nama}!")
        else:
            print("Email atau password salah.\n")
    elif pilih_awal == "2":
        registrasi()
    elif pilih_awal == "3":
        print("Keluar dari aplikasi.")
        exit()
    else:
        print("Pilihan tidak valid.")

# === MENU UTAMA ===
while True:
    print("\n=== MENU E-COMMERCE (OOP) ===")
    print("1. Lihat Produk")
    print("2. Tambah ke Keranjang")
    print("3. Lihat Keranjang")
    print("4. Checkout")
    print("5. Tracking Produk")
    print("6. Terima Produk")
    print("7. Info Pembeli")
    print("8. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        produk.tampilkan_semua_produk()
    elif pilih == "2":
        try:
            idx = int(input("Nomor produk: ")) - 1
            jumlah = int(input("Jumlah beli: "))
            if 0 <= idx < len(produk.daftar_produk):
                user.tambah_keranjang(produk.daftar_produk[idx], jumlah)
            else:
                print("Produk tidak ditemukan.")
        except ValueError:
            print("Input harus angka.")
    elif pilih == "3":
        user.lihat_keranjang()
    elif pilih == "4":
        user.checkout()
    elif pilih == "5":
        user.tracking_produk()
    elif pilih == "6":
        for item in user._Pembeli__pesanan_dikirim:
            produk_diterima = item['produk'].get_nama()
            alamat = user._Pembeli__alamat
            nama = user._nama
            print(f"Pesanan '{produk_diterima}' telah sampai di tujuan ({alamat}) dan diterima oleh {nama}.")
        user.terima_produk()
    elif pilih == "7":
        print("\n=== Info Pembeli ===")
        user.tampilkan_info()

        pesanan = getattr(user, '_Pembeli__pesanan_dikirim', [])
        keranjang = getattr(user, '_Pembeli__keranjang', [])

        if pesanan:
            print("\nStatus: Telah melakukan checkout")
            print(f"Nama pengguna: {user._nama}")
            print("Produk yang dibeli:")
            for item in pesanan:
                p = item['produk']
                print(f"- {p.get_nama()} x{item['jumlah']} ({item['status']})")
        elif keranjang:
            print("\nStatus: Sedang menyiapkan checkout")
            print("Keranjang berisi:")
            for p, j in keranjang:
                print(f"- {p.get_nama()} x{j} - Rp{p.get_harga() * j}")
        else:
            print("\nStatus: Belum melakukan pembelian.")
            print("Detail lengkap pengguna:")
            print(f"Nama     : {user._nama}")
            print(f"Email    : {user._email}")
            print(f"No. HP   : {user._nomer_hp}")
            print(f"Alamat   : {user._Pembeli__alamat}")
    elif pilih == "8":
        print("Terima kasih telah menggunakan aplikasi.")
        break
    else:
        print("Menu tidak valid.")