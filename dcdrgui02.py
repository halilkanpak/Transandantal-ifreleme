import tkinter as tk
from tkinter import *
import math

def dcdr():
    a=[97, 249, 203, 213, 82, 11, 183, 45, 1, 165, 30, 29, 229, 86, 161, 223, 13, 251, 61, 58, 134, 98, 210, 63, 64, 100, 80, 151, 35, 4, 160, 23, 0, 245, 205, 43, 202, 7, 123, 94, 244, 176, 170, 135, 216, 20, 222, 180, 75, 215, 243, 95, 116, 92, 158, 198, 74, 14, 71, 107, 171, 239, 178, 225, 122, 143, 12, 173, 208, 38, 27, 194, 55, 39, 248, 88, 207, 221, 252, 131, 188, 36, 190, 53, 233, 76, 31, 118, 68, 217, 226, 187, 60, 126, 189, 10, 236, 235, 137, 104, 124, 193, 184, 133, 149, 214, 147, 115, 25, 56, 69, 162, 113, 117, 32, 199, 255, 77, 3, 59, 112, 172, 254, 48, 114, 93, 240, 138, 246, 103, 228, 224, 73, 209, 101, 89, 159, 140, 105, 211, 181, 136, 166, 148, 128, 241, 6, 163, 218, 127, 142, 54, 110, 70, 154, 220, 150, 90, 28, 231, 16, 238, 169, 17, 84, 21, 177, 26, 83, 132, 78, 96, 34, 46, 155, 186, 196, 120, 106, 102, 42, 212, 121, 22, 195, 152, 79, 164, 232, 85, 237, 200, 125, 179, 130, 24, 146, 33, 91, 47, 19, 41, 144, 108, 192, 40, 87, 65, 52, 111, 219, 37, 204, 66, 44, 141, 253, 5, 167, 197, 145, 250, 62, 49, 168, 129, 81, 139, 174, 201, 242, 234, 15, 109, 153, 182, 185, 50, 175, 9, 119, 156, 157, 8, 2, 57, 99, 247, 67, 51, 206, 72, 227, 191, 230, 18]
    Symn1=[]
    Symn=[]
    o=0
    u=0
    for o in range(256):
        for u in range(256):
            if o == a[u]:
                u+=1

                Symn1.append(u-1)
    k=şifreliMetin.get('1.0',END)
    karisikmetin = []
    asciimetin = []
    sifrelimetin = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    n=len(k) // 42
    for i in range(256-n):
        Symn1.remove(max(Symn1))
    o=0
    u=0
    for o in range(n):
        for u in range(n):
            if o == Symn1[u]:
                u+=1
                Symn.append(u-1)
    print(Symn)
    karisikmetin = list(map(int, k.strip().split()))[:n]
    for i in range(len(karisikmetin)):
        sifrelimetin[Symn[i]]=karisikmetin[i]
    s1=int(taban.get())
    s2=math.sqrt(int(üs.get()))
    for i in range(len(sifrelimetin)):
        a=(i+1)*(s1 ** s2)
        b=a-int(a)
        c=b*10**40
        d=int(c)
        asciimetin.append(int((sifrelimetin[i])/d))

    Kq=(''.join(map(chr,asciimetin)))
    text1.insert(tk.INSERT,Kq)
    print(Kq)
def temizle():
    şifreliMetin.delete('1.0',END)
    şifreliMetin.update()
    text1.delete('1.0',END)
    text1.update()


pencere = tk.Tk()
pencere.title("DCDR")
pencere.geometry("900x600+200+60")

başlık= tk.Label(text = "Transandantal Sayılar ile Şifreleme")
başlık['font'] = "verdana 10 bold"
başlık['fg'] = "#000000" #16 lık kodlar 000000 siyah renk için
başlık.pack()

metingui1 = tk.Label(text = "Şifreli metni giriniz: ")
metingui1['font'] = "arial 10 bold"
metingui1['fg'] = "#000000" #16 lık kodlar 000000 siyah renk için
metingui1.place(x=10,y=60)

şifreliMetin = tk.Text(pencere,height = 30,width=80)
şifreliMetin.place(x=220,y=60)

metingui2 = tk.Label(text = "Transandantal anahtarın taban ve üssünü giriniz: ")
metingui2['font'] = "arial 10 bold"
metingui2['fg'] = "#000000" #16 lık kodlar 000000 siyah renk için
metingui2.place(x=10,y=20)

taban = tk.Entry(width=3)
taban.place(x=330,y=23)

üs = tk.Entry(width=3)
üs.place(x=359,y=23)


çöz = tk.Button(text="ŞİFREYİ ÇÖZ!",command=dcdr)#KOMUTLARI GİR
çöz['font'] = "verdana 18 bold"
çöz['fg'] = "#000000"
çöz.place (x=5, y=95)

temizleb = tk.Button(text="TEMİZLE!",command=temizle)#KOMUTLARI GİR
temizleb['font'] = "verdana 18 bold"
temizleb['fg'] = "#000000"
temizleb.place (x=5, y=150)

text1 = tk.Text(pencere,height=1,width=80)

text1.config(state="normal")
text1.place(x=220,y=550)

pencere.mainloop()

#©Şükrü Yiğit Karaağaç-Halil İbrahim Kanpak 2020

