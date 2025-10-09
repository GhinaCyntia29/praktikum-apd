#login
username_benar = "ghina"
password_benar = "054"

login_gagal = True
while login_gagal:
    print ("silahkan login")
    
    username = input ("masukkan username: ")
    password = input ("masukkan password: ")
    
    if username == username_benar and password == password_benar:
        print ("login berhasil!")
        login_gagal = False
    elif username != username_benar and password == password_benar:
        print ("username salah, silahkan coba lagi")
    elif username == username_benar and password != password_benar:
        print ("password salah, silahkan coba lagi")
    else:
        print ("username dan password salah, silahkan coba lagi")
    if login_gagal:
        print ("-"*35)
        print ("program dilanjutkan")

#input golongan darah  dan rhesus
ulang = "Y"

#variabel total darah
A_positif = 0
A_negatif = 0
B_positif = 0
B_negatif = 0
AB_positif = 0
AB_negatif = 0
O_positif = 0
O_negatif = 0

while ulang == "Y":
    golongan = input("masukkan golongan darah (A/B/AB/O): ")

    if golongan == "A":
        rhesus = input("masukkan rhesus (+/-): ")
        if rhesus == "+":
            A_positif += int(input("masukkan jumlah kantong darah: ")) * 500       
        elif rhesus == "-":
            A_negatif += int(input("masukkan jumlah kantong darah: ")) * 500
        else:
            print("input rhesus salah")

    elif golongan == "B":
        rhesus = input("masukkan rhesus (+/-): ")
        if rhesus == "+":
            B_positif += int(input("masukkan jumlah kantong darah: ")) * 500       
        elif rhesus == "-":
            B_negatif += int(input("masukkan jumlah kantong darah: ")) * 500
        else:
            print("input rhesus salah")
        
    elif golongan == "AB":
        rhesus = input("masukkan rhesus (+/-): ")
        if rhesus == "+":
            AB_positif += int(input("masukkan jumlah kantong darah: ")) * 500       
        elif rhesus == "-":
            AB_negatif += int(input("masukkan jumlah kantong darah: ")) * 500
        else:
            print("input rhesus salah")

    elif golongan == "O":
        rhesus = input("masukkan rhesus (+/-): ")
        if rhesus == "+":
            O_positif += int(input("masukkan jumlah kantong darah: ")) * 500       
        elif rhesus == "-":
            O_negatif += int(input("masukkan jumlah kantong darah: ")) * 500
        else:
            print("input rhesus salah")

    else:
        print("input golongan darah salah")

    ulang = input("apakah anda ingin menginput data lagi? (Y/T): ")

#ringkasan data darah
print("ringkasan data darah:")
print("golongan darah A:")
print("A+ :", A_positif, "ml")
print("A- :", A_negatif, "ml")
print("total A :", A_positif + A_negatif, "ml")

print("golongan darah B:")
print("B+ :", B_positif, "ml")
print("B- :", B_negatif, "ml")   
print("total B :", B_positif + B_negatif, "ml")

print("golongan darah AB:")
print("AB+ :", AB_positif, "ml")
print("AB- :", AB_negatif, "ml")
print("total AB :", AB_positif + AB_negatif, "ml")

print("golongan darah O:")
print("O+ :", O_positif, "ml")
print("O- :", O_negatif, "ml")
print("total O :", O_positif + O_negatif, "ml")

#total keseluruhan darah
total_semua = (
    A_positif + A_negatif +
    B_positif + B_negatif +
    AB_positif + AB_negatif +
    O_positif + O_negatif
)
print ("total keseluruhan darah:", total_semua, "ml") 