import random

tutulan_sayi = random.randint(1, 100)

while True:
    tahmin = int(input("1 ile 100 arasında tahmininizi girin: "))

    if tahmin < tutulan_sayi:
        print("Yukarı çık")
    elif tahmin > tutulan_sayi:
        print("Aşağı in")
    else:
        print("Tebrikler, doğru tahmin!")
        break
