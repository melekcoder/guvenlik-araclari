import parola_kontrol
import dosya_butunluk


def menu():
    while True:
        print("\n=== GÜVENLİK ARAÇLARI ===")
        print("1) Parola gücü kontrolcüsü")
        print("2) Dosya bütünlük kontrolcüsü")
        print("0) Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            parola_kontrol.main()
        elif secim == "2":
            dosya_butunluk.main()
        elif secim == "0":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")


if __name__ == "__main__":
    menu()