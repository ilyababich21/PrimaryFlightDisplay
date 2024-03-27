from PyQt6.QtCore import pyqtSignal, QObject
from PyQt6.QtGui import QImage

from model.PoletModel import Polet
from viewModel.video_vm import VideoReader, SensorsReader


class ViewModel(QObject):
    change_image = pyqtSignal(QImage)

    def __init__(self):
        super().__init__()
        self.model = Polet()
        self.video_reader = VideoReader(30)
        self.video_reader.change_pixmap_signal.connect(self.send_image)
        self.video_reader.start()

        self.sensors_reader = SensorsReader()
        self.sensors_reader.params.connect(self.update_model)
        self.sensors_reader.start()



    def send_image(self, q_image):
        self.change_image.emit(q_image)

    def get_polet(self):
        return self.model

    def update_model(self, polet):
        self.model.roll = polet.roll
        self.model.pitch =polet.pitch
        self.model.heading =polet.heading
        self.model.airspeed =polet.airspeed
        self.model.vspeed =polet.vspeed
        self.model.alt =polet.alt
        self.model.skipskid =polet.skipskid
        self.model.battery = polet.battery
        self.model.arm = polet.arm
