from prettytable import PrettyTable

def tampilkan_reservasi(reservasi):
    if not reservasi:
        print("tidak ada data reservasi")
        return
    
    table = PrettyTable()
    table.field_names = ["No", "Nama", "Tipe Kamar", "Tanggal Reservasi", "Durasi Menginap"]

    for i, (nama, data) in enumerate(reservasi.items(), start=1):
        table.add_row([i, nama, data["tipe_kamar"], data["tanggal_reservasi"], data["durasi_menginap"]])

    print(table)