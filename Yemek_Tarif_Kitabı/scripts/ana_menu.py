import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from corba_sayfasi import CorbaSayfasi
from ana_yemekler_sayfasi import AnaYemekSayfasi
from tatli_sayfasi import TatliSayfasi
from icecek_sayfasi import IcecekSayfasi
from arama_sayfasi import AramaSayfasi
from tarif_ekleme_sayfasi import TarifEklemeSayfasi
from tarif_silme_sayfasi import TarifSilmeSayfasi



class AnaMenu(QWidget):

    # Tarif silme sayfasını açan fonksiyon
    def tarif_silme_sayfasina_git(self):
        self.tarif_silme_sayfasi = TarifSilmeSayfasi()
        self.tarif_silme_sayfasi.show()

    # Tarif ekleme sayfasını açan fonksiyon
    def tarif_ekleme_sayfasina_git(self):
        self.tarif_ekleme_sayfasi = TarifEklemeSayfasi()
        self.tarif_ekleme_sayfasi.show()

    # Arama sayfasını açan fonksiyon
    def arama_sayfasina_git(self):
        self.arama_sayfasi = AramaSayfasi()
        self.arama_sayfasi.show()

    # Çorbalar sayfasını açan fonksiyon
    def corba_sayfasina_git(self):
        self.corba_sayfasi = CorbaSayfasi()
        self.corba_sayfasi.show()

    # Ana yemekler sayfasını açan fonksiyon
    def ana_yemek_sayfasina_git(self):
        self.ana_yemek_sayfasi = AnaYemekSayfasi()
        self.ana_yemek_sayfasi.show()
    
    # Tatlılar sayfasını açan fonksiyon
    def tatli_sayfasina_git(self):
        self.tatli_sayfasi = TatliSayfasi()
        self.tatli_sayfasi.show()

    # İçecekler sayfasını açan fonksiyon
    def icecek_sayfasina_git(self):
        self.icecek_sayfasi = IcecekSayfasi()
        self.icecek_sayfasi.show()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yemek Tarifi Kitabı - Ana Menü")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: white;")
        
        layout = QVBoxLayout()
        
        # Başlık
        self.baslik = QLabel("🍽️ Yemek Tarifi Kitabı", self)
        self.baslik.setFont(QFont("Arial", 20, QFont.Bold))
        self.baslik.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.baslik)

        # Buton Stili
        buton_stili = """
            QPushButton {
                font-size: 18px;
                padding: 10px;
                background-color: #ff6600;
                color: white;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #e65c00;
            }
        """

        # Arama Butonu
        self.arama_butonu = QPushButton("Tarif Ara")
        self.arama_butonu.setStyleSheet(buton_stili)
        self.arama_butonu.clicked.connect(self.arama_sayfasina_git)
        layout.addWidget(self.arama_butonu)

        # Tarif Ekle Butonu
        self.ekle_butonu = QPushButton("Tarif Ekle")
        self.ekle_butonu.setStyleSheet(buton_stili)
        self.ekle_butonu.clicked.connect(self.tarif_ekleme_sayfasina_git)
        layout.addWidget(self.ekle_butonu)

        # Tarif Sil Butonu
        self.silme_butonu = QPushButton("Tarif Sil")
        self.silme_butonu.setStyleSheet(buton_stili)
        self.silme_butonu.clicked.connect(self.tarif_silme_sayfasina_git)
        layout.addWidget(self.silme_butonu)

        # Çorbalar Butonu
        self.corba_butonu = QPushButton("Çorbalar")
        self.corba_butonu.setStyleSheet(buton_stili)
        self.corba_butonu.clicked.connect(self.corba_sayfasina_git)
        layout.addWidget(self.corba_butonu)

        # Ana Yemekler Butonu
        self.ana_yemek_butonu = QPushButton("Ana Yemekler")
        self.ana_yemek_butonu.setStyleSheet(buton_stili)
        self.ana_yemek_butonu.clicked.connect(self.ana_yemek_sayfasina_git)
        layout.addWidget(self.ana_yemek_butonu)

        # Tatlılar Butonu
        self.tatli_butonu = QPushButton("Tatlılar")
        self.tatli_butonu.setStyleSheet(buton_stili)
        self.tatli_butonu.clicked.connect(self.tatli_sayfasina_git)
        layout.addWidget(self.tatli_butonu)

        # İçecekler Butonu
        self.icecek_butonu = QPushButton("İçecekler")
        self.icecek_butonu.setStyleSheet(buton_stili)
        self.icecek_butonu.clicked.connect(self.icecek_sayfasina_git)
        layout.addWidget(self.icecek_butonu)
        
        

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = AnaMenu()
    pencere.show()
    sys.exit(app.exec_())
