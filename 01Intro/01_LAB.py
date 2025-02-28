# from operator import truediv
#
# # Comment Line (Yorum satırı)
# # Bu satırlar IDE tarafından çalıştırılmazlar
#
# # Değişken (Variable)
# x = 10
# print (x)  #built-in fonksiyon
# # Değişken tipleri
# # Tam sayılar için integer
# x = 10
# # Ondalıklı sayılar için Float
# y=12.2
# # Sözel ifadeler için string
# first_name = "Burak"
# # Mantıksal değişkenler için boolean - true false
# is_active = True
# is_passive = False
# z = 120
# print (z)
# z = "Mike Tyson"
# print (z)
# z = True
# print (z)
# print(type(z))
# x=5
# y=10
# toplam=x+y
# print(toplam)
# Kullanıcıdan 2 tane tam sayı alın ve bu sayıları toplayan programı yazınız
# Kullanıcıdan bir input aldığımızda bize gelen değerin tip her zamn stringdir.
# x = int(input("bir tam sayı giriniz:"))
# y = int(input("bir tam sayı giriniz:"))
# toplam = x+y
# print (toplam)
#
# KArenin çevresini ve alanını hesaplayan uygulama
# a=int(input("kenar : "))
# alan=a*a
# cevre=4*a
# print("bu karenin alanı :", alan )
# print(f"Cevre:{cevre}")
# print("Cevre:{}".format(cevre))
# # dikdortgen çevre ve alanı hesaplamak
# kisa_kenar=int(input("Kisa kenar:"))
# uzun_kenar=int(input("Uzun kenar:"))
# alan=kisa_kenar*uzun_kenar
# cevre=2*(kisa_kenar+uzun_kenar)
# print(f'Alan:{alan}\n'
#       f"Çevre:{cevre}")
#üçgenin alanını hesaplamak
taban=float(input("Taban: "))
yukseklik=float(input("Yükseklik:"))
print(f"Alan: {taban*yukseklik/2}")  #çıkan bilgi bir yerde kullanılmayacağı için direkt print içinde hesaplattık

