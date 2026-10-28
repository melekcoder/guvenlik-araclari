YAYGIN_PAROLALAR = {
    "123456", "12345678", "123456789", "password", "qwerty",
    "111111", "123123", "abc123", "iloveyou", "admin",
    "welcome", "sifre", "parola", "123456a",
    "fenerbahce", "galatasaray", "besiktas", "trabzonspor",
}
def parola_puani(parola):
    puan = 0
    eksikler = []

    if parola.lower() in YAYGIN_PAROLALAR:
        return 0, ["Bu parola kolayca tahmin edilebilecek bir parola"]

    if len(parola) >= 8:
        puan += 1
    else:
        eksikler.append("Şifre en az 8 karakter olmalı")

    if len(parola) >= 12:
        puan += 1
    else:
        eksikler.append("12 ve üzeri karakter sayısı daha güvenli")

    if any(k.islower() for k in parola):
        puan += 1
    else:
        eksikler.append("Küçük harf eklenmelidir")

    if any(k.isupper() for k in parola):
        puan += 1
    else:
        eksikler.append("Büyük harf eklenmelidir")

    if any(k.isdigit() for k in parola):
        puan += 1
    else:
        eksikler.append("Rakam eklenmelidir")

    if any(not k.isalnum() for k in parola):
        puan += 1
    else:
        eksikler.append("Sembol eklenmelidir (!, @, ?, #)")

    return puan, eksikler
def seviye_belirle(puan):
    if puan <= 1:
        return "Şifre çok zayıf"
    elif puan == 2:
        return "Şifre zayıf"
    elif puan == 3:
        return "Şifre orta seviyededir"
    elif puan == 4:
        return "Şifre iyi"
    elif puan == 5:
        return "Şifre güçlü"
    else:
        return "Çok güçlü"

def main():
    print("Parola Gücü Kontrolcüsü")
    parola = input("Parolanızı girin: ")

    puan, eksikler = parola_puani(parola)
    seviye =seviye_belirle(puan)

    print(f"\nPuan: {puan}/6")
    print(f"Seviye: {seviye}")

    if eksikler:
        print("\nİyileştirme önerileri:")
        for eksik in eksikler:
            print (f"-{eksik}")
    
if __name__ == "__main__":
    main()