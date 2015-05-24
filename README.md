# pardusAyar2.0
Pardus ARM Topluluk için Kontrol Paneli

Pardus Ayar 2.0
===========

Özellikler
--------
- Hostname bilgisi
- Kernel sürüm bilgisi
- Lokal IP bilgisi
- SSH durum kontrolu
- HTTP durum kontrolu (lighttpd)
- FTP durum kontrolu (vsftpd)


Bu proje Pardus Topluluk Sürümü'nde ARM ekibinde geliştirdiğimiz
işletim sistemi için basit bir kontrol paneli sunmaktadır.


Ekran Görüntüleri
-----------


Ana Ekran
~~~~~~
.. image:: https://raw.githubusercontent.com/iscalik/iscalik.github.io/master/pardusAyar2/0.png?token=AFkGKeY542x4ZAYHXbI1S9rebNoXTNHZks5Va0GrwA%3D%3D

Ana ekrandaki butonlar ile bilgi ve SSH, HTTP Sunucu, FTP Sunucu kontrolü sağlanabilir.

Hakkımızda
~~~~~~~~~~~~~~~
.. image:: https://raw.githubusercontent.com/iscalik/iscalik.github.io/master/pardusAyar2/1.png?token=AFkGKXFECoeoHWCtwWK3HSMLRgG8DOSCks5Va0HAwA%3D%3D

İsmet Said Çalık <ismetsaid.calik@pardus.net.tr>
Mehmet Nuri Öztürk <mehmetnuri.ozturk@pardus.net.tr>
Erdoğan Bilgici <erdogan.bilgici@pardus.net.tr>


Kurulumu
------------
- Python 2 Kurulu olması gerekir.

apt-get install python


- PyQt4 Kurulu olması gerekir.

apt-get install python-pip python2.7-dev libxext-dev python-qt4 qt4-dev-tools build-essential

- netifaces paketi kurulu olması gerekir

apt-get install python-netifaces

Kullanımı
-----
İçindeki sh uzantılı dosyaya çift tıklamanız yeterli. Veya ./main/main.py dosyasini python ile çalıştırmanız yeterli olacaktır.
python ./main/main.py

Destek
---
İsmet Said Çalık <ismetsaid.calik@pardus.net.tr>
http://calik.me

Mehmet Nuri Öztürk <mehmetnuri.ozturk@pardus.net.tr>
Erdoğan Bilgici <erdogan.bilgici@pardus.net.tr>
