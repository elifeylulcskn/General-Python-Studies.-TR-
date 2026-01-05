print("Part 1")
print("")
def list2DigitEven() :
    list1 = []
    for i in range(10, 100, 2):
        list1.append(i)
        return list1
    print(list2DigitEven)

    #2 SORU TAKIMLAR VE NUMARALARI
    #İSTENİLEN : ('Tottenham', 23, 'Manchester_City', 21, 'Arsenal', 21)
    #('Burnley', 4, 'Bournemouth', 3, 'Sheffield_Utd', 1)
    #"Tottenham" "Manchester_City" "Arsenal" "Liverpool Aston_Villa
    #"Newcastle"  "Brighton" "Manchester_Utd_West_Ham" "Chelsea" "Crystal_Palace" "Wolverhampton" "Fulham"
    #"Brentgord" "Nottingham_Forest" "Everton" "Luton_Town" "Burnley" "Bournemouth" "Sheffield_Utd"

    #23 21 20 19 16 16 15 14 112 11 11 10 10 7 5 4 3 1

    #takimlar = input().split()
    #puanlar = input().split()

    #en_iyi = list()
    #en_kotu = list()
    #for i in range (3):
        #en_iyi.append(takimlar[i])
        #en_iyi.append(int(puanlar[i]))

        #for i in range(-3, 0)
            #en_kotu.append(takimlar[i])
            #en_kotu.append(puanlar[i])

            #print(tuple(en_iyi))
            #print(tuple(en_kotu))

# == BASİT TAHMİN OYUNU ==
import random

print("Basit Tahmin Oyununa Hoş Geldiniz!")
sayı =random.randint(1,100)
tahmin_hakkı = 5

while True:
    tahmin = int(input("Tahmini Gir: "))
    if tahmin == sayı:
        print("Tebrikler! Doğru tahmin ettiniz.")
        break
    elif tahmin < sayı:
        print("Daha büyük bir sayı girin.")
    else:
        print("Daha küçük bir sayı girin.")

        tahmin_hakkı -= 1
        if tahmin_hakkı == 0:
            print("Tahmin hakkın bitti! Doğru cevap", sayı, "idi.")
            break



# === ORTALAMA HESAPLAMA ===
import time


def aciklamalar():
    baslık = """Klavyeden girilen N adet tam sayının 
negatif ve pozit olanları ile tüm sayıların
ayrı ayrı ortalamasını bulan program"""

    print("*" * (len(baslık) // 3), baslık, "*" * (len(baslık) // 3), sep="\n", end="\n\n")

    print("İşlemin sonlanması için rakam dışında bir karaktere basın !")


def ortalamaHesaplama():
    ortHep = ortPoz = ortNeg = poz = neg = sayP = sayN = 0
    sayac = 1

    while True:

        try:
            sayi = int(input("{}. tam sayıyı giriniz :".format(sayac)))
        except:
            # Hata verirse demekki kullanıcı rakam dışı bir karakter girmiştir.
            print("1) Pozitif{0}{1}\n2) Negatif{0}{2}\n3) Tüm{0}{3}".format(" tam sayıların ortalaması => ", ortPoz,
                                                                            ortNeg, ortHep))
            break
        else:
            # Bu kısım çalışıyorsa demekki giriş verisi uygundur.
            sayac += 1
            if sayi >= 0:
                poz += sayi
                sayP += 1
                ortPoz = poz / sayP
            else:
                neg += sayi
                sayN += 1
                ortNeg = neg / sayN

            ortHep = (neg + poz) / (sayN + sayP)


if __name__ == "__main__":
    aciklamalar()
    ortalamaHesaplama()
    print("Program Kapatılıyor....")
    time.sleep(5)

