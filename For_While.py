# Listeler ile for döngüsü
# range fonksiyonu ve for döngüsü
# iç içe for döngüleri
# break ve continue anahtar kelimeleri
# while döngüsü
# DÖNGÜLER : Tek tek listeler iprint ile yazdırmak yerine, bütün elemanları aynı işi yapacak şeye döngü denir.

 #liste = [1,2,3,4,5,6]
#print(liste[0])
#print(liste[1])
#print(liste[2])
#print(liste[3]) MANTIKLI DEĞİL

#for rakam in liste:
#    print(rakam)
#rakam bir değişken gibi. İlk önce 1in yerini aldı, sonra 2, sonra 3... gibi. Listedeki elemanlar için bunu tekrarladı.
#Ayrı ayrı yazılmaya gerek kalmadı. For döngüsü bunu halletti. Rakam, listenin içinde olduğu sürece bu rakamları yazdır demek.

#isim = "ELA" #stringlerde kullanılabilir. demetlerde de.

#for harf in isim:
   #print(harf)

#demet = (1,2,3,4)
#for i in demet:
 #   print(i)

#for a range(10):
 #   for a range(0,10): BU İKİSİ AYNI ŞEY

#sonuc = 1
#for i in range(0 , 10):
 #   sonuc *= 2
  #  print(sonuc)  RANGE LİSTEDEKİ BÜTÜN ELEMANLAR İÇİN AYNI İŞLEMİ YAPMAK YERİNE BİR İŞLEMİ BELİRLİ BİR SAYIDA TEKRAR ETMEK İÇİN.

#liste1 = ["a", "b", "c"]
#liste2 = [1,2,3]
#for harf in liste1:
  #  for rakam in liste2:
 #       print(harf, rakam)
        #HARF İLK ÖNCE A OLUYOR, SAYI DEĞERİ 1,2,3. SONRA HARF B OLUYOR, SAYI DEĞERİ 1,2,3 GİBİ GİBİ.



liste = range(100)

for i in liste:
    if i %3 != 0:
        continue
    if i == 81:
        break #81 E GELİNCE DÖNGÜYÜ DURDURUR.
    print(i)
    #ŞU AN DÖNGÜDE SADECE 3E TAM BÖLÜNEN SAYILAR YAZILACFAK


    # liste= [1,2,3,4,5,6,7,8,9]
    # for i in liste:
    #   if i == 3: # LİSTEDE 3 SİLİP, DÖNGÜNÜN DEVAM ETMESİNİ İSTERSEK. PAS GEÇER.
      #  print("(3 ü atladık.)")
       # continue #DÖNGÜ DEVAM EDER.
       # break DÖNGÜYÜ SONLANDIRIR.
   # print(i)

#while x < 10:
  #  print(x)
   # x += 1
    #print("x = " , x)
    #BİR ARTTIRARAK DEVAM EDER. DÖNGÜ X = 10 OLDUĞUNDA SONA ERER.

#x = 2
#y = 3
#while  x * y < 1000:
 #   print(x,y)
  #  x += 2
   # y += 2
    #DÖNGÜ İKİ SAYININ ÇARPIMI 1000İ GEÇERSE SONLANIR.


#i = 1
#while True:
   # print(i)
    #i += 1
    #if i == 10000:
     #   break
        #BREAK GİBİ, YA DA IF GİBİ SINIR KONMAZSA DÖNGÜ SONSUZA KADAR DEVAM EDER.

i = 1
while True:
    if i % 2 == 0:
        i += 1 #CONTINUE DEMEDEN ÖNCE İ ARTTIRMALIYIZ YOKSA KISIR DÖNGÜYE GİRER.
        continue
    print(i)
    i = i + 1 #WHILE TRUE ŞEKLİNDE KULLANILIYORSA MUTLAKA DEĞİŞKEN BİR YERLERDE ARTTIRMALIYIZ.
    if i == 1000:
        break

