# === FILE: mainkonsepoop.py (VERSI PERBAIKAN) ===

# --- Blok 1: Impor Modul ---
from AllClass import produk, AkunPembeli, ManajemenAkun

# --- Blok 2: Inisialisasi Data Awal ---
# (Penting: Untuk persistensi data produk, bagian ini idealnya diganti
# dengan fungsi memuat data dari file, sama seperti akun)
produk("laptop Asus", 9000, "Abu", "Elektronik", 5, "Bandung")
produk("mouse Logitech", 150, "Hitam", "Aksesoris", 20, "Jakarta")
produk("monitor LG", 2000, "Putih", "Elektronik", 10, "Surabaya")

# --- Blok 3: Memuat Data Akun ---
ManajemenAkun.muat_akun_dari_file()

# --- Blok 4: Fungsi Registrasi (Tidak ada perubahan) ---
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
            print("Email sudah digunakan. Gagal registrasi.")
            return None

    akun_baru = AkunPembeli(nama, email, nomer_hp, alamat, password)
    ManajemenAkun.tambah_akun(akun_baru)
    print("Registrasi berhasil! Silakan login.")
    return akun_baru

# --- Blok 5 & 6: RESTRUKTURISASI LOOP UTAMA PROGRAM ---
while True:  # <<< INI ADALAH LOOP UTAMA YANG MENGONTROL SELURUH APLIKASI
    user = None
    # Loop untuk Login/Registrasi
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
                print(f"\nSelamat datang, {user._nama}!")
                # Jika login berhasil, loop 'while not user' akan berhenti
            else:
                print("Email atau password salah.\n")
        elif pilih_awal == "2":
            registrasi()
        elif pilih_awal == "3":
            print("Keluar dari aplikasi.")
            exit()  # <<< GUNAKAN exit() UNTUK MENGHENTIKAN PROGRAM SEPENUHNYA
        else:
            print("Pilihan tidak valid.")

    # Loop Aplikasi E-commerce (Hanya berjalan jika 'user' sudah login)
    while True:
        print("\n=== MENU E-COMMERCE (OOP) ===")
        print("1. Lihat Produk")
        print("2. Tambah ke Keranjang")
        print("3. Lihat Keranjang")
        print("4. Checkout")
        print("5. Tracking Produk")
        print("6. Terima Produk")
        print("7. Info Pembeli")
        print("8. Beri Rating Produk")
        print("9. Riwayat Pembelian")
        print("10. Logout")
        print("11. Keluar Aplikasi")

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
            user.terima_produk()
            
        elif pilih == "7":
            # (Logika untuk info pembeli, tidak ada perubahan)
            print("\n=== Info Pembeli ===")
            user.tampilkan_info()

        elif pilih == "8":
            # (Logika untuk beri rating, tidak ada perubahan)
            print("\n=== Beri Rating Produk ===")
            riwayat = getattr(user, '_Pembeli__riwayat_pembelian', [])
            if not riwayat:
                print("Anda harus menyelesaikan pembelian terlebih dahulu untuk memberi rating.")
            else:
                for i, item in enumerate(riwayat, 1):
                    print(f"{i}. {item['produk'].get_nama()}")
                try:
                    idx = int(input("Pilih nomor produk yang akan dirating: ")) - 1
                    if 0 <= idx < len(riwayat):
                        produk_dipilih = riwayat[idx]['produk']
                        rating = int(input(f"Masukkan rating (1-5) untuk {produk_dipilih.get_nama()}: "))
                        produk_dipilih.tambah_rating(rating)
                    else:
                        print("Nomor produk tidak valid.")
                except (ValueError, IndexError):
                    print("Input tidak valid.")

        elif pilih == "9":
            user.lihat_riwayat_pembelian()

        # --- PERBAIKAN LOGIKA DI SINI ---
        elif pilih == "10": # Logout
            print(f"Anda telah logout dari akun {user._nama}.")
            break  # <<< GUNAKAN 'break' untuk keluar dari loop aplikasi dan kembali ke loop login

        elif pilih == "11": # Keluar Aplikasi
            print("Terima kasih telah menggunakan aplikasi.")
            exit() # <<< GUNAKAN 'exit()' untuk menghentikan program sepenuhnya
            
        else:
            print("Menu tidak valid.")