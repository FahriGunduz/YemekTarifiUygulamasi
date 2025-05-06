import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from ana_menu import AnaMenu

class GirisEkrani(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yemek Tarifi Kitabı - Giriş")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: white;")
        
        layout = QVBoxLayout()
        
        
        self.resim_label = QLabel(self)
        pixmap = QPixmap("image\img1.png")  
        self.resim_label.setPixmap(pixmap)
        self.resim_label.setAlignment(Qt.AlignCenter)
        
        
        self.baslik = QLabel("Hoş Geldiniz!", self)
        self.baslik.setStyleSheet("font-size: 24px; font-weight: bold; color: black;")
        self.baslik.setAlignment(Qt.AlignCenter)
        
        # Devam butonu
        self.devam_butonu = QPushButton("Başla")
        self.devam_butonu.setStyleSheet("font-size: 18px; padding: 10px; background-color: #ff6600; color: white; border-radius: 10px;")
        self.devam_butonu.clicked.connect(self.devam_et)
        
        layout.addWidget(self.resim_label)
        layout.addWidget(self.baslik)
        layout.addWidget(self.devam_butonu)
        
        self.setLayout(layout)
        
    def devam_et(self):
        self.hide() 
        self.ana_menu = AnaMenu() 
        self.ana_menu.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = GirisEkrani()
    pencere.show()
    sys.exit(app.exec_())
