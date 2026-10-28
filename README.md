# Güvenlik Araçları Projesi

Bu proje, Python dersi için hazırladığım iki küçük güvenlik programını içeriyor.
Bu programları tek bir menüden çalıştırabiliyorum.

## Programlar

**1. Parola Gücü Kontrolcüsü** (`parola_kontrol.py`)
Girilen parolaya 0-6 arası puan veriyor ve parolanın neden zayıf olduğunu söylüyor.
Uzunluğa, büyük/küçük harfe, rakama ve sembole bakıyor. Çok yaygın parolalar
(123456, password gibi) direkt 0 puan alıyor.

**2. Dosya Bütünlük Kontrolcüsü** (`dosya_butunluk.py`)
Bir dosyanın SHA-256 hash'ini hesaplayıp `hashler.json` dosyasına kaydediyor.
Sonra tekrar kontrol edince dosyanın değişip değişmediğini söylüyor.

## Nasıl çalıştırılır?

Bilgisayarda Python yüklü olmalı. Terminale şunu yazın:

```
python ana_menu.py
```

## Testler

```
pip install pytest
python -m pytest
```

## Dosyalar

- `ana_menu.py`: iki programı birleştiren menü
- `parola_kontrol.py`: parola gücü kontrolcüsü
- `dosya_butunluk.py`: dosya bütünlük kontrolcüsü
- `test_projeler.py`: testler

## Eksikler

- `aaaa` ya da `1234` gibi tekrar eden/ardışık karakterler için ayrıca ceza yok.
- Yaygın parola listesi kısa, gerçek listeler çok daha büyük.
