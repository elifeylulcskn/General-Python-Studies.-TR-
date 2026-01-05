isim = "Elif" #SORU 1
a = 1
b = 2
print(a + b) #SORU 2

print(a ** 2) #SORU 3
print(b ** 3) # SORU 4

sayi1 = input("Sayi giriniz: ") #SORU 5
sayi1_int = int(sayi1)
print(sayi1_int ** 2) #SORU 6

sayii1 = input("Sayi giriniz: ")
sayii1 = int(sayii1)

sayii2 = input("2. sayi giriniz: ")
sayii2 = int(sayii2)
print(sayii1 + sayii2) #SORU 7

if sayii1 %2 == 0:
    print("ÇİFT")
else:
    print("TEK") #SORU 8

if sayii1 < 0 :
    print("SAYI NEGATİF")
else:
    print("SAYI POZTİF") #SORU 9

if sayii1 < 10:
    print("SAYI 10DAN KÜÇÜK")
else:
    print("SAYI 10DAN BÜYÜK") #SORU 10

for i in range(1,11):
    print(i) #SORU 11

for i in range(1,21):
   if i %2 == 0:
    print(i) #SORU 12

for a in range(1,6):
    print(a ** 2) # SORU 13


sayilarr = [1,2,3]
print(sayilarr) #SORU 18

for k in range(1,51):
    k = int(k)
    if k % 2 == 1:
        print(k) #SORU 22


fasayi = int(input("Faktoriyeli hesaplanacak sayiyi giriniz: "))
faktoriyel = 1

for i in range(1, fasayi + 1):
    faktoriyel = faktoriyel * i

print("Faktoriyel:", faktoriyel) #SORU 23

k = input("Kelime gir:")
k = len(k)
print(k) #SORU 24

kelimeler = input("Tekrar bir kelime giriniz: ")
if len(kelimeler) > 5:
    print("Kelime 5 harften uzun")
else:
    print("Kelime 5 harften daha kısa") #SORU 25

    