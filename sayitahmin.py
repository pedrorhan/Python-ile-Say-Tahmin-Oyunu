import random

def sayiTahmin(random_sayi):
    deneme_sayisi = 0  # Deneme sayısını tutmak için sayaç
    while True:
        sayi = int(input("Bir sayı girin: "))
        deneme_sayisi += 1  # Her tahminde sayaç artırılır
        if sayi == random_sayi:
            print(f"Tebrikler! Sayıyı doğru bildiniz. {deneme_sayisi} denemede buldunuz.")
            break  # Doğru tahmin edildiğinde döngüden çık
        elif sayi > random_sayi:
            print("Daha küçük bir sayı girin.")
        elif sayi < random_sayi:
            print("Daha büyük bir sayı girin.")

while True:
    # Her yeni oyun için yeni bir rastgele sayı oluştur
    random_sayi = random.randint(1, 100)
    print("Yeni bir sayı belirlendi. Hadi tahmin edelim!")
    sayiTahmin(random_sayi)

    kontrol = input("Yeni oyun için 'e' basın. Çıkmak için herhangi bir tuşa basın... ")
    if kontrol.lower() != 'e':
        print("Oyun bitti.")
        break
