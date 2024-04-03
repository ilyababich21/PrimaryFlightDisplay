from PyQt6.QtWidgets import QMainWindow

from PyQt6 import uic, QtGui

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
        self.view_model.change_model.connect(self.update_model)

    def update_model(self, polet):
        self.video_player.roll = polet.roll
        self.video_player.pitch = polet.pitch
        self.video_player.skipskid = polet.skipskid
        self.video_player.heading = polet.heading
        self.video_player.airspeed = polet.airspeed
        self.video_player.alt = polet.alt
        self.video_player.vspeed = polet.vspeed
        self.video_player.battery = polet.battery
        self.video_player.arm = polet.arm

    def update_image(self, qt_image):
        self.video_player.image = qt_image
        self.video_player.update()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.view_model.closeConnection()
