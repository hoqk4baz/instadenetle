#------------- KÜTÜPHANELER -------------#
from instagrapi import Client
import os
import time, sys, pwinput




                    

    

#--------------- GİRİŞ ------------------#
if os.path.isfile('giriskayit.txt'):
    with open('giriskayit.txt', 'r') as r:
        data = r.readlines()
        k_adi = str(data[0])
        sifre = data[1]

else:
    k_adi = input('Kullanıcı ADI: ')
    sifre = pwinput.pwinput(prompt='Şifre : ')
    with open('giriskayit.txt', 'w') as a:
        a.write(k_adi + '\n' + sifre)

#------------ EKSTRALAR -----------#
def havali(parametre, time_sleep = 0.04):
    soz=[]
    for i in parametre+"\n":
        soz.append(i)
        time.sleep(time_sleep)
        sys.stdout.write(str(soz[0]))
        sys.stdout.flush()
        soz.remove(i)


def bekle():
    say = 0
    karakter = ["\\", "|", "/", "-"]

    while True:
        if say == 11: break


        for i in range(0, 4):
            sys.stdout.write('---- GİRİŞ YAPILIYOR ----' +karakter[i]+" \r")
            sys.stdout.flush()
            time.sleep(0.1)
        say += 1



yazi1=('----- GİRİŞ BAŞARILI----')
if __name__ == "__main__":
    bekle()
    dark = Client() 
    dark.login(k_adi, sifre)
    havali(yazi1, 0.05)
    time.sleep(2)


#---------- GÖNDERİDEN KULLANICILARI ÇEKME ------#
url = input("Gönderi Url gir : ")
populer_photo_id = dark.media_pk_from_url(url)
print(f"Gönderi ID : {populer_photo_id}") 
begenenler = dark.media_info(populer_photo_id).dict()
likes = begenenler['like_count']
#havali("------ GÖNDERİYİ BEĞENENLER LİSTELENİYOR ---", 0.05)
#time.sleep(3)
likers_res = dark.media_likers(populer_photo_id)

#--------------------- LİSTELEME ----------------------#

begeni_list = []
count = 0
for object in likers_res:
    begeni_list.append(object.username)
    begeni_list = open("begenenler.txt", "a+")
    begeni_list.write("\n")
    begeni_list.close()
    count = count + 1
#--------------- LİSTELEME SONU --------------#

#---------- TAKİP EDİLENLERİ ÇEKME -----------#
#havali("------- TAKİP ETTİKLERİN GETİRİLİYOR ------", 0.05)
#time.sleep(3)
takip_edilenler = dark.user_following_v1(dark.user_id)

#------------ LİSTELEM ----------#
begeni_list2 = []
count = 0
for object in takip_edilenler:
    begeni_list2.append(object.username)
    begeni_list2 = open("kullanıcılar.txt", "a+")
    begeni_list2.write("\n")
    begeni_list2.close()
    count = count + 1
#----------- LİSTELEME SONU ------#

#----------- KARŞILAŞTIRMA -------#
with open("begenenler.txt") as dosya1:
    with open("kullanıcılar.txt") as dosya2:
        krs = set(dosya1).intersection(dosya2)
        krs.discard('\n')

        havali("--- KARŞILAŞTIRMA SONUCU --- ", 0.05)
        havali("    -Beğenenler Listelendi", 0.03)
        havali("    -Takip Ettiklerin Listelendi", 0.03)
        havali("    -Karşılaştırma Yapılıyor...", 0.03)
        havali("LİSTE GETİRİLİYOR.....", 0.05)

with open('karşılaştır.txt', 'w') as cikis:
    for line in krs:
        cikis.write(line)
        time.sleep(1)
        print(line)
havali("BUNLAR TAKİP ETTİĞİN KİŞİLER ARASINDA PAYLAŞTIĞIN POSTU BEĞENENLER")

