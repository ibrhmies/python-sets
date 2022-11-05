#sets -> indexlenemez,sıralanamaz

arabalar = { "opel","honda","bmw","Audi"}
telefonlar = { "iphone","samsung","huawei"}

sonuc = arabalar
#sonuc = arabalar[0] indexlenemez

print(sonuc)
# sets liste tipinde yazdığımız sırayla aynı sonuc verilmez sets liste tipinde sıra ve index numarası önemli değildir.

for x in arabalar:
    print(x)

#-> for komutuyla listedeki elemanları yazdırabiliriz sets liste tipinde de.

sonuc = "opel" in arabalar
print(sonuc)  
#sets liste tipinde içindeki elemanları sorgulama yapılabilir.

arabalar.add("Togg")

print(arabalar)
#-> add komutuyla sets liste tipine eleman ekleyebiliriz.

arabalar.remove("opel") #-> discard komutuyla da aynı işlemi yapabiliriz.
print(arabalar)
#-> remove komutuyla sets liste tipinde istediğimiz elemanı silebiliriz.

sonuc = arabalar.union(telefonlar)
print(sonuc)
#-> union komutuyla 2 farklı sets liste tipindeki listeyi birleştirebiliriz.


