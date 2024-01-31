import sys
import time

def nummenu():
    
        dosya = open("rehberlik.txt","r")
        print("   Rehber Kayıt Listesi ")        
        print("═════════════════════════════")
        a = 1        
        kayit = {}
        for k in dosya.readlines():
            kayit = k
            print(k)


nummenu()

