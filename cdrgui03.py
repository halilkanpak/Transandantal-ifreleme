import tkinter as tk
from tkinter import *
import math

def cdr():
    Symn=[32, 8, 244, 118, 29, 217, 146, 37, 243, 239, 95, 5, 66, 16, 57, 232, 160, 163, 255, 200, 45, 165, 183, 31, 195, 108, 167, 70, 158, 11, 10, 86, 114, 197, 172, 28, 81, 211, 69, 73, 205, 201, 180, 35, 214, 7, 173, 199, 123, 223, 237, 249, 208, 83, 151, 72, 109, 245, 19, 119, 92, 18, 222, 23, 24, 207, 213, 248, 88, 110, 153, 58, 251, 132, 56, 48, 85, 117, 170, 186, 26, 226, 4, 168, 164, 189, 13, 206, 75, 135, 157, 198, 53, 125, 39, 51, 171, 0, 21, 246, 25, 134, 179, 129, 99, 138, 178, 59, 203, 233, 152, 209, 120, 112, 124, 107, 52, 113, 87, 240, 177, 182, 64, 38, 100, 192, 93, 149, 144, 225, 194, 79, 169, 103, 20, 43, 141, 98, 127, 227, 137, 215, 150, 65, 202, 220, 196, 106, 143, 104, 156, 27, 185, 234, 154, 174, 241, 242, 54, 136, 30, 14, 111, 147, 187, 9, 142, 218, 224, 162, 42, 60, 121, 67, 228, 238, 41, 166, 62, 193, 47, 140, 235, 6, 102, 236, 175, 91, 80, 94, 82, 253, 204, 101, 71, 184, 176, 219, 55, 115, 191, 229, 36, 2, 212, 34, 250, 76, 68, 133, 22, 139, 181, 3, 105, 49, 44, 89, 148, 210, 155, 77, 46, 15, 131, 63, 90, 252, 130, 12, 254, 159, 188, 84, 231, 97, 96, 190, 161, 61, 126, 145, 230, 50, 40, 33, 128, 247, 74, 1, 221, 17, 78, 216, 122, 116]
    metin=şifreliMetin.get()
    for i in range(256-len(metin)):
        Symn.remove(max(Symn))
    karisikmetin=[]
    for i in range(len(metin)):
        karisikmetin.append(0)
    sifrelimetin=[]
    verimetin=[]
    asciimetin=[]
    for i in metin:
        verimetin.append(i)#metni liste haline getirdim verimi arttırmak için alfabeye uygun frekans testleriyle gerekli harflere daha çok transandal sayı atanabalir
    for i in range(len(verimetin)):
        asciimetin.append(ord(verimetin[i]))
    s1=int(taban.get())
    s2=math.sqrt(int(üs.get()))
    for i in range(len(asciimetin)):
        a=(i+1)*(s1 ** s2)
        b=a-int(a)
        c=b*10**40
        d=int(c)
        sifrelimetin.append((asciimetin[i])*d)
    for i in range(len(sifrelimetin)):
        karisikmetin[Symn[i]]=sifrelimetin[i]


    text1.insert(tk.INSERT,karisikmetin)

def temizle():
    text1.delete('1.0',END)
    text1.update()
    
pencere = tk.Tk()
pencere.title("CDR")
pencere.geometry("900x600+200+60")

başlık= tk.Label(text = "Transandantal Sayılar ile Şifreleme")
başlık['font'] = "verdana 10 bold"
başlık['fg'] = "#000000" #16 lık kodlar 000000 siyah renk için
başlık.pack()

metingui1 = tk.Label(text = "Şifrelenecek metni giriniz: ")
metingui1['font'] = "arial 10 bold"
metingui1['fg'] = "#000000" #16 lık kodlar 000000 siyah renk için
metingui1.place(x=10,y=60)

şifreliMetin = tk.Entry(width=100)
şifreliMetin.place(x=220,y=60)

metingui2 = tk.Label(text = "Transandantal sayı için taban ve üs giriniz: ")
metingui2['font'] = "arial 10 bold"
metingui2['fg'] = "#000000" #16 lık kodlar 000000 siyah renk için
metingui2.place(x=10,y=20)

taban = tk.Entry(width=3)
taban.place(x=300,y=23)

üs = tk.Entry(width=3)
üs.place(x=329,y=23)


şifrele = tk.Button(text="ŞİFRELE!",command=cdr)
şifrele['font'] = "verdana 22 bold"
şifrele['fg'] = "#000000"
şifrele.place (x=250, y=95)

temizleb = tk.Button(text="TEMİZLE!",command=temizle)
temizleb['font'] = "verdana 22 bold"
temizleb['fg'] = "#000000"
temizleb.place (x=450, y=95)

text1 = tk.Text(pencere,height=25,width=109)

text1.config(state="normal")


text1.place(x=10,y=160)

pencere.mainloop()

#©Şükrü Yiğit Karaağaç-Halil İbrahim Kanpak 2020

