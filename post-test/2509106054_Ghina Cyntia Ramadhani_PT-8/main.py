from tools import clear, pause, tidak_valid
from login import login_admin, login_pengguna, register_akun
from main_data import akun, reservasi, running
from reservasi import tambah_data_reservasi, lihat_data_reservasi, ubah_data_reservasi, hapus_data_reservasi, cari_data_reservasi, filter_data_reservasi

running = True

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
            print("pilihan tidak valid")
    except Exception as e:
        print(f"terjadi kesalahan: {e}")


if __name__ == "__main__":
    while running:
        menu_awal()

    clear()
    print("terima kasih telah menggunakan sistem reservasi hotel")