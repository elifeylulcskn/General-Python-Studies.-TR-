# Liste nedir ve nasıl oluşturulur?
# Liste nasıl yazdırılır?
# Len fonksiyonu nedir?
# Liste elemenlarına nasıl erişilebilir?
# Liste nasıl parçalanır?

#renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"] #köşeli parantez liste
#print(renkler)
#print(type(renkler))

#print(len(renkler)) #liste uzunluğunu öğrenmek için

#print(renkler[1]) #Siyah sıfırıncı indextir. 1 yazınca bu yüzden beyaz gelir.

#print(renkler[1:4]) #2. indexten başlayıp sonuna kadar yaz demek.
# 1 ile başlar 3. indexe kadar yazar. 4ü kabul etmez

#print(renkler[::2]) #aralıklarla yazdırır.
#print(renkler[1:4:2]) #önce 1. index yazdırır, 2 tane atlayıp 3. indexi yazdırdı.
# daha fazla bir şey olmadığı için durdu.

#append metodu
#insert metodu
#remove metodu
#extend metodu
#pop metodu
#reverse metodu
#sort ve sorted metotları

#print(renkler)
#renkler.append("Gri") #Gri eklenir EN SONUNA

#renkler.insert(0, "Gri") #0. indexe Gri eklenir. ya da kaçıncı indexe eklenmek istenirse
# index kısmına ona göre numara verilir
#renkler.insert(2, "Gri") #2. index kısmına Gri eklenir

#print(renkler)

#renkler.remove("Sarı")
#print(renkler) #Sarı listeden silinir

#renkler2 = ["Turuncu", "Pembe"]
#renkler.extend(renkler2) #Renkler2 elemenlarını eleman olarak ekledi. Listeyi tamamen eklemek yerine elemanlarını ekledi
#renkler.append(renkler2) #Listeyi olduğu gibi diğer listenin sonuna ekler.
#print(renkler)

#renkler3 = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]
#renkler3.pop()
#print(renkler3)
#silinen = renkler3.pop() #pop. sondaki elemanı siliyor.
# aynı şekilde farklı bir değişken içine pop atandığında bize silinen değerin kendisini ekrana yazdırır.
# Silinen elemanı geri kullanmak isterksek başka değişken içine atanır
#print(silinen)

#renkler.reverse() #baştaki olan değerleri başa getirir. eski liste değişir.
# Elemanların yerleri değiştirilmiş farklı bir listeye dönüşür
#print(renkler)

#renkler.sort() #listeyi sıralar alfabetik olarak, sayısal büyülükleri küçükten büyüğe sıralar
#renkler.sort(reverse=True) #sıralamayı alfabatik olrak tersten yapar yine.
#LİSTE ESKİ HALİNİ KAYBEDİP BAŞKA LİSTE OLUR

#liste2 = sorted(renkler)
#print(liste2) #eski liste bozulmasını istemşyorsak sorted

#print(renkler)


# min, max ve in kullanımı
# sum ve kullanımı
# for döngüsü ile listeyi yazdırmak
# enumerate
# listeyi stringe çevirmek ve join metodu
# stringi listeye çevirmek ve split metodu

renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]
sayilar = [1,2,3,4,5,6,7,8]

#print(min(renkler)) #renklerdeki en küçük eleman, alfabetik olarak ilk sırada olan elemanı çeker
#print(min(sayilar)) #sayılardaki en küçük değer çeker
#print(max(sayilar)) #en büyük elemanları çeker
#print(max(renkler))

print(sum(sayilar)) #string oloamazlar

print(list(enumerate(renkler))) #indexlerin numaralarını 0 dan başlayarak yazar

print(list(enumerate(renkler,start=1))) #numaralandımaya 1den başlar

print("Gri" in renkler) #"Siyah" değeri renkler listesinde var mı sorusu. cevap true veya false

stringrenkler = " - ".join(renkler) #birleştirmek, bağlamak anlamında,
# tek bir metin dosyası haline gelir aralarına da "" içinde ne varsa onu koyar
print(type(stringrenkler))

print(stringrenkler)

renkler2 = stringrenkler.split(" - ") #split içine bir karakter değil uzunca birşeyler de alabilir
renkler2 = stringrenkler.split("Ma")  #Ma ile başlayan kısmı ayırır, ekrana yazdırırken vi kısmı görünür
print(renkler2)


