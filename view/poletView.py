from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QPixmap

from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel

from PyQt6 import uic

from resourse_path import resource_path
from view.QPrimaryFlightDisplay import QPrimaryFlightDisplay
from viewModel.vw_module import ViewModel

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
        polet = self.view_model.get_polet()

        self.video_player.roll=polet.roll
        self.video_player.pitch=polet.pitch
        self.video_player.skipskid=polet.skipskid
        self.video_player.heading=polet.heading
        self.video_player.airspeed=polet.airspeed
        self.video_player.alt=polet.alt
        self.video_player.vspeed=polet.vspeed
        self.video_player.battery=polet.battery
        self.video_player.arm=polet.arm

        self.video_player.update()















