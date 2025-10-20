import os
os.system('cls' if os.name == 'nt' else 'clear')

# Data akun & reservasi
akun = {
    "admin": {"username": "admin", "password": "admin123", "role": "admin"},
    "pengguna": {"username": "pengguna", "password": "pengguna123", "role": "pengguna"}
}
reservasi = {}  # key = nama pemesan, value = dict data reservasi

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SISTEM RESERVASI KAMAR HOTEL ===")
    print("1. login sebagai admin")
    print("2. login sebagai pengguna")
    print("3. register")
    print("4. keluar")
    pilih = input("silahkan pilih menu (1/2/3/4): ")

    # LOGIN ADMIN
    if pilih == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN ADMIN ===")
        username = input("masukkan username: ")
        password = input("masukkan password: ")
        if username in akun and akun[username]["password"] == password:
            role = akun[username]["role"]
        else:
            print("Username atau password salah!")
            input("Tekan ENTER untuk kembali ke menu awal...")
            continue
        if role == "admin":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== MENU ADMIN ===")
                print("1. tambah data reservasi (create)")
                print("2. lihat data reservasi (read)")
                print("3. ubah data reservasi (update)")
                print("4. hapus data reservasi (delete)")
                print("5. cari data reservasi")
                print("6. filter berdasarkan tanggal")
                print("7. logout")
                pilihan_admin = input("pilih menu (1/2/3/4/5/6/7): ")

                # CREATE
                if pilihan_admin == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== TAMBAH DATA RESERVASI ===")
                    nama = input("masukkan nama: ")
                    tipe = input("masukkan tipe kamar (single/superior/deluxe): ")
                    tanggal = input("masukkan tanggal reservasi (dd/mm/yyyy): ")
                    durasi = input("masukkan durasi menginap (dalam hari): ")

                    # Cek kamar sudah dibooking
                    sudah_dibooking = False
                    for data in reservasi.values():
                        if data["Tipe_Kamar"] == tipe and data["Tanggal_Reservasi"] == tanggal:
                            sudah_dibooking = True
                            break

                    if sudah_dibooking:
                        print("maaf, kamar sudah dibooking pada tanggal tersebut")
                    else:
                        reservasi[nama] = {
                            "Tipe_Kamar": tipe,
                            "Tanggal_Reservasi": tanggal,
                            "Durasi": durasi
                        }
                        print("data reservasi berhasil ditambahkan")
                    input("tekan enter untuk melanjutkan...")

                # READ
                elif pilihan_admin == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== DATA RESERVASI ===")
                    if len(reservasi) == 0:
                        print("belum ada data reservasi")
                    else:
                        nomor = 1
                        for key, data in reservasi.items():
                            print(f"{nomor}. Nama: {key}, Tipe Kamar: {data['Tipe_Kamar']}, Tanggal: {data['Tanggal_Reservasi']}, Durasi: {data['Durasi']} hari")
                            nomor += 1
                    input("tekan enter untuk melanjutkan...")

                # UPDATE
                elif pilihan_admin == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
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
                                    reservasi[key_terpilih]['Nama'] = nama
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
                        input("tekan enter untuk melanjutkan...")

                # DELETE
                elif pilihan_admin == "4":
                    os.system('cls' if os.name == 'nt' else 'clear')
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
                    input("tekan enter untuk melanjutkan...")
                # CARI DATA RESERVASI (MENU ADMIN 5)
                elif pilihan_admin == "5":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== CARI DATA RESERVASI ===")
                    keyword = input("masukkan nama yang ingin dicari: ")
                    hasil = []
                    for key, data in reservasi.items():
                        if keyword in key:  # langsung case-sensitive
                            hasil.append((key, data))
                    if len(hasil) == 0:
                        print("data tidak ditemukan")
                    else:
                        for i, (key, data) in enumerate(hasil, 1):
                            print(f"{i}. Nama: {key}, Tipe Kamar: {data['Tipe_Kamar']}, Tanggal: {data['Tanggal_Reservasi']}, Durasi: {data['Durasi']} hari")
                    input("tekan enter untuk melanjutkan...")

                # FILTER BERDASARKAN TANGGAL (MENU ADMIN 6)
                elif pilihan_admin == "6":
                    os.system('cls' if os.name == 'nt' else 'clear')
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
                    input("tekan enter untuk melanjutkan...")

    # LOGIN PENGGUNA
    elif pilih == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN PENGGUNA ===")
        username = input("masukkan username: ")
        password = input("masukkan password: ")

        # ERROR HANDLING PENGGUNA
        if username == "" or password == "":
            print("Username atau password tidak boleh kosong!")
            input("tekan enter untuk kembali...")
            continue

        if username in akun and akun[username]["password"] == password and akun[username]["role"] == "pengguna":
            print("login berhasil sebagai pengguna")
            input("tekan enter untuk melanjutkan...")

            # MENU PENGGUNA
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== MENU PENGGUNA ===")
                print("1. buat reservasi baru")
                print("2. lihat reservasi saya")
                print("3. keluar")
                pilihan_user = input("pilih menu (1/2/3): ")

                # CREATE RESERVASI PENGGUNA
                if pilihan_user == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== BUAT RESERVASI BARU ===")
                    nama = username  # nama pemesan = username pengguna
                    tipe = input("masukkan tipe kamar (single/superior/deluxe): ")
                    tanggal = input("masukkan tanggal reservasi (dd/mm/yyyy): ")
                    durasi = input("masukkan durasi menginap (hari): ")

                    sudah_dibooking = False
                    for data in reservasi.values():
                        if data["Tipe_Kamar"] == tipe and data["Tanggal_Reservasi"] == tanggal:
                            sudah_dibooking = True
                            break

                    if sudah_dibooking:
                        print("maaf, kamar sudah dibooking pada tanggal tersebut")
                    else:
                        reservasi[nama] = {
                            "Tipe_Kamar": tipe,
                            "Tanggal_Reservasi": tanggal,
                            "Durasi": durasi
                        }
                        print("reservasi berhasil dibuat")
                    input("tekan enter untuk melanjutkan...")

                # READ RESERVASI PENGGUNA
                elif pilihan_user == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"=== RESERVASI {username} ===")
                    if username in reservasi:
                        data = reservasi[username]
                        print(f"Nama: {username}")
                        print(f"Tipe Kamar: {data['Tipe_Kamar']}")
                        print(f"Tanggal: {data['Tanggal_Reservasi']}")
                        print(f"Durasi: {data['Durasi']} hari")
                    else:
                        print("belum ada reservasi")
                    input("tekan enter untuk melanjutkan...")

                # KELUAR MENU PENGGUNA
                elif pilihan_user == "3":
                    break
                else:
                    print("pilihan tidak valid")
                    input("tekan enter untuk melanjutkan...")

    # REGISTER
    elif pilih == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER ===")
        username = input("masukkan username baru: ")
        if username in akun:
            print("username sudah ada!")
        else:
            password = input("masukkan password baru: ")
            akun[username] = {"username": username, "password": password, "role": "pengguna"}
            print("registrasi berhasil")
        input("tekan enter untuk kembali ke menu utama...")

    # KELUAR
    elif pilih == "4":
        print("Terima kasih telah menggunakan sistem reservasi!")
        break
    else:
        print("pilihan salah! masukkan 1/2/3/4")
        input("tekan enter untuk kembali...")