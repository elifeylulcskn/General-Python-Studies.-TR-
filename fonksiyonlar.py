#Fonksiyon kavramı ve önemi
#Fonksiyonları tanımlama ve çalıştırma
#Parametre almayan ve alan fonksiyonlar
#return anahtar kelimesi
#parametrelere varsayılan değerler atamak

#print("İşlem başarılı.")
#print("İşlem başarılı!")

def bilg_ver(): #def fonksyion tanımlayacağımızın anahtar kelimesi
    print("İşlem başarılı.") #tek tek değiştirmeye gerek kalmadan birfonksiyon şeklinde atarsanız ve bu print
    print("Bloğun içerisi")  # yazısındaki herhangi bir değişiklik aşağıda devam eden fonksiyonlara da aktarılır.

#bilg_ver parantezsiz olursa fonksiyonu çağıramıypruz. PARANTEZ OLMALI
bilg_ver()

def selamla(isim): #parantez içi parametredir. isim şeklinde parametre atanır ve selamla fonksiyonunun içerisine değer atanır.
    print("Merhaba " + isim)
selamla("Elif")

def topla(x,y):
    print(f"X + Y = {x + y}")

topla(3,6)

def ortalama_hesapla(liste):
    toplam = sum(liste)
    adet = len(liste)  
    ortalama = toplam / adet
    print(f"Girilen sayıların ortalaması = {ortalama}")

ortalama_hesapla([1,2,3,4,5,6]) #içerisine liste ve liste elemanları almalı

def buyuk_harfe_cevir(metin):
    metin = metin.upper() #hepsini büyük harf yapıyor
    print(metin)
buyuk_harfe_cevir("AnSYtYY")

def selamlama(mesaj,isim): #ikinci parametreye isim verilmezse altta, def kısmındaki paranteze parametreye karşılık geleni verir.
    print(f"{mesaj} {isim}.")
selamlama("Merhaba", "Elif")

def indirim_yap(fiyat, yuzde):
    indirim_miktarı = fiyat * (yuzde / 100)
    indirimli_fiyat = fiyat - indirim_miktarı
    print(f"İndirimli tutar : {indirimli_fiyat}")

indirim_yap(50,10)

def toplamak(k,l):
    print(k + l)
    return k + l  #başka bir değişkene atayıp çalıştırmak istiyorsak. Hehrnagi bir değer geri döndürmesi demek.

sonuc = toplamak(3,8)
print(sonuc)

def ortalama_hesaplamak(a,b):
    return (a + b) / 2

print(ortalama_hesaplamak(3,8))
print(type(ortalama_hesaplamak(2,6)))

c = ortalama_hesaplamak(2,6)
d = ortalama_hesaplamak(6,10)
print(c + d)