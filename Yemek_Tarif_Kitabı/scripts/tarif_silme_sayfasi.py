import sqlite3
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class TarifSilmeSayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tarif Sil")
        self.setGeometry(100, 100, 800, 400)
        self.setStyleSheet("background-color: #FFE6E6;")

        layout = QVBoxLayout()

        # Başlık
        self.baslik = QLabel("❌ Tarif Sil", self)
        self.baslik.setFont(QFont("Arial", 20, QFont.Bold))
        self.baslik.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.baslik)

        # ComboBox ile tarif seçimi
        self.comboBox = QComboBox(self)
        self.comboBox.setFont(QFont("Arial", 14))
        layout.addWidget(self.comboBox)

        # Silme Butonu
        self.sil_buton = QPushButton("Seçilen Tarifi Sil", self)
        self.sil_buton.setFont(QFont("Arial", 14))
        self.sil_buton.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;
                color: white;
                padding: 10px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
        """)
        self.sil_buton.clicked.connect(self.tarif_sil)
        layout.addWidget(self.sil_buton)

        self.setLayout(layout)

        self.tarifleri_yukle()

    def tarifleri_yukle(self):
        """Veritabanından tarifleri combobox'a yükler"""
        conn = sqlite3.connect("tarifler.db")
        cursor = conn.cursor()
        cursor.execute("SELECT isim FROM tarifler")
        tarifler = cursor.fetchall()
        conn.close()

        self.comboBox.clear()
        for tarif in tarifler:
            self.comboBox.addItem(tarif[0])

    def tarif_sil(self):
        secilen_tarif = self.comboBox.currentText()

        if not secilen_tarif:
            QMessageBox.warning(self, "Uyarı", "Lütfen silinecek bir tarif seçiniz.")
            return

        cevap = QMessageBox.question(self, "Emin misiniz?",
                                     f"'{secilen_tarif}' tarifini silmek istediğinize emin misiniz?",
                                     QMessageBox.Yes | QMessageBox.No)

        if cevap == QMessageBox.Yes:
            conn = sqlite3.connect("tarifler.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tarifler WHERE isim=?", (secilen_tarif,))
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Başarılı", f"'{secilen_tarif}' tarifiniz silindi.")
            self.tarifleri_yukle()
