# Sözlük Nedir?
# Sözlük nasıl oluşur?
# Sözlük nasıl yazdırılır?
# Sözlükte verilere nasıl erişilir?
# Sözlükte veriler nasıl değiştirilir?
# Sözlükte birden fazla alan nasıl değiştirilir?
# Sözlükten bir alan nasıl silinir?
# keys ve values ve items metotları
# Sözlüğü for döngüsü yardımıyla nasıl yazdırabiliriz?
#"isim" : "ali", "yas" : 20, "cinsiyet" : "m" , "hobiler" : ["Sinema", "Konser", "Yazılım"]
# ilk değerler anahtar ikinciler yani kelimelerin anlamları da valueler olur

kisi = {"isim" : "ali", "yas" : 20, "cinsiyet" : "m" , "hobiler" : ["Sinema", "Konser", "Yazılım"]}
#int veya string ilk anahtar

print(kisi["isim"]) #buraya anahtarları yazarız, ve anahtarın anlamına karşılık gelen valueyi ekrana yazdırır.
print(kisi["cinsiyet"])
print(kisi["hobiler"])

print(kisi)
kisi["isim"] = "Elif" #sözlükteki elemanları değiştirir
#kisi sözlüğündeki "isim" anahtarına ulaştım, isim içerisindeki valueya "Elif" değerini atayacağım demek oluyor bu kod.

#print(kisi)

kisi.update({"yas" : 19, "cinsiyet" : "female"}) #birden fazla sözlükteki valueleri değiştirmek için .update

kisi["id"] = 12345 #"id" sözlüğe eklendi
print(kisi)
del kisi["id"] #sözlük içindeki "id" alanı silindi del ile
print(kisi)

for x in kisi:
    #print(x) #sözlük içindeki anahtarları yazdırdı
    print(kisi[x]) #x ilk önce isim oldu, isim anahtarının değerini yazdı. sonra yaşa karşılık gelen değeri yazdırdı.
    print(kisi.keys()) #anahtarlardan oluşan bir liste oluşturdu .keys()
    print(kisi.values()) #anahtarlar içindeki valueleri sıralar
    print(kisi.items()) #hem ikili ikili isim ali yas 20 gibi. hem anahtar hem içindeki valular

    for k,v in kisi.items():
        print(k) #k yazılırsa sadece keyleri yani anahtarları, v valuelar anahtarlar içindeki değerler.
        # k,v yazılırsa ikili ikili yazdırır

        #print(kisi["id"]) #sözlükte "id" yok ve KeyError verir.
        #print(kisi.get("id", "Bulunamadı")) #hiç bulunmadığı için None yazdırır. Aradığımız anahtar sözlükte yoksa, ikinci parametre ekrana yazılacak olan mesajdır.
        print(kisi.get("isim"))
