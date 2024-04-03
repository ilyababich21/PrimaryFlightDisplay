from PyQt6.QtCore import pyqtSignal, QObject
from PyQt6.QtGui import QImage

from model.PoletModel import Polet
from viewModel.sensors_vm import SensorsReader
from viewModel.video_vm import VideoReader


class ViewModel(QObject):
    change_image = pyqtSignal(QImage)
    change_model = pyqtSignal(Polet)

    def __init__(self):
        super().__init__()
        self.video_reader = VideoReader(30)
        self.video_reader.change_pixmap_signal.connect(self.send_image)

        self.sensors_reader = SensorsReader()
        self.sensors_reader.params.connect(self.update_model)
        self.video_reader.start()
        self.sensors_reader.start()



    def send_image(self, q_image):
        self.change_image.emit(q_image)


    def closeConnection(self):
        self.sensors_reader.close()

    def update_model(self, polet):
        self.change_model.emit(polet)
