# if ile kullanılabilecek operatörler
# Eşittir "==", Eşit Değildir "!=", Büyüktür ">", Küçüktür "<" Büyük veya Eşittir ">=" Küçük veya Eşittir "<="
# in anahtar kelimesi
# not anahtar kelimesi
# and ve or bağlaçları
# is anahtar kelmiesi ( Hafızada aynı nesne olmalı)

#if True:
    #print("Koşul doğru")
    #print("Halen if bloğunun içindeyiz")
#if True:
    #print("Koşul doğru")
    #print("Halen if bloğunun içindeyiz")

#a = 10
#a = 5
#b = 7
#b = 5
#if a == b: #false #ikisi de eşit olursa True diyecek
    #print("a == b")

    #if a > b:
        #print("a > b")
#if a != b:
    #print("a != b") #eşit değiller diye yazdırır ekrana

#a = 6
#b = 8

#if a == b:
    #print("a = b")
#else:
    #print("a != b")

#renk = "Siyah"
#if renk == "Beyaz":
    #print("Beyaz")
#elif renk == "Sarı": #eğer öyle değil de böyleyse anlamında. elif her zaman bir koşul yazılmalı.
    #print("Sarı")
#elif renk == "Mavi":
    #print("Mavi")
#else:
    #print("Hiçbiri")

a = 5
b = 8
c = 10
if a < b and b == c: #and doğru olması için bütün her şeyin doğru olması lazım
#if a > b or c == a or b > a: #or ifadesinin sonucunun doğru olabilmesi için ik ifadeden birisinin doğru olması yeterli.
    print("Koşul doğru")
else:
    print("Koşul Yanlış")


j = 8
k = 10
if not j == k: # j == k yanlış bir ifade ama başına not koyarak asslında koşul doğru dedirtmiş oluruz.
    print("Koşul doğru.")
else:
    print("Koşul yanlış.")

isim = "Elif" #küçük e ve büyük E aynı karakterler değiller.
e = "E"
if not e in isim: #not bloğu ile else kısmı yani ikinci satır çalışır.
    print("İsim içerisinde bu harf var.")
else:
    print("İsim içerisinde bu harf yok.")

liste = [1,2,3,4,6,7,8,9]
d = 5
if a in liste:
    print("Listede var")
else:
    print("Listede yok")

E = "Eylul"
Y = "Eylu"
Y += "l"

if E is Y: #eşit olduklarında iki değişkende de Eylul yazıyor demektir.
    # E is Y dediğimizde ise E değişkenler aynı sayılabilir ama aynı değişkenler değiller. Aynı isme sahip değere sahip iki değişken.
    print("E = Y")
else:
    print("E != Y")

X = 56
M = 46
if X is M:
    print("DOĞRU")
else:
    print("YANLIŞ")

    j = 4
    k = 9
    p = 12
    if j > k or p == j or k > j:


