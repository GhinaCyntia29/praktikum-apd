import os
os.system('cls' if os.name == 'nt' else 'clear')

# ===== Variabel Global =====
akun = {
    "admin": {"username": "admin", "password": "admin123", "role": "admin"},
    "pengguna": {"username": "pengguna", "password": "pengguna123", "role": "pengguna"}
}
reservasi = {}  
role = None  

# ===== Prosedur =====
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("tekan enter untuk melanjutkan...")

# ===== Fungsi Tanpa Parameter =====
def total_data_reservasi():
    return len(reservasi)

# ===== Fungsi Dengan Parameter =====
def cek_kamar_dipesan(tipe, tanggal):
    for data in reservasi.values():
        if data["Tipe_Kamar"] == tipe and data["Tanggal_Reservasi"] == tanggal:
            return True
    return False

def tambah_reservasi(nama, tipe, tanggal, durasi):
    reservasi[nama] = {
        "Tipe_Kamar": tipe,
        "Tanggal_Reservasi": tanggal,
        "Durasi": durasi
    }

# ========= LOGIN ADMIN REKURSIF DI SINI ✅ =========
def login_admin():
    clear()
    print("=== LOGIN ADMIN ===")
    username = input("masukkan username: ")
    password = input("masukkan password: ")

    if username not in akun or akun[username]["password"] != password:
        print("Username atau password salah!")
        pause()
        return login_admin()  # REKURSIF ❗

    if akun[username]["role"] != "admin":
        print("Anda bukan admin!")
        pause()
        return login_admin()  # REKURSIF ❗

    # Sukses login → Masuk menu admin
    while True:
        clear()
        print("=== MENU ADMIN ===")
        print("1. tambah data reservasi (create)")
        print("2. lihat data reservasi (read)")
        print("3. ubah data reservasi (update)")
        print("4. hapus data reservasi (delete)")
        print("5. cari data reservasi")
        print("6. filter berdasarkan tanggal")
        print("7. total data reservasi (rekursif)")
        print("8. logout")
        pilihan_admin = input("pilih menu (1/2/3/4/5/6/7/8): ")

        if pilihan_admin == "1":
            clear()
            print("=== TAMBAH DATA RESERVASI ===")
            nama = input("masukkan nama: ")
            tipe = input("masukkan tipe kamar (single/superior/deluxe): ")
            tanggal = input("masukkan tanggal reservasi (dd/mm/yyyy): ")
            durasi = input("masukkan durasi menginap (dalam hari): ")

            if cek_kamar_dipesan(tipe, tanggal):
                print("maaf, kamar sudah dibooking pada tanggal tersebut")
            else:
                tambah_reservasi(nama, tipe, tanggal, durasi)
                print("data reservasi berhasil ditambahkan")
            pause()

        elif pilihan_admin == "2":
            clear()
            print("=== DATA RESERVASI ===")
            if len(reservasi) == 0:
                print("belum ada data reservasi")
            else:
                nomor = 1
                for key, data in reservasi.items():
                    print(f"{nomor}. Nama: {key}, Tipe Kamar: {data['Tipe_Kamar']}, Tanggal: {data['Tanggal_Reservasi']}, Durasi: {data['Durasi']} hari")
                    nomor += 1
            pause()

        elif pilihan_admin == "3":
            clear()
            print("=== UBAH DATA RESERVASI ===")
            if len(reservasi) == 0:
                print("belum ada data reservasi")
            else:
                nomor = 1
                keys_list = list(reservasi.keys())
                for key in keys_list:
                    data = reservasi[key]
                    print(f"{nomor}. Nama: {key}, Tipe Kamar: {data['Tipe_Kamar']}, Tanggal: {data['Tanggal_Reservasi']}, Durasi: {data['Durasi']} hari")
                    nomor += 1

                index_input = input("masukkan nomor data yang ingin diubah: ")
                if index_input.isdigit():
                    index = int(index_input) - 1
                    if 0 <= index < len(keys_list):
                        key_terpilih = keys_list[index]
                        nama = input("masukkan nama baru (kosongkan jika tidak diubah): ")
                        kamar = input("masukkan tipe kamar baru (kosongkan jika tidak diubah): ")
                        tanggal = input("masukkan tanggal reservasi baru (kosongkan jika tidak diubah): ")
                        durasi = input("masukkan durasi menginap baru (kosongkan jika tidak diubah): ")
                        if nama:
                            reservasi[nama] = reservasi.pop(key_terpilih)
                            key_terpilih = nama
                        if kamar:
                            reservasi[key_terpilih]['Tipe_Kamar'] = kamar
                        if tanggal:
                            reservasi[key_terpilih]['Tanggal_Reservasi'] = tanggal
                        if durasi:
                            reservasi[key_terpilih]['Durasi'] = durasi
                        print("data reservasi berhasil diubah")
                    else:
                        print("nomor data tidak valid")
                else:
                    print("input harus angka!")
            pause()

        elif pilihan_admin == "4":
            clear()
            print("=== HAPUS DATA RESERVASI ===")
            if len(reservasi) == 0:
                print("belum ada data reservasi")
            else:
                nomor = 1
                keys_list = list(reservasi.keys())
                for key in keys_list:
                    data = reservasi[key]
                    print(f"{nomor}. Nama: {key}, Tipe Kamar: {data['Tipe_Kamar']}, Tanggal: {data['Tanggal_Reservasi']}, Durasi: {data['Durasi']} hari")
                    nomor += 1
                
                index_input = input("masukkan nomor data yang ingin dihapus: ")
                if index_input.isdigit():
                    index = int(index_input) - 1
                    if 0 <= index < len(keys_list):
                        del reservasi[keys_list[index]]
                        print("data reservasi berhasil dihapus")
                    else:
                        print("nomor data tidak valid")
                else:
                    print("input harus angka!")
            pause()

        elif pilihan_admin == "5":
            clear()
            print("=== CARI DATA RESERVASI ===")
            keyword = input("masukkan nama yang ingin dicari: ")
            hasil = []
            for key, data in reservasi.items():
                if keyword in key:
                    hasil.append((key, data))
            if len(hasil) == 0:
                print("data tidak ditemukan")
            else:
                for i, (key, data) in enumerate(hasil, 1):
                    print(f"{i}. Nama: {key}, Tipe Kamar: {data['Tipe_Kamar']}, Tanggal: {data['Tanggal_Reservasi']}, Durasi: {data['Durasi']} hari")
            pause()

        elif pilihan_admin == "6":
            clear()
            print("=== FILTER BERDASARKAN TANGGAL ===")
            tanggal_filter = input("masukkan tanggal yang ingin dicari (dd/mm/yyyy): ")
            hasil = []
            for key, data in reservasi.items():
                if data["Tanggal_Reservasi"] == tanggal_filter:
                    hasil.append((key, data))
            if len(hasil) == 0:
                print("tidak ada reservasi pada tanggal tersebut")
            else:
                for i, (key, data) in enumerate(hasil, 1):
                    print(f"{i}. Nama: {key}, Tipe Kamar: {data['Tipe_Kamar']}, Durasi: {data['Durasi']} hari")
            pause()

        elif pilihan_admin == "7":
            total = total_data_reservasi()
            print(f"Total reservasi: {total}")
            pause()

        elif pilihan_admin == "8":
            break
        else:
            pause()

# ================= PROGRAM UTAMA =================
while True:
    clear()
    print("=== SISTEM RESERVASI KAMAR HOTEL ===")
    print("1. login sebagai admin")
    print("2. login sebagai pengguna")
    print("3. register")
    print("4. keluar")
    pilih = input("silahkan pilih menu (1/2/3/4): ")

    if pilih == "1":
        login_admin()  # ✅ sekarang rekursif

    elif pilih == "2":
        # (LOGIN PENGGUNA PERSIS SAMA TIDAK AKU SENTUH)
        clear()
        print("=== LOGIN PENGGUNA ===")
        username = input("masukkan username: ")
        password = input("masukkan password: ")

        if username == "" or password == "":
            print("Username atau password tidak boleh kosong!")
            pause()
            continue

        if username in akun and akun[username]["password"] == password and akun[username]["role"] == "pengguna":
            print("login berhasil sebagai pengguna")
            pause()
            while True:
                clear()
                print("=== MENU PENGGUNA ===")
                print("1. buat reservasi baru")
                print("2. lihat reservasi saya")
                print("3. logout")
                pilihan_user = input("pilih menu (1/2/3): ")

                if pilihan_user == "1":
                    clear()
                    print("=== BUAT RESERVASI BARU ===")
                    nama = username
                    tipe = input("masukkan tipe kamar (single/superior/deluxe): ")
                    tanggal = input("masukkan tanggal reservasi (dd/mm/yyyy): ")
                    durasi = input("masukkan durasi menginap (hari): ")

                    if cek_kamar_dipesan(tipe, tanggal):
                        print("maaf, kamar sudah dibooking pada tanggal tersebut")
                    else:
                        tambah_reservasi(nama, tipe, tanggal, durasi)
                        print("reservasi berhasil dibuat")
                    pause()

                elif pilihan_user == "2":
                    clear()
                    print(f"=== RESERVASI {username} ===")
                    if username in reservasi:
                        data = reservasi[username]
                        print(f"Nama: {username}")
                        print(f"Tipe Kamar: {data['Tipe_Kamar']}")
                        print(f"Tanggal: {data['Tanggal_Reservasi']}")
                        print(f"Durasi: {data['Durasi']} hari")
                    else:
                        print("belum ada reservasi")
                    pause()

                elif pilihan_user == "3":
                    break
                else:
                    print("pilihan tidak valid")
                    pause()
        else:
            print("login gagal!")
            pause()

    elif pilih == "3":
        clear()
        print("=== REGISTER ===")
        username = input("masukkan username baru: ")
        if username in akun:
            print("username sudah ada!")
        else:
            password = input("masukkan password baru: ")
            akun[username] = {"username": username, "password": password, "role": "pengguna"}
            print("registrasi berhasil")
        pause()

    elif pilih == "4":
        print("Terima kasih telah menggunakan sistem reservasi!")
        break

    else:
        print("pilihan tidak valid! masukkan 1/2/3/4")
        pause()