import sys, os, io

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ';' + os.environ['PATH']

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, \
    QVBoxLayout, QHBoxLayout, QGridLayout, \
    QDialog, QFileDialog, QMessageBox, QAbstractItemView

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
from PyPDF2 import PdfFileMerger

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class PDFApp(QWidget):
    def __init__(self):
        super.__init__()
        self.setWindowTitle("PDF Merger")
        self.setWindowIcon(QIcon(resource_path("../resource/merger_favicon.ico")))
        self.resize(1800,800)

