suhu=[27,33,46,55,67,92]

fahrenheit1=(suhu[0]*9/5)+32
fahrenheit2=(suhu[1]*9/5)+32
kelvin1=suhu[2]+273.15
kelvin2=suhu[3]+273.15    
reamur1=suhu[4]*(4/5)
reamur2=suhu[5]*(4/5)
jumlah=fahrenheit1+fahrenheit2+kelvin1+kelvin2+reamur1+reamur2
ratarata=jumlah/6
nim=54
boolean=nim<ratarata
print("suhu ke-1=",suhu[0],"C")
print("suhu ke-2=",suhu[1],"C")
print("suhu ke-3=",suhu[2],"C")
print("suhu ke-4=",suhu[3],"C")
print("suhu ke-5=",suhu[4],"C")
print("suhu ke-6=",suhu[5],"C")
print("suhu fahrenheit dari 27 celcius=",fahrenheit1,"F")
print("suhu fahrenheit dari 33 celcius=",fahrenheit2,"F")
print("suhu kelvin dari 46 celcius=",kelvin1,"K")
print("suhu kelvin dari 55 celcius=",kelvin2,"K")
print("suhu reamur dari 67 celcius=",reamur1,"R")
print("suhu reamur dari 92 celcius=",reamur2,"R")
print("jumlah suhu=",jumlah)
print("rata-rata suhu=",ratarata)
print("nim=",nim)
print("boolean=",boolean)

print ("list suhu dari 46 sampai 92:",suhu [-4:6])