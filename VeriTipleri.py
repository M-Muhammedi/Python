
# Değişkenler
name = "Mustafa"  # String (metin)
mesej = """buda string tipidir
ama yazdığınızı olduğu gibi yazdırır       
örneği satırlar boşluklar gibi...
 """                                   # Çoğuklu metin
age = 24        # Integer (tamsayı)
height = 1.72   # Float (ondalık sayı)
is_student = True  # Boolean (doğru/yanlış)

print(name)
print(mesej)
print(age)
print(height)
print(is_student)

                                    # Veri Tip dünüşümları
namber1 = 25  # Integer
print(type(namber1))  # Veri tipine gösterir
print(namber1)  # print ile yazdırır

StrNamber1 = str(namber1)  # Integer'e String'e çevriyor
print(type(StrNamber1))
print(StrNamber1)

namber2 = 30   # Integer
print(type(namber2))
print(namber2)

FloatNamber2 = float(namber2)  # Integer'e Float'e Çeviriyor.
print(type(FloatNamber2))
print(FloatNamber2)

# int()           Integer'e çevirir
# str()           String'e çevirir
# float()         Float'e çevirir
# bool()          Boolean' çevirir