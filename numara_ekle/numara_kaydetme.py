dosya = open("rehberlik.txt","a")
ad = input("kaydedilicek ad ve soyad :")
nu = input ("kaydedilicek numara   :")

veri = ad+" "+nu+"\n"
dosya.write(veri)
dosya.close

with open("rehberlik.txt", "a+") as f:
    f.seek(0)
    f.write("Alperen Gokten\t: 05438857422\n")
