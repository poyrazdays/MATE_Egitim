while True:
    try:
        sayi = int(input("Bir sayı giriniz: "))
        print("Girdiğiniz sayı:", sayi)
        break
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz")
