import sqlite3
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QComboBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class TatliSayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tatlı Tarifleri")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: #FFD700;") 

        layout = QVBoxLayout()

        # Başlık
        self.baslik = QLabel("🍰 Tatlı Tarifleri", self)
        self.baslik.setFont(QFont("Arial", 20, QFont.Bold))
        self.baslik.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.baslik)

        # Tatlı Seçimi için ComboBox
        self.comboBox = QComboBox(self)
        self.comboBox.setFont(QFont("Arial", 14))
        self.comboBox.setStyleSheet("""
            QComboBox {
                background-color: #ffffff;
                border: 2px solid #ff6600;
                border-radius: 10px;
                padding: 5px;
                font-size: 16px;
            }
        """)
        layout.addWidget(self.comboBox)

        # Tarif Gösterme Alanı
        self.tarif_label = QLabel("Lütfen bir tatlı seçin.", self)
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

        # Veritabanından tatlıları yükler
        self.verileri_yukle()

        # ComboBox değiştiğinde tarifi gösterir
        self.comboBox.currentIndexChanged.connect(self.guncelle_tarif)

    def verileri_yukle(self):
        """SQLite veritabanından tatlı tariflerini yükler"""
        conn = sqlite3.connect("tarifler.db")
        cursor = conn.cursor()
        cursor.execute("SELECT isim FROM tarifler WHERE kategori='Tatlı'")
        tatlilar = cursor.fetchall()
        conn.close()

        self.comboBox.clear()
        for tatli in tatlilar:
            self.comboBox.addItem(tatli[0])

    def guncelle_tarif(self):
        """Seçilen tatlının tarifini getirir"""
        secilen_tatli = self.comboBox.currentText()

        conn = sqlite3.connect("tarifler.db")
        cursor = conn.cursor()
        cursor.execute("SELECT tarif FROM tarifler WHERE isim=?", (secilen_tatli,))
        sonuc = cursor.fetchone()
        conn.close()

        if sonuc:
            self.tarif_label.setText(sonuc[0])
        else:
            self.tarif_label.setText("Tarif bulunamadı.")
