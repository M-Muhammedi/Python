

# Kişisel bilgiler
def bilgi(isim:str,soyisim:str,yas:int):
    return print(f"Adınız : {isim} \nSoyAdınız : {soyisim} \nYaşınız : {yas}")


kisi1 = bilgi("Mustafa","Muhammedi",24)
print(kisi1)

#       Şuanki Yıl
def yil():
    import datetime
    return datetime.datetime.now().year


#  Ysş hesaplama Yıl Fonksiyonu kullanarak
def YasHesaplama(dogumYil):
    return yil()-dogumYil

print(YasHesaplama(2000))

#  Selamlama
def selamlama(isim,msj= "Merhaba"):
    return f"{msj} {isim}"

print(selamlama("Mustafa"))

print(selamlama("Mustafa","Hoşgeldin"))
