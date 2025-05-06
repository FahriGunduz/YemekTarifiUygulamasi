import sqlite3
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QComboBox, QScrollArea
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class CorbaSayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çorba Tarifleri")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: #FFA500;")

        layout = QVBoxLayout()

        # Başlık
        self.baslik = QLabel("🍵 Çorba Tarifleri", self)
        self.baslik.setFont(QFont("Arial", 20, QFont.Bold))
        self.baslik.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.baslik)

        # Çorba Seçimi için ComboBox
        self.comboBox = QComboBox(self)
        self.comboBox.setFont(QFont("Arial", 14))
        self.comboBox.setStyleSheet("""
            QComboBox {
                background-color: #ffffff;
                border: 2px solid #ff9800;
                border-radius: 10px;
                padding: 5px;
                font-size: 16px;
            }
        """)
        layout.addWidget(self.comboBox)

        # Tarif Gösterme Alanı
        self.tarif_label = QLabel("Lütfen bir çorba seçin.", self)
        self.tarif_label.setFont(QFont("Arial", 12))
        self.tarif_label.setAlignment(Qt.AlignTop)
        self.tarif_label.setWordWrap(True)
        self.tarif_label.setStyleSheet("""
            background-color: #ffffff;
            border: 2px solid #ddd;
            border-radius: 10px;
            padding: 10px;
            font-size: 14px;
            color: #555;
        """)
        layout.addWidget(self.tarif_label)
        self.setLayout(layout)

        # Veritabanından çorba tariflerini yükler
        self.verileri_yukle()

        # ComboBox değiştiğinde tarifi gösterir
        self.comboBox.currentIndexChanged.connect(self.guncelle_tarif)

    def verileri_yukle(self):
        """SQLite veritabanından çorba tariflerini yükler"""
        conn = sqlite3.connect("tarifler.db")
        cursor = conn.cursor()
        cursor.execute("SELECT isim FROM tarifler WHERE kategori='Çorba'")
        corbalar = cursor.fetchall()
        conn.close()

        self.comboBox.clear()
        for corba in corbalar:
            self.comboBox.addItem(corba[0])

    def guncelle_tarif(self):
        """Seçilen çorbanın tarifini getirir"""
        secilen_corba = self.comboBox.currentText()

        conn = sqlite3.connect("tarifler.db")
        cursor = conn.cursor()
        cursor.execute("SELECT tarif FROM tarifler WHERE isim=?", (secilen_corba,))
        sonuc = cursor.fetchone()
        conn.close()

        if sonuc:
            self.tarif_label.setText(sonuc[0])
        else:
            self.tarif_label.setText("Tarif bulunamadı.")
