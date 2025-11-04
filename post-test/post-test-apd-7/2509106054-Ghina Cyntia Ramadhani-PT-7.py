import os
os.system('cls' if os.name == 'nt' else 'clear')

#data akun & reservasi (variabel global)
akun = {
    "admin": {"username": "admin", "password": "admin123", "role": "admin"},
    "pengguna": {"username": "pengguna", "password": "pengguna123", "role": "pengguna"}
}   
reservasi = {}
running = True

#prosedur
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("tekan enter untuk melanjutkan...")

#error handling
def tidak_valid(teks):
    if teks.strip() == "":
        raise ValueError("input tidak boleh kosong")

#fungsi tanpa parameter
def menu_awal():
    global running
    clear()
    print("=== SISTEM RESERVASI HOTEL ===")
    print("1. login admin")
    print("2. login pengguna")
    print("3. register")
    print("4. keluar")
    pilih = input("pilih menu (1/2/3/4): ")
        
    try:
        if pilih == "1":
            login_admin()
        elif pilih == "2":
            login_pengguna()
        elif pilih == "3":
            register_akun()
        elif pilih == "4":
            running = False
        else:
            raise ValueError("pilihan tidak valid")
    except Exception as e:
        print(f"terjadi kesalahan: {e}")
        pause()
        menu_awal()

def menu_admin():
    while True:
        clear()
        print("=== MENU ADMIN ===")
        print("1. tambah data reservasi (create)")
        print("2. lihat data reservasi (read)")
        print("3. ubah data reservasi (update)")
        print("4. hapus data reservasi (delete)")
        print("5. cari data reservasi")
        print("6. filter berdasarkan tanggal")
        print("7. logout")
        pilih = input("pilih menu (1/2/3/4/5/6/7): ")

        try:
            if pilih == "1":
                clear()
                print("=== TAMBAH DATA RESERVASI ===")
                nama = input("nama: ")
                tipe_kamar = input("tipe kamar (single/superior/deluxe): ")
                tanggal = input("tanggal reservasi (dd-mm-yyyy): ")
                durasi= input("durasi menginap (hari): ")
                tambah_data_reservasi(nama, tipe_kamar, tanggal, durasi)
                
            elif pilih == "2":
                clear()
                print("=== LIHAT DATA RESERVASI ===")
                lihat_data_reservasi()
                
            elif pilih == "3":
                clear()
                print("=== UBAH DATA RESERVASI ===")
                ubah_data_reservasi()
                
            elif pilih == "4":
                clear()
                print("=== HAPUS DATA RESERVASI ===")
                hapus_data_reservasi()
                
            elif pilih == "5":
                clear()
                print("=== CARI DATA RESERVASI ===")
                nama = input("masukkan nama reservasi yang ingin dicari: ")
                cari_data_reservasi(nama)
                
            elif pilih == "6":
                clear()
                print("=== FILTER DATA RESERVASI BERDASARKAN TANGGAL ===")
                tanggal =  input("masukkan tanggal reservasi yang ingin difilter (dd-mm-yyyy): ")
                filter_data_reservasi(tanggal)
            elif pilih == "7":
                print("logout berhasil")
                pause()
                break
            else:
                raise ValueError("pilihan tidak valid")
                pause()
        except Exception as e:
            print(f"terjadi kesalahan: {e}")
            pause()

def menu_pengguna():
    global running
    clear()
    print("=== MENU PENGGUNA ===")
    print("1. tambah data reservasi")
    print("2. lihat reservasi saya")
    print("3. logout")
    pilih = input("pilih menu (1/2/3): ")

    try:
        if pilih == "1":
            clear()
            print("=== TAMBAH DATA RESERVASI ===")
            nama = input("nama: ")
            tipe_kamar = input("tipe kamar (single/superior/deluxe): ")
            tanggal = input("tanggal reservasi (dd-mm-yyyy): ")
            durasi = input("durasi menginap (hari): ")
            tambah_data_reservasi(nama, tipe_kamar, tanggal, durasi)
            menu_pengguna()
        elif pilih == "2":
            clear()
            print("=== LIHAT RESERVASI SAYA ===")
            nama = input("masukkan nama yang anda gunakan saat reservasi: ")
            if nama in reservasi:
                data = reservasi[nama]
                print(f"nama: {nama}, tipe kamar: {data['tipe_kamar']}, tanggal reservasi: {data['tanggal_reservasi']}, durasi menginap: {data['durasi_menginap']} hari")
            else:
                print("anda belum memiliki reservasi")
            pause()
            menu_pengguna()
        elif pilih == "3":
            return
        else:
            print("pilihan tidak valid")
            pause()

    except Exception as e:
        print(f"terjadi kesalahan: {e}")
        pause()
        
#fungsi dengan parameter
def tambah_data_reservasi(nama, tipe_kamar, tanggal, durasi):
    clear()
    print("=== TAMBAH DATA RESERVASI ===")
    if cek_ketersediaan_kamar(tipe_kamar, tanggal):
        print("maaf, kamar tidak tersedia pada tanggal tersebut")
        pause()
    else:
        reservasi[nama] = {
            "tipe_kamar": tipe_kamar,
            "tanggal_reservasi": tanggal,
            "durasi_menginap": durasi
        }
        print("data reservasi berhasil ditambahkan")
        pause()

def cek_ketersediaan_kamar(tipe, tanggal):
    for data in reservasi.values():
        if data["tipe_kamar"] == tipe and data["tanggal_reservasi"] == tanggal:
            return True
    return False

def lihat_data_reservasi():
    clear()
    print("=== DATA RESERVASI ===")
    if not reservasi:
        print("tidak ada data reservasi")
    else:
        for i, (nama, data) in enumerate(reservasi.items(), start=1):
            print(f"{i}. nama: {nama}, tipe kamar: {data["tipe_kamar"]},  tanggal reservasi: {data['tanggal_reservasi']}, durasi menginap: {data['durasi_menginap']} hari")
    pause()
    
def ubah_data_reservasi():
    clear()
    print("=== UBAH DATA RESERVASI ===")    
    if not reservasi:
        print("tidak ada data reservasi untuk diubah")
        pause()
        return
        
    for i, (nama, data) in enumerate(reservasi.items(), start=1):
        print(f"{i}. nama: {nama}, tipe kamar: {data['tipe_kamar']}, tanggal: {data['tanggal_reservasi']}, durasi: {data['durasi_menginap']} hari")

    try:
        no = int(input("masukkan nomor data reservasi yang ingin diubah: "))
        if no < 1 or no > len(reservasi):
            print("nomor data reservasi tidak valid")
            pause()
            return
            
        key_list = list(reservasi.keys())
        key = key_list[no - 1]

        nama_baru = input("masukkan nama baru (kosongkan jika tidak diubah): ") or key
        tipe_baru = input("masukkan tipe kamar baru (kosongkan jika tidak diubah): ") or reservasi[key]["tipe_kamar"]
        tanggal_baru = input("masukkan tanggal reservasi baru (kosongkan jika tidak diubah): ") or reservasi[key]["tanggal_reservasi"]
        durasi_baru = input("masukkan durasi menginap baru (kosongkan jika tidak diubah): ") or reservasi[key]["durasi_menginap"]

        reservasi.pop(key)
        reservasi[nama_baru] = {
            "tipe_kamar": tipe_baru,
            "tanggal_reservasi": tanggal_baru,
            "durasi_menginap": durasi_baru
        }
        print("data reservasi berhasil diubah")
        pause()

    except Exception as e:
        print(f"terjadi kesalahan: {e}")
        pause()
        
def hapus_data_reservasi():
    clear()
    print("=== HAPUS DATA RESERVASI ===")
    if not reservasi:
        print("tidak ada data reservasi untuk dihapus")
        pause()
        return
    for i, (nama, data) in enumerate(reservasi.items(), start=1):
        print(f"{i}. nama: {nama}, tipe kamar: {data['tipe_kamar']}, tanggal: {data['tanggal_reservasi']}, durasi: {data['durasi_menginap']} hari")

    try:
        no = int(input("masukkan nomor data reservasi yang ingin dihapus: "))
        if no < 1 or no > len(reservasi):
            print("nomor data reservasi tidak valid")
            pause()
            return

        key_list = list(reservasi.keys())
        key = key_list[no - 1]

        del reservasi[key]
        print("data reservasi berhasil dihapus")
        pause()

    except ValueError as e:
        print(f"terjadi kesalahan: {e}")
        pause()

def cari_data_reservasi(nama):
    clear()
    print("=== CARI DATA RESERVASI ===")
    if nama in reservasi:
        data = reservasi[nama]
        print(f"Nama: {nama}, Tipe Kamar: {data['tipe_kamar']}, Tanggal Reservasi: {data['tanggal_reservasi']}, Durasi Menginap: {data['durasi_menginap']} hari")
    else:
        print("data reservasi tidak ditemukan")
    pause()

def filter_data_reservasi(tanggal):
    clear()
    print(f"=== DATA RESERVASI PADA TANGGAL {tanggal} ===")
    ditemukan = False
    for nama, data in reservasi.items():
        if data["tanggal_reservasi"] == tanggal:
            print(f"Nama: {nama}, Tipe Kamar: {data['tipe_kamar']}, Durasi Menginap: {data['durasi_menginap']} hari")
            ditemukan = True
    if not ditemukan:
        print("tidak ada data reservasi pada tanggal tersebut")
    pause()

#fungsi rekursif
def login_admin():
    clear()
    print("=== LOGIN ADMIN ===")
    try:
        username = input("masukkan username: ")
        password = input("masukkan password: ")

        tidak_valid(username)
        tidak_valid(password)

        if username == akun["admin"]["username"] and password == akun["admin"]["password"]:
            print("login berhasil sebagai admin")
            pause()
            menu_admin()
            return
        else:
            print("username atau password salah")
            pause()
            return login_admin()

    except Exception as e:
        print(f"terjadi kesalahan: {e}")
        pause()
        return login_admin()    
    
def login_pengguna():
    clear()
    print("=== LOGIN PENGGUNA ===")
    try:
        username = input("masukkan username: ")
        password = input("masukkan password: ")

        tidak_valid(username)
        tidak_valid(password)

        if username in akun and akun[username]["password"] == password:
            print("login berhasil sebagai pengguna")
            pause()
            menu_pengguna()
            return
        else:
            print("username atau password salah")
            pause()
            return login_pengguna()
            
    except Exception as e:
        print(f"terjadi kesalahan: {e}")
        pause()
        return login_pengguna()
    
def register_akun():
    clear()
    global akun
    print("=== REGISTER AKUN ===")
    try:
        username = input("masukkan username baru: ")
        password = input("masukkan password baru: ")

        tidak_valid(username)
        tidak_valid(password)

        if username in akun:
            print("username sudah terdaftar")
        else:
            akun[username] = {
                "username": username,
                "password": password,
                "role": "pengguna"
            }
            print("registrasi berhasil, silakan login.")
    except Exception as e:
        print(f"terjadi kesalahan: {e}")
        pause()
        return register_akun()
    
#program utama      
while running:
    menu_awal()

clear() 
print("terima kasih telah menggunakan sistem reservasi hotel")