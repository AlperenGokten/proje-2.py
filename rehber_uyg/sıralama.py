dosya = open ("rehberlik.txt","r")
print("╔═════════════════════╗")
print("║ Kayıtlı kişiler     ║")
print("╚═════════════════════╝")

for a in range (5):
    okunan = dosya.read(5)
    print(okunan)


dosya.close()
