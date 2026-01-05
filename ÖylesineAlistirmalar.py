isim = "Elif"
print(isim)

yas = 19
a = 3
b = 5


print("İşte yaşınız", yas + a + b)

print("Ben Elif, 20 yaşomdayım.")

ad = input("Adınızı girin.")
print("Hoş geldin," , ad)
yasiniz = input("Yasinizi girin.")

yasiniz_int = int(yasiniz)
print(yasiniz_int)

renkler = input("Renkleri lütfen girin.")
print("Teşekkür ederiz, işte renkler" , renkler)

sayi = input("Bir sayı girin.")
sayi_int = int(sayi)
sayikaresi = sayi_int ** 2
print(sayikaresi)

ikincisayi = input("İkinci sayı girin.")
ikincisayi_int = int(ikincisayi)

ikincisayikaresi = ikincisayi_int ** 2
print(ikincisayikaresi)

print(sayikaresi + ikincisayikaresi)

birsayi = input("Bir sayi gir artık.")
birsayi_int = int(birsayi)

if birsayi_int % 2 == 0:
    print("Sayi çift")
else:
    print("Sayi tek")

kullaniciyas = input("Yaş gir.")
kullaniciyas_int = int(kullaniciyas)

if kullaniciyas_int > 18:
    print("REŞİT")
else:
    print("ÇOCUK")

kullaniciyas_int = input("Yaş tekrar gir.")

if kullaniciyas_int > 80:
    print("İHTİYAR")
else:
    print("REŞİT")



#for forsayi in range (11): BİRDEN 10A KADAR YAZDIR
    #print(forsayi)

for forsayi in range(0, 11):
    if forsayi % 2 == 0:
        print(forsayi)

meyveler = ["elma", "muz",  "çilek", "uzum"]
print(meyveler)





