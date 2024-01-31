import re, json, ast

def menu():
  
    print("╔═════════════════════╗")
    print("║  REHBER UYGULAMASI  ║")
    print("║                     ║")
    print("║  1-Rehber ekle      ║")
    print("║  2-kayıtları listele║")
    print("║  3-kayıt ara        ║")
    print("║  4-kayıt düzelt     ║")
    print("║  5-numara sil       ║")
    print("║  6-çıkıi            ║")
    print("║  Seçimiz nedir?     ║")
    print("╚═════════════════════╝")


    secim = input("")
    if secim=="1":
        listele()
        kisiEkle()
        listele()
        menu()
    if secim=="2":
        listele()
        menu()
    if secim=="3":
        ara()
        menu()
    if secim=="4":
        duzelt()
        listele()
        menu()
    if secim=="5":
        sil()
        listele()
        menu()

def kisiEkle():
    dosya = open("rehber.txt","a")
    print("╠════════════╣ KİŞİ EKLEME ╠════════════╣")
    ad = input("Kaydedilecek ad ve soyad :")
    nu = input("Kaydedilecek numara      :")
    dosya.write(f'{str({"adi":ad,"num":nu})},')
    dosya.close()

def listele():
    try:
        import re, json, ast
        with open("rehber.txt", "r") as dosya:
            okunan = dosya.read()
        print("╠════════════╣ KİŞİ LİSTELEME ╠════════════╣")

        cevirilen = ast.literal_eval(okunan)
        # print(cevirilen)
        for a in cevirilen:
            print (a)
    except :
        print("Bir hata oluştu")          
def ara():
    with open("rehber.txt", "r") as dosya:
        okunan = dosya.read()
    print("╠════════════╣ KİŞİ ARAMA ╠════════════╣")

    cevirilen = ast.literal_eval(okunan)
    aranan = input("Aranan isim nedir?")
    for a in cevirilen:
        if a["adi"]==aranan: print(a)

def duzelt():
    with open("rehber.txt", "r") as dosya:
        okunan = dosya.read()
    print("╠════════════╣ KİŞİ DÜZELTME ╠════════════╣")

    cevirilen = ast.literal_eval(okunan)
    aranan = input("Düzeltilecek isim nedir? ")
    dosya.close()
    with open("rehber.txt","w") as dosya:
        for a in cevirilen:
            if a["adi"]==aranan:
                print(a)
                yeniAd = input("Yeni ad nedir? ")
                yeniNo = input("Yeni no nedir? ")
                a["adi"]=yeniAd
                a["num"]=yeniNo
            dosya.write(f"{str(a)},")        

def sil():
    with open("rehber.txt", "r") as dosya:
        okunan = dosya.read()
    print("╠════════════╣ KİŞİ SİLME ╠════════════╣")

    cevirilen = ast.literal_eval(okunan)
    aranan = input("Silinecek isim nedir? ")
    dosya.close()
    with open("rehber.txt","w") as dosya:
        for a in cevirilen:
            if a["adi"]!=aranan:
                dosya.write(f"{str(a)},")

menu()
