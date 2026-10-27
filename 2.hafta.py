# Kullanıcıdan ad, soyad ve şehir bilgilerini alıp bunları düzenli bir cümle halinde ekrana yazdıran bir kod #

ad = input("Adınız: ")
soyad = input("Soyadınız: ")
sehir = input("Şehriniz: ")

print(f"Ad: {ad}, Soyad: {soyad}, Şehir: {sehir}")

# Kullanıcıdan fiyatsız tutar ve indirim yüzdesi alarak indirim tutarı ile son fiyatı hesaplayan bir indirim_hesapla()fonksiyonu #

def indirim_hesapla():
    fiyat = float(input("Fiyat: "))
    indirim_yuzdesi = float(input("İndirim Yüzdesi (%): "))
    
    indirim_tutari = fiyat * (indirim_yuzdesi / 100)
    son_fiyat = fiyat - indirim_tutari
    
    return indirim_tutari, son_fiyat

indirim, odenecek_tutar = indirim_hesapla()

print(f"İndirim Tutarı: {indirim:.2f} TL")
print(f"Ödenecek Son Fiyat: {odenecek_tutar:.2f} TL")

# Kullanıcıdan doğum yılını alıp mevcut yıla (2026) göre yaşını hesaplayan ve ehliyet alıp alamayacağını belirten koşullu yapı #

dogum_yili = int(input("Doğum yılınızı girin: "))
mevcut_yil = 2026

yas = mevcut_yil - dogum_yili

print(f"Yaşınız: {yas}")


if yas >= 18:
    print("Tebrikler, ehliyet alabilirsiniz.")
elif yas > 0:
    kalan_yil = 18 - yas
    print(f"Ehliyet alamazsınız. Ehliyet alabilmek için {kalan_yil} yıl daha beklemelisiniz.")
else:
    print("Geçersiz bir doğum yılı girdiniz.")

#Vize (%40) ve final (%60) notlarına göre ortalama ve harf notunu hesaplayan bir harf_notu_hesapla() fonksiyon #

def harf_notu_hesapla(vize, final):
    # Ağırlıklı ortalama hesabı
    ortalama = (vize * 0.40) + (final * 0.60)
    
    # Harf notu aralıkları
    if ortalama >= 90:
        harf = "AA"
    elif ortalama >= 80:
        harf = "BA"
    elif ortalama >= 70:
        harf = "BB"
    elif ortalama >= 60:
        harf = "CB"
    elif ortalama >= 50:
        harf = "CC"
    elif ortalama >= 45:
        harf = "DC"
    elif ortalama >= 40:
        harf = "DD"
    else:
        harf = "FF"
        
    return ortalama, harf

vize_notu = float(input("Vize notunuzu girin: "))
final_notu = float(input("Final notunuzu girin: "))

ort, harf = harf_notu_hesapla(vize_notu, final_notu)

print(f"Dönem Ortalamanız: {ort:.2f}")
print(f"Harf Notunuz: {harf}")
