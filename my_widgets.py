import os
from PyQt6.QtWidgets import (QLabel, QFileDialog)
from PyQt6.QtCore import Qt, QByteArray, QBuffer, QIODevice 
from PyQt6.QtGui import QDragEnterEvent, QDropEvent, QPixmap
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest


class ImageDropLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText("\n\n Drop Image Here \n - or - \n Click to Upload \n\n")
        self.setStyleSheet("""
            QLabel {
                border: 2px dashed #aaa;
                border-radius: 10px;
            }
        """)
        self.setFixedSize(256, 256)
        self.setAcceptDrops(True)
        self.image_data = None
        self.image_data_original = None
        self.network_manager = QNetworkAccessManager()
        self.network_manager.finished.connect(self.load_image_web) 

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def pixmap_to_bytes(self, pixmap):
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QIODevice.OpenModeFlag.WriteOnly)
        pixmap.save(buffer, "PNG")  # Save QPixmap as PNG in buffer
        return byte_array.data()  # Return bytes from QByteArray
        
    def dropEvent(self, event: QDropEvent):
        mime = event.mimeData()
        if mime.hasImage():
            # print('pass 1')
            event.accept()
            img = mime.imageData()
            pixmap = QPixmap.fromImage(img)
            print('pixmap size', pixmap.size())
            resized_pixmap = pixmap.scaled(256, 256, Qt.AspectRatioMode.KeepAspectRatio)
            self.setPixmap(resized_pixmap)
            self.image_data = self.pixmap_to_bytes(pixmap)

        elif mime.hasUrls():
            # print('pass 2')
            event.accept()
            url = mime.urls()[0]
            if url.isLocalFile():
                print('2.1')
                file_path = url.toLocalFile()
                self.load_image(file_path)
        else:
            event.ignore()

    def load_image_web(self, reply):
        data = reply.readAll()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        resized_pixmap = pixmap.scaled(256, 256, Qt.AspectRatioMode.KeepAspectRatio)
        self.setPixmap(resized_pixmap)
        self.image_data = self.pixmap_to_bytes(pixmap)

    def download_image(self, url):
        self.network_manager.get(QNetworkRequest(url))

    def load_image(self, file_path):
        _, ext = os.path.splitext(file_path)
        if ext.lower() in ('.jpeg', '.png', '.jpg'):
            pixmap = QPixmap(file_path)
            self.image_data = self.pixmap_to_bytes(pixmap)
            resized_pixmap = pixmap.scaled(256, 256, Qt.AspectRatioMode.KeepAspectRatio)
            self.setPixmap(QPixmap(resized_pixmap))

    def mousePressEvent(self, event):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select an image", os.getcwd(), "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.load_image(file_path)