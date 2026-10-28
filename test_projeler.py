import os
import parola_kontrol
import dosya_butunluk


def test_yaygin_parola_sifir_puan():
    puan, eksikler = parola_kontrol.parola_puani("123456")
    assert puan == 0


def test_guclu_parola_yuksek_puan():
    puan, eksikler = parola_kontrol.parola_puani("Merhaba123!xyz")
    assert puan == 6


def test_kisa_parola_eksik_listesi():
    puan, eksikler = parola_kontrol.parola_puani("abc")
    assert "Şifre en az 8 karakter olmalı" in eksikler


def test_seviye_belirle():
    assert parola_kontrol.seviye_belirle(0) == "Şifre çok zayıf"
    assert parola_kontrol.seviye_belirle(6) == "Çok güçlü"


def test_ayni_icerik_ayni_hash(tmp_path):
    dosya = tmp_path / "a.txt"
    dosya.write_text("merhaba")
    h1 = dosya_butunluk.hash_hesapla(str(dosya))
    h2 = dosya_butunluk.hash_hesapla(str(dosya))
    assert h1 == h2


def test_degisen_icerik_farkli_hash(tmp_path):
    dosya = tmp_path / "a.txt"
    dosya.write_text("merhaba")
    h1 = dosya_butunluk.hash_hesapla(str(dosya))
    dosya.write_text("merhabaa")
    h2 = dosya_butunluk.hash_hesapla(str(dosya))
    assert h1 != h2
    