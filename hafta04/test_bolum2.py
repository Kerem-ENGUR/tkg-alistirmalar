# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v

import pytest

from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim


def test_kisa_sifre_zayif():
    assert sifre_gucu("abc") == "zayıf"
    assert sifre_gucu("kerokerokero") == "güçlü"
    assert sifre_gucu("kerokeroker") == "orta"


def test_otopark_ucreti():
    assert otopark_ucreti(14) == 0
    assert otopark_ucreti(15) == 0
    assert otopark_ucreti(59) == 20
    assert otopark_ucreti(60) == 20
    assert otopark_ucreti(179) == 40
    assert otopark_ucreti(180) == 40
    assert otopark_ucreti(200) == 60

def test_yuzde_degisim():
    assert yuzde_degisim(200, 250) == 25.0
    assert yuzde_degisim(100, 200) == 100.0
    assert yuzde_degisim(200, 150) == -25.0
    assert yuzde_degisim(100, 0) == -100.0
    assert yuzde_degisim(100, 100) == 0.0