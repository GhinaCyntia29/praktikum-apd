from tools import clear, pause, tidak_valid
from main_data import akun
from reservasi import menu_admin, menu_pengguna

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
            pause()
    except Exception as e:
        print(f"terjadi kesalahan: {e}")
        pause()
        return register_akun()