import sqlite3
import time
class kitab:

    def __init__(self,isim,yazar,yayinevi,tur,baski):

        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski

    def __str__(self):

        return "isim : {}\n yazar : {}\n yayinevi : {}\n tur : {}\n baski : {}\n"

class kitabxana:

    def __init__(self):
        self.baglanti_olustur = sqlite3.connect("kutubhane.db")
        self.cursor = self.baglanti_olustur.cursor()


    def baglanti_olustur(self):
        a = "CREATE TABLE kitablar (isim TEXT, yazar TEXT, yazyinevi TEXT, tur TEXT, baski INT)"
        self.cursor.execute(a)
        self.baglanti_olustur.commit()

    def baglanti_kes(self):
        self.baglanti_olustur.close()

    def kitablari_goster(self):

        sorgu2 = "SELECT * FROM kitablar"
        self.cursor.execute(sorgu2)
        kitablar = self.cursor.fetchall()

        if len(kitablar) == 0:
            print("Kitab tapilmadi")

        else:
            for i in kitablar:
                Kitab = kitab(i[0],i[1],i[2],i[3],i[4])
                print(Kitab)

    def kitab_sorgula(self,isim):
        sorgu3 = "SELECT * FROM kitablar where isim = ?"
        self.cursor.execute(sorgu3,(isim,))
        kitablar = self.cursor.fetchall()

        if len(kitablar) == 0:
            print("kitab tapilmadi")

        else:
            Kitab = kitab(kitablar[0][0],kitablar[0][1],kitablar[0][2],kitablar[0][3],kitablar[0][4])

            print(Kitab)

    def kitab_ekle(self,kitab):
        sorgu = "insert into kitablar values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(kitab.isim,kitab.yazar,kitab.yayinevi,kitab.tur,kitab.baski))

        self.baglanti_olustur.commit()

    def kitap_sil(self,isim):

        sorgu = "Delete From kitablar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        self.baglanti_olustur.commit()

    def baski_yukselt(self,isim):

        sorgu = "Select * From kitablar where isim = ?"

        self.cursor.execute(sorgu,(isim,))


        kitablar = self.cursor.fetchall()

        if (len(kitablar) == 0):
            print("Böyle bir kitap bulunmuyor...")
        else:
            baski = kitablar[0][4]

            baski += 1

            sorgu2 = "Update kitaplar set baskı = ? where isim = ?"

            self.cursor.execute(sorgu2,(baski,isim))

            self.baglanti_olustur.commit()

