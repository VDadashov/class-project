from book import*

print("""***********************************

Kütüphane Programına Hoşgeldiniz.

İşlemler;

1. Kitapları Göster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil 

5. Baskı Yükselt

Çıkmak için 'q' ya basın.
***********************************""")

kitabxana1 = kitabxana()


while True:
    islem = input("Yapacağınız İşlem:")

    if (islem == "q"):
        print("Program Sonlandırılıyor.....")
        print("Yine bekleriz....")
        break
    elif (islem == "1"):
        kitabxana.kitablari_goster()

    elif (islem == "2"):
        isim = input("Hangi kitabı istiyorsunuz ? ")
        print("Kitap Sorgulanıyor...")
        time.sleep(2)

        kitabxana.kitab_sorgula(isim)

    elif (islem == "3"):
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayinevi = input("Yayınevi:")
        tur = input("Tür:")
        baskı = int(input("Baskı"))

        yeni_kitap = kitab(isim,yazar,yayinevi,tur,baskı)

        print("Kitap ekleniyor....")
        time.sleep(2)

        kitabxana.kitab_ekle(yeni_kitap)
        print("Kitap Eklendi....")


    elif (islem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunuz ?")

        cevap = input("Emin misiniz ? (E/H)")
        if (cevap == "E"):
            print("Kitap Siliniyor...")
            time.sleep(2)
            kitabxana.kitap_sil(isim)
            print("Kitap silindi....")


    elif (islem == "5"):
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz ?")
        print("Baskı yükseltiliyor....")
        time.sleep(2)
        kitabxana.baski_yukselt(isim)
        print("Baskı yükseltildi....")

    else:
        print("Geçersiz İşlem...")
