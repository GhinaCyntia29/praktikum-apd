import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("tekan enter untuk melanjutkan...")

def tidak_valid(teks):
    if teks.strip() == "":
        raise ValueError("input tidak boleh kosong")