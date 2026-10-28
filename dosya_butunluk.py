import hashlib
import json
import os

def hash_hesapla(dosya_yolu):
    sha256 = hashlib.sha256()

    with open(dosya_yolu,"rb") as dosya:
        while True:
            veri = dosya.read(4096)
            if not veri:
                break
            sha256.update(veri)
    return sha256.hexdigest()

KAYIT_DOSYASI = "hashler.json"

def hash_kaydet(dosya_yolu):
    hash_degeri = hash_hesapla(dosya_yolu)
    if os.path.exists(KAYIT_DOSYASI):
        with open (KAYIT_DOSYASI,"r",encoding="utf-8") as f:
            kayitlar = json.load(f)
    else:
        kayitlar = {}
    kayitlar[dosya_yolu] = hash_degeri
    with open(KAYIT_DOSYASI,"w",encoding="utf-8") as f:
        json.dump(kayitlar,f,indent=4)

    print(f"Kaydedildi: {dosya_yolu}")
    print(f"hash: {hash_degeri}")

def hash_kontrol(dosya_yolu):
    if not os.path.exists(KAYIT_DOSYASI):
        print("Henüz kayıt yok. Önce bir dosya kaydetmelisin.")
        return

    with open(KAYIT_DOSYASI, "r", encoding="utf-8") as f:
        kayitlar = json.load(f)

    if dosya_yolu not in kayitlar:
        print("Bu dosya için kayıtlı bir hash yok.")
        return

    eski_hash = kayitlar[dosya_yolu]
    yeni_hash = hash_hesapla(dosya_yolu)

    if eski_hash == yeni_hash:
        print("Dosya DEĞİŞMEMİŞ. Bütünlük doğrulandı.")
    else:
        print("UYARI: Dosya DEĞİŞMİŞ!")
        print(f"Kayıtlı hash: {eski_hash}")
        print(f"Şimdiki hash: {yeni_hash}")

def main():
    print("=== Dosya Bütünlük Kontrolcüsü ===")
    print("1) Dosyanın hash'ini kaydet")
    print("2) Dosyanın değişip değişmediğini kontrol et")

    secim = input("Seçiminiz (1/2): ")
    dosya_yolu = input("Dosya adı: ")

    if not os.path.exists(dosya_yolu):
        print("Böyle bir dosya bulunamadı.")
        return

    if secim == "1":
        hash_kaydet(dosya_yolu)
    elif secim == "2":
        hash_kontrol(dosya_yolu)
    else:
        print("Geçersiz seçim.")


if __name__ == "__main__":
    main()