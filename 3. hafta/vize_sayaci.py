from datetime import datetime

tarih_giris = input("Sınav tarihini ve saatini girin (GG.AA.YYYY SS:DD): ")
sinav_tarihi = datetime.strptime(tarih_giris, "%d.%m.%Y %H:%M")
simdi = datetime.now()

kalan_sure = sinav_tarihi - simdi
gun = kalan_sure.days
saat = kalan_sure.seconds // 3600

print(f"Sınava {gun} gün ve {saat} saat kaldı.")
