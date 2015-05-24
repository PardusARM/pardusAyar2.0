#!/usr/share/bin/python
# -*- coding: utf-8 -*-
# Author: Ismet Said Calik
# Author Mail : ismetsaid.calik@gmail.com

from PyQt4 import QtCore, QtGui
import sys
import commands
import os
import netifaces as ni

from pardusAyar_20 import Ui_Dialog

ip = ni.ifaddresses('lo')[2][0]['addr']

class MainWindow(QtGui.QMainWindow, Ui_Dialog):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.lblHostname.setText(str(commands.getoutput("hostname")))
        self.lblKernel.setText(str(commands.getoutput("uname -r")))
        self.lblIP.setText(ip)

        QtCore.QObject.connect(self.btnsshBaslat, QtCore.SIGNAL("clicked()"), self.sshBaslat)
        QtCore.QObject.connect(self.btnsshDur, QtCore.SIGNAL("clicked()"), self.sshDurdur)
        QtCore.QObject.connect(self.btnsshBaslat, QtCore.SIGNAL("clicked()"), self.sshBaslat)

        QtCore.QObject.connect(self.btnhttpBaslat, QtCore.SIGNAL("clicked()"), self.httpBaslat)
        QtCore.QObject.connect(self.btnhttpDur, QtCore.SIGNAL("clicked()"), self.httpDurdur)
        QtCore.QObject.connect(self.btnhttpYeniden, QtCore.SIGNAL("clicked()"), self.httpYeniden)

        QtCore.QObject.connect(self.btnftpBaslat, QtCore.SIGNAL("clicked()"), self.ftpBaslat)
        QtCore.QObject.connect(self.btnftpDur, QtCore.SIGNAL("clicked()"), self.ftpDurdur)
        QtCore.QObject.connect(self.btnftpYeniden, QtCore.SIGNAL("clicked()"), self.ftpYeniden)

        QtCore.QObject.connect(self.hakkinda,QtCore.SIGNAL("clicked()"), self.btnhakkinda)

        QtCore.QObject.connect(self.kapat, QtCore.SIGNAL("clicked()"), self.close)
        self.setFixedSize(425, 285)

    def sshBaslat(self):
        os.system("service sshd start")
        os.system("sleep 2")
        print("SSH sunucusu başarı ile başlatıldı.")
        QtGui.QMessageBox.information(self, u"Başatıldı", u"SSH sunucusu başarı ile başlatıldı.")
        self.lblSSHDurum.setText("AKTIF")
    def sshDurdur(self):
        os.system("service sshd stop")
        os.system("sleep 2")
        print("SSH sunucusu başarı ile kapatildı.")
        QtGui.QMessageBox.information(self, u"Durduruldu", u"SSH sunucusu başarı ile kapatıldı.")
        self.lblSSHDurum.setText("KAPALI")
    def sshYeniden(self):
        os.system("service sshd restart")
        os.system("sleep 2")
        print("SSH sunucusu başarı ile yeniden baslatildı.")
        QtGui.QMessageBox.information(self, u"Yeniden Başlatıldı", u"SSH sunucusu başarı ile yeniden başlatıldı.")
        self.lblSSHDurum.setText("AKTIF")


    def httpBaslat(self):
        os.system("service lighttpd start")
        os.system("sleep 2")
        print("HTTP sunucusu başarı ile başlatıldı.")
        QtGui.QMessageBox.information(self, u"Başatıldı", u"HTTP sunucusu başarı ile başlatıldı")
        self.lblhttpDurum.setText("AKTIF")
    def httpDurdur(self):
        os.system("service lighttpd stop")
        os.system("sleep 2")
        print("HTTP sunucusu başarı ile kapatildı.")
        QtGui.QMessageBox.information(self, u"Durduruldu", u"HTTP sunucusu başarı ile kapatıldı")
        self.lblhttpDurum.setText("KAPALI")
    def httpYeniden(self):
        os.system("service lighttpd restart")
        os.system("sleep 2")
        print("HTTP sunucusu başarı ile yeniden baslatildı.")
        QtGui.QMessageBox.information(self, u"Yeniden Başlatıldı", u"HTTP sunucusu başarı ile kapatıldı")
        self.lblhttpDurum.setText("AKTIF")



    def ftpBaslat(self):
        os.system("service vsftpd start")
        os.system("sleep 2")
        print("FTP sunucusu başarı ile başlatıldı.")
        QtGui.QMessageBox.information(self, u"Başatıldı", u"FTP sunucusu başarı ile başlatıldı")
        self.lblftpDurum.setText("AKTIF")
    def ftpDurdur(self):
        os.system("service vsftpd stop")
        os.system("sleep 2")
        print("FTP sunucusu başarı ile kapatildı.")
        QtGui.QMessageBox.information(self, u"Durduruldu", u"FTP sunucusu başarı ile kapatıldı")
        self.lblftpDurum.setText("KAPALI")
    def ftpYeniden(self):
        os.system("service vsftpd restart")
        os.system("sleep 2")
        print("FTP sunucusu başarı ile yeniden baslatildı.")
        QtGui.QMessageBox.information(self, u"Yeniden Başlatıldı", u"FTP sunucusu başarı ile yeniden başlatıldı.")
        self.lblftpDurum.setText("AKTIF")



    def btnhakkinda(self):
        QtGui.QMessageBox.information(self, u"Hakkında", u"İsmet Said Çalık <ismetsaid.calik@pardus.net.tr>\nMehmet Nuri Öztürk <mehmetnuri.ozturk@pardus.net.tr>\nErdoğan Bilgici <erdogan.bilgici@pardus.net.tr>")





    def app(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

def main():
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    mw.app()
    mw.show()
    return app.exec_()
if __name__ == '__main__':
    main()