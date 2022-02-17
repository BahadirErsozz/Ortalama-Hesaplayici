ogrenci_no = input("Okunacak dosya ismini giriniz: ")
# Harf notlarinin 4'luk sistemdeki karsiliklarini gostermektedir. Eger notlandirma sisteminiz farkli ise assagidan degistirebilirsiniz.
gecerli_not_listesi = {"AA": 4, "BA": 3.5, "BB": 3, "CB": 2.5, "CC": 2, "DC": 1.5, "DD": 1, "DF": 0.5, "FF": 0}
# Program sadece listedeki dersler icin calisiyor. Assagiya ders ek0leyebilirsiniz(kac kredi oldugunu assagiya yazmayi unutmayin).
ders_listesi = ["BİL103", "BİL113", "MAT101", "FİZ101", "FİZ101L", "TÜR101", "İNG001", "BİL211", "BİL132", "MAT102", "FİZ102", "FİZ102L", "TÜR102", "İNG002", "BİL133", "BİL212", "BİL265", "BİL245", "AİT201", "İNG003", "BİL214", "BİL334", "BİL361", "İKT105", "OEG101", "AİT202", "İNG004", "BİL331", "BİL395", "BİL481", "BİL345", "UGİ315", "İYD1", "BİL372", "BİL372", "BİL461", "BilimSD", "BSD1", "İYD2", "BİL452", "BİL495", "FSD", "BSD2", "BSD3", "İYD3", "BİL496", "BSD4", "BSD5", "ÜSD", "İYD4"]
olan_dersler = []
notlar = {}
toplam_ders_kredisi = 0
not_toplam = 0
z = 1
hata_yok = True
# Ders ekledikten sonra kac kredi oldugunu da yazmak gerekmektedir.
ders_kredileri = {"BİL103": 2, "BİL113": 4, "MAT101": 4, "FİZ101": 3, "FİZ101L": 1, "TÜR101": 2, "İNG001": 2, "BİL211": 4, "BİL132": 3, "MAT102": 4, "FİZ102": 3, "FİZ102L": 1, "TÜR102": 2, "İNG002": 2, "BİL133": 3, "BİL212": 4, "BİL265": 4, "BİL245": 4, "AİT201": 2, "İNG003": 2, "BİL214": 4, "BİL334": 3, "BİL361": 3, "İKT105": 3, "OEG101": 1, "AİT202": 2, "İNG004": 2, "BİL331": 3, "BİL395": 3, "BİL481": 3, "BİL345": 3, "UGİ315": 2, "İYD1": 3, "BİL372": 4, "BİL461": 3, "BilimSD": 3, "BSD1": 3, "İYD2": 3, "BİL452": 3, "BİL495": 1, "FSD": 3, "BSD2": 3, "BSD3": 3, "İYD3": 3, "BİL496": 4, "BSD4": 3, "BSD5": 3, "ÜSD": 3, "İYD4": 3}
try:
    f = open(ogrenci_no + ".txt", "r", encoding="utf-8")
    for a in f:
        if a[0:len(a)-4] in ders_listesi:
            notlar[a[0:len(a)-4]] = a[len(a) - 3:len(a) - 1]
            olan_dersler.append([a[0:len(a)-4]])
        elif a[0:len(a) - 4] not in ders_listesi:
            print("Geçersiz bir ders bulundu!")
            z = 0
            hata_yok = False
            exit()
    f.close()

except:
    if z == 1:
        print("Geçersiz dosya ismi")
        hata_yok = False
        exit()

for x in notlar:
    if notlar[x] in gecerli_not_listesi:
        not_toplam += gecerli_not_listesi[notlar[x]] * ders_kredileri[x]
    elif notlar[x] not in gecerli_not_listesi:
        print("Geçersiz bir not bulundu!")
        hata_yok = False
        exit()
    toplam_ders_kredisi += ders_kredileri[x]

if hata_yok:    # == True çıkardım
    ano = not_toplam / toplam_ders_kredisi
    print("Hesaplanan not ortalamanız: " + str(ano)[0:4] + "(4 üzerinden) " + str(ano * 25)[0:4] + "(100 üzerinden)")
