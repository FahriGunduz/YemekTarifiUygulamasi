import sqlite3
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit, QPushButton, QComboBox, QMessageBox, QFrame
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt

class TarifEklemeSayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tarif Ekle")
        self.setGeometry(100, 100, 800, 550)
        self.setStyleSheet("background-color: #fdfdfd;")

        ana_layout = QVBoxLayout()
        ana_layout.setContentsMargins(50, 30, 50, 30)
        ana_layout.setSpacing(20)

        # Başlık
        baslik = QLabel("➕ Yeni Tarif Ekle")
        baslik.setFont(QFont("Arial", 24, QFont.Bold))
        baslik.setAlignment(Qt.AlignCenter)
        baslik.setStyleSheet("color: #333333;")
        ana_layout.addWidget(baslik)

        # Tarif Adı
        self.ad_input = QLineEdit()
        self.ad_input.setPlaceholderText("Tarif Adı")
        self.ad_input.setFont(QFont("Arial", 14))
        self.ad_input.setStyleSheet(self._input_style())
        ana_layout.addWidget(self.ad_input)

        # Kategori Seçimi
        self.kategori_combo = QComboBox()
        self.kategori_combo.addItems(["Çorba", "Ana Yemek", "Tatlı", "İçecek"])
        self.kategori_combo.setFont(QFont("Arial", 14))
        self.kategori_combo.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 2px solid #ccc;
                border-radius: 8px;
                padding: 8px;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)
        ana_layout.addWidget(self.kategori_combo)

        # Tarif Metni
        self.tarif_input = QTextEdit()
        self.tarif_input.setPlaceholderText("Tarif detaylarını buraya yazınız...")
        self.tarif_input.setFont(QFont("Arial", 13))
        self.tarif_input.setStyleSheet("""
            QTextEdit {
                border: 2px solid #ccc;
                border-radius: 8px;
                padding: 10px;
                background-color: #ffffff;
                color: #333;
            }
        """)
        ana_layout.addWidget(self.tarif_input)

        # Ekle Butonu
        self.ekle_buton = QPushButton("✔️ Tarifi Kaydet")
        self.ekle_buton.setFont(QFont("Arial", 14, QFont.Bold))
        self.ekle_buton.setCursor(Qt.PointingHandCursor)
        self.ekle_buton.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                padding: 12px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        self.ekle_buton.clicked.connect(self.tarif_ekle)
        ana_layout.addWidget(self.ekle_buton)

        # Alt çizgi
        alt_cizgi = QFrame()
        alt_cizgi.setFrameShape(QFrame.HLine)
        alt_cizgi.setFrameShadow(QFrame.Sunken)
        alt_cizgi.setStyleSheet("color: #cccccc;")
        ana_layout.addWidget(alt_cizgi)

        self.setLayout(ana_layout)

    def _input_style(self):
        return """
            QLineEdit {
                border: 2px solid #ccc;
                border-radius: 8px;
                padding: 10px;
                background-color: #ffffff;
                color: #333;
            }
        """

    def tarif_ekle(self):
        isim = self.ad_input.text().strip()
        kategori = self.kategori_combo.currentText()
        tarif = self.tarif_input.toPlainText().strip()

        if not isim or not tarif:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurunuz.")
            return

        try:
            conn = sqlite3.connect("tarifler.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tarifler (isim, kategori, tarif) VALUES (?, ?, ?)",
                           (isim, kategori, tarif))
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Başarılı", f"'{isim}' tarifiniz başarıyla eklendi!")
            self.ad_input.clear()
            self.tarif_input.clear()
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Tarif eklenemedi: {str(e)}")
