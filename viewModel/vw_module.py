from PyQt6.QtCore import pyqtSignal, QObject
from PyQt6.QtGui import QImage

from viewModel.video_vm import VideoReader


class ViewModel(QObject):
    change_image = pyqtSignal(QImage)


    def __init__(self):
        super().__init__()
        self.video_reader = VideoReader()
        self.video_reader.change_pixmap_signal.connect(self.send_image)
        self.video_reader.start()

    def send_image(self,q_image):
        self.change_image.emit(q_image)