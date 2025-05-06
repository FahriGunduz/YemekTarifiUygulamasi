import sqlite3
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class AramaSayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tarif Arama")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: #F0F8FF;")

        layout = QVBoxLayout()

        # Başlık
        self.baslik = QLabel("🔍 Tarif Arama", self)
        self.baslik.setFont(QFont("Arial", 20, QFont.Bold))
        self.baslik.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.baslik)

        # Arama Kutusu
        self.arama_kutusu = QLineEdit(self)
        self.arama_kutusu.setPlaceholderText("Tarif adı giriniz...")
        self.arama_kutusu.setFont(QFont("Arial", 14))
        self.arama_kutusu.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 2px solid #007acc;
                border-radius: 10px;
                font-size: 16px;
            }
        """)
        layout.addWidget(self.arama_kutusu)

        # Arama Butonu
        self.arama_butonu = QPushButton("Ara", self)
        self.arama_butonu.setFont(QFont("Arial", 14))
        self.arama_butonu.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                padding: 10px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #005f99;
            }
        """)
        self.arama_butonu.clicked.connect(self.tarif_ara)
        layout.addWidget(self.arama_butonu)

        # Sonuç Alanı
        self.sonuc_alani = QTextEdit(self)
        self.sonuc_alani.setReadOnly(True)
        self.sonuc_alani.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;
                border: 2px solid #ddd;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
                color: #333;
            }
        """)
        layout.addWidget(self.sonuc_alani)

        self.setLayout(layout)

    def tarif_ara(self):
        aranan = self.arama_kutusu.text().strip()
        if not aranan:
            self.sonuc_alani.setText("Lütfen bir tarif adı giriniz.")
            return

        conn = sqlite3.connect("tarifler.db")
        cursor = conn.cursor()
        cursor.execute("SELECT isim, tarif FROM tarifler WHERE isim LIKE ?", ('%' + aranan + '%',))
        sonuc = cursor.fetchall()
        conn.close()

        if sonuc:
            metin = ""
            for isim, tarif in sonuc:
                metin += f"🍴 {isim}\n{tarif}\n\n"
            self.sonuc_alani.setText(metin.strip())
        else:
            self.sonuc_alani.setText("Aranan tarif bulunamadı.")
