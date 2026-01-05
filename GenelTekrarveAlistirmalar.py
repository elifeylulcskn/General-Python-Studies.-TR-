#ilk 10.000 asal sayının kaç tanesi 3 ile başlar ve 7 ile biter?

#prime_list = list()

#prime_list.append(2)

#sayi = 3

#while True: #ben çık diyene kadar döngüyü devam ettir demek
 #   prime = True
  #  for i in range(2, int(sayi ** 0.5) + 1) :
   #     if sayi %i == 0:
    #        prime = False
     #       break
        #if prime:
       #     prime_list.append(sayi)
      #      if len(prime_list) == 10000:
         #       break
   # sayi += 1
    #liste2 = []
    #print(prime_list)
   # for prime in prime_list:
    #    strprime = str(prime)
     #   if strprime.startswith("3") and strprime.startswith("7"):
        #    liste2.append(prime)
         #   print(liste2)
          #  print(len(liste2))

#3 basamaklı sayıların kaç tanesi rakamlarının küplerinin toplamına eşittir?


liste = []
for sayi in range(100, 1000):
    toplam = 0
    gecici_sayi = sayi
    while gecici_sayi != 0:
        basamak = gecici_sayi % 10
        toplam += basamak ** 3
        gecici_sayi //= 10
    if toplam == sayi:
        liste.append(sayi)

print(liste)

#Fibonacci sayı dizisi ilk iki 1 olan ve sonraki her terimi kendisinden önceki 2 terimin
#toplamı olan bir sayı dizisidir. ilk 100 fibonacci sayısını ekrana yazdırın.
#1,1,2,3,5,8,13,21,....

#fibonacci_liste = []
#fibonacci_liste.append(1)
#fibonacci_liste.append(1)

#for i in range(2, 100):
 #   fibonacci_liste.append(fibonacci_liste[i-2] + fibonacci_liste[i-1])

#print(fibonacci_liste)
#index = 2
#while True:
 #   fibonacci_liste.append(fibonacci_liste[index - 2] + fibonacci_liste[index - 1])
  #  index += 1
   # if len(fibonacci_liste) == 100:
    #    break
#print(fibonacci_liste)

#100 basamaklı ilk fibonacci sayısını ekrana yazdırın.

fibonacci_liste = list()
fibonacci_liste.append(1)
fibonacci_liste.append(2)

index = 2
while True:
    fibonacci_liste.append(fibonacci_liste[index - 2] + fibonacci_liste[index - 1])
    terim = fibonacci_liste[index -  2] + fibonacci_liste[index - 1]
    if len(str(terim)) == 1000:
        print(terim)
        break
    index += 1
