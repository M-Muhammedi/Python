#                                Sınavı Ortalama Hesaplama Uygulaması
# Kullancıdan değer alma
VizeNotu = int(input("Vize Notu Giriniz : "))
FinalNotu = int(input("Final Notu Giriniz : "))

# girilen puanları Matematiksel Hesaplama
Ortalama = (VizeNotu*0.4)+(FinalNotu*0.6)


if Ortalama > 50 :
    print("Tebrikler Geçtiniz. "+ str(Ortalama))

elif Ortalama < 50 :
    print("Kaldınız Daha Fazla Caba Göstermelisiniz. "+ str(Ortalama))


#         Hava Durumu Ugulaması
Gunusli = True
Bulutlu = False

if Gunusli:
    print("Hava Güneşli  Güneş Gözlüğüne Al.")

elif Bulutlu:
    print("Hava Bulutlu Montune Giy.")

else:
    print("Hava Yarım Bulutlu.")