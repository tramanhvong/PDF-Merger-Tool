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

class ListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent=None)
        self.setAcceptDrops(True)
        self.setStyleSheet('font-size: 25px;')
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            return super().dragEnterEvent(event)
        
    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            return super().dragMoveEvent(event)
        
    def dragDropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            pdf_list = []
            for url in event.mimeData().urls():
                if url.isLocalFile(): 
                    if url.toString().endswith(".pdf"):
                        # if local file and is pdf, then convert to string
                        pdf_list.append(str(url.toLocalFile()))
            self.addItems(pdf_list) # append the file to list
        else:
            return super().dragDropEvent(event)
        
class output_field(QLineEdit):
    def __init__(self):
        super().__init__()
        self.height = 55
        self.setStyleSheet('font-size: 30px;')
        self.setFixedHeight(self.height)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore() # not changing behavior
        
    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore() # not changing behavior

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            if event.mimeData().urls(): # in case of multiple files, just take the first one
                self.setText(event.mimeData().urls()[0].toLocalFile())
        else:
            event.ignore()

class PDFApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Merger")
        self.setWindowIcon(QIcon(resource_path("resource/favicon.ico")))
        self.resize(1800,800)

app = QApplication(sys.argv)
app.setStyle('Fusion')

pdf = PDFApp()
pdf.show()

sys.exit(app.exec_())