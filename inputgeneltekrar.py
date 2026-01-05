#ekrandan alınan bir sayının faktöriyelini hesaplayan bir program yazın.
#sayi = int(input("Bir sayi girin lütfen:"))
#print(type(sayi))

#faktoriyel = 1
#for i in range(1, sayi + 1):
 #   faktoriyel *= i
  #  print(f"{sayi}! = {faktoriyel}")

#i = 2
#while i <= sayi:
 #   faktoriyel *= i
  #  i += 1

#sayi = int(input("Asal Sayı mı değil mi kontrol?:")) #ASAL SAYI MI DEĞİL Mİ PROGRAMI
#print(sayi)

#if sayi <= 1:
 #   print("Sayi asal değil")
#else:
 #   asal = True
  #  for i in range(2, sayi):
   #     if sayi % i == 0:
    #        asal = False
     #       break
#if asal:
 #   print("Girdiğiniz sayı ASAL.")
#else:
 #   print("Asal DEĞİL.")

#sayi = int(input("Bir sayi girin:")) #KAÇ POZİTİF BÖLEN VAR BULMA PROGRAMI
#bolen_sayisi = 0

#for i in range(1, sayi + 1):
 #   if  sayi %i == 0:
  #      bolen_sayisi += 1
   # print(f"{sayi} sayısının {bolen_sayisi} tane boleni vardır.")

#EKRANDAN OKUNAN BİR SAYININ RAKAMLARINI TOPLAYAN BİR PROGRAM YAZ
#sayi = int(input("Bir sayi girin:"))
#str_sayi = str(sayi)
#toplam = 0
#for rakam in str_sayi:
 #   toplam += int(rakam)

#print(toplam)

#EKRANDAN PEŞPEŞE OKUNAN 5 SAYININ EN KÜÇÜĞÜNÜ VE EN BÜYÜĞÜNÜ EKRANA YAZDIRAN BİR PROGRAM YAZIN.
# Aynı hizadaki satırlar, aynı bloğa aittir
# Fazladan boşluk → başka blok
# Yanlış boşluk → hata
#liste = []
#for i in range(5):
 #   sayi = int(input("Bir sayı gir:"))
  #  liste.append(sayi)

#print(f"en büyük sayı : {max(liste)}")
#print(f"en küçük sayı : {min(liste)}")

#EKRANDAN OKUNAN BİR SAYININ HERHANGİ BİR SAYININ KARESİ OLUP OLMADIĞINI KONTROL EDEN BİR PROGRAM YAZIN.
#sayi = int(input("Bir sayı gir:"))
#kare_mi = False
#for i in range(1, sayi + 1):
  #      if i * i == sayi:
 #           kare_mi = True
#            break
#if kare_mi:
 #   print("Girilen sayı, bir sayının karesidir")
#else:
  #print("Girilen sayı, bir sayının karesi DEĞİLDİR.")



