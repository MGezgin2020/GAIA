# # Karar mekanizmaları (Desicions)
# number = int(input("Sayı: "))
#
# sonuc = number % 2 #Burada number değişkeni üzerinde tutulan tam sayının 2'ye bölümünden kalanı sonuç değişkenine atadık
# if sonuc== 0 :  #programlama dillerinde == karşılaştırma operatörüdür
#     print(f"{number} çifttir")
# else :
#     print(f"{number} tektir")

# Kullanıcıdan bir sayı alıp bu sayı pozitif mi negstif mi yoksa nötr mü onu bildirsin
# x= int (input("Sayı:"))
# if x>0 :
#     print (f'{x} pozitif')
# elif x<0 :
#     print(f'{x} negatif')
# else :
#     print(f'{x} nötr')
#Kullanıcıdan mevsim bilgisi alıp, gelen mevsime göre ayları yazın
# x =(input("bana mevsimi söyleyin size aylarını söyleyeyim : "))
# if x == "Kış":
#     print ("Aralık,Ocak,Şubat")
# elif x == "İlkbahar" :
#     print ("Mart,Nisan,Mayıs")
# elif x== "Yaz":
#     print ("Haziran, Temmuz, Ağustos")
# else :
#     print ("Eylül, Ekim ,Kasım")
    # Kullanıcıdan 2 adet sayı alalım , büyük olanı ekrana yazdıralım
# x = input("ilk rakamı giriniz :")
# y = input("ikinci rakamı giriniz :")
# if x<y :
#     print (y)
# elif y<x :
#     print (x)
# else:
# #     print ("x ve y birbirine eşit")
# mevsim = input ("mevsim : ").lower()
# match mevsim:
#     case "kış" :
#         print("Aralık-Ocak-Şubat")
#     case "ilkbahar" :
#         print("Mart-Nisan-Mayıs")
#     case "sonbahar" :
#         print("Eylül-Ekim-Kasım")
#     case _ :
#         print("Ağustos-Temmuz-Haziran")
# Kullanıcıdan 3 adet sayı alıp en büyük sayıyı veren uygulamayı yazalım
# x = int(input("bir tam sayı giriniz:"))
# y = int(input("bir tam sayı giriniz:"))
# z = int(input("bir tam sayı giriniz:"))
# if x > y and x > z:
#     print(f"En büyük sayı {x}")
# elif y > x and y > z:
#     print(f"En büyük sayı {y}")
# elif z > x and z > y:
#     print(f"En büyük sayı {z}")
# else:
#     print("Sayılardan bazıları birbirine eşit")
# Kullanıcıdan bir adet ürün bilgisi alacağız, ürün elma, muz, ıspanak ise sebze reyonuna gidiniz, eğer notebook, tablet, smart_phone ise teknoloji reyonuna gidiniz , eğer şampuan, sabun, parfüm ise kozmatik reyonuna gidiniz diye feed-back veren uygulama

# urun = int(input("aradığınız ürün hangisi ? Numarasını giriniz : 1)elma, 2)muz, 3) ıspanak 4)notebook, 5)tablet, 6)smart_phone ,7)şampuan, 8)sabun, 9)parfüm" : ))
# if urun==1 or urun==2 or urun==3 :
#     print ("meyve-sebze reyonuna gidiniz")
# elif urun==4 or urun==5 or urun==6:
#     print ("meyve-sebze reyonuna gidiniz")
# elif urun==7 or urun==8 or urun==9:
#     print("kozmetik reyonuna gidiniz")
# else:
#     print ("ürün bizde yok bildirirseniz alınması için ne yapılabilir bakabiliriz")
# kullanıcıdan password ve user_name alalım ; eğer username "beast", sifre "123" ise giriş yapabilsin, sonra boy ve kilosunu alıp body mass indeksini hesaplayalım.. aralıklar vardı.. onu bildirin BMI
#BMI (Vücut Kitle İndeksi) derecelendirmesi şu şekilde yapılır:

#18,5 ve altı: Zayıf. 35
#18,5 - 24,9: Normal kilolu. 35
#25,0 - 29,9: Fazla kilolu. 35
#30,0 - 34,9: Obez (1. derece obezite). 35
#35,0 - 39,9: Aşırı obez (2. derece obezite). 35
#40 ve üstü: Morbid obez (3. derece obezite). 5
# user_name=input("user name giriniz : ")
# password=input("password giriniz: ")
# if user_name=="beast" and password=="123" :
#     print("Hoşgeldiniz, acaba bugün BMI skalasında nerdesiniz ? ")
#     kilo=float(input ("lütfen kilonuzu giriniz:"))
#     boy=float(input("lütfen boyunuzu cm cinsinden giriniz"))
#     BMI=kilo/boy/100**2
#
#     if 0< BMI <= 18.5:
#         print ("Zayıfsınız")
#     elif 24.9> BMI >18.5:
#         print("Normal kilolusunuz")
#     elif 30 < BMI < 34.9:
#         print ("Maalesef 1. derece obezsiniz")
#     elif BMI>35 and BMI<39.9:
#         print ("Maalesef 2. derece obezsiniz")
#     elif BMI>40 :
#         print ("Maalesef 3. derece obezsiniz")
# else :
#     print("hatalı password ya da user_name")
# try-except-finally
# try :
#     bolen = int(input("Bolen:"))
#     bolunen = int(input("Bolunen"))
#
#     sonuc=bolunen/bolen
# # err genel kabul gören bir kelime , hata örnekleri bir yerde listeli..
#     print(f"Sonuç {sonuc}")
# except ZeroDivisionError as err :
#         print(err)
#         print ("tam sayılar sıfıra bölünemez")
# # try da çalışsa, except de çalışsa finally çalışır
# finally :
#         print ("Bağlantı kapatılıyor ! ")
try :
    age=int(input("Age:"))
    print(f"Age: {age}")
except ValueError as err :
    print ("tekrar dener misiniz ? rakam harici bir şey girdiniz..")
except ZeroDivisionError as err :
    print (err)
except :
    print("Python içinde kayıtlı bütün hataları check eder; ama sistemden yer.. python bütün hataları hepsini tek tek kontrol eder.. pek optimal değil")
else :
    print ("except bloğu tetiklenmezse else bloğu çalışır , try çalışıyor, except çalışıyor")











