mod=int(input("mod değerini giriniz : "))+1
a=[1,1,35,2,2,3,3,8,9,10]
b=[]
c=[]
for i in range(len(a)):
    b.append(0)
for i in range(mod):
    s=a.count(i)
    c.append(i)
    c.append(s)

e=[]
d=[]
for i in range(len (a)):
    if a[i] >len (a):
        e.append(a[i])
e.sort()
e.reverse()
for i in range(len(e)):
    k=a.index(e[i])
    a[k]=len(a)-i

for i in range(len (a)):
    if a[i] <= len (a):
        d.append(a[i])
d.sort()

for i in range(len(d)):
    k=a.index(d[i])
    a[k]=i+1






    
#©Şükrü Yiğit Karaağaç-Halil İbrahim Kanpak 2020
print(a)
