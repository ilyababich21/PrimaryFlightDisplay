from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QPixmap

from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel

from PyQt6 import uic

from resourse_path import resource_path
from view.QPrimaryFlightDisplay import QPrimaryFlightDisplay
from viewModel.video_vm import VideoReader
from viewModel.vw_module import ViewModel


class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
        # self.cap = cv2.VideoCapture(0)
        self.layout = QVBoxLayout()
        self.label = QLabel("Pizda")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


        self.video_reader=VideoReader()
        self.video_reader.change_pixmap_signal.connect(self.update_image)
        self.video_reader.start()

    def update_image(self, qt_image):
        pixmap = QPixmap.fromImage(qt_image)
        self.label.setPixmap(pixmap)


class PoletView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(resource_path("view/UI/main.ui"), self)
        self.view_model = ViewModel()
        self.video_player = QPrimaryFlightDisplay()
        self.setCentralWidget(self.video_player)

        self.view_model.change_image.connect(self.update_image)



    def update_image(self,qt_image):
        self.video_player.image = qt_image
        self.video_player.update()















