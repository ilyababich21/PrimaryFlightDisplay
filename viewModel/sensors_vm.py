import random
import time

import bluetooth
from PyQt6.QtCore import QThread, pyqtSignal

from model.PoletModel import Polet


class SensorsReader(QThread):
    params = pyqtSignal(Polet)
    uuid = "00001101-0000-1000-8000-00805F9B34FB"
    addr = "F4:C2:48:C0:4A:7F"

    def __init__(self):
        super().__init__()
        self.running = True
        self.polet = Polet()
        self.socket = self.connect()
        # print(self.socket)

    def connect(self):
        service_matches = bluetooth.find_service(uuid=self.uuid, address=self.addr)

        if len(service_matches) == 0:
            # print("couldn't find the FooBar service")
            return None
        else:

            first_match = service_matches[0]
            port = first_match["port"]
            host = first_match["host"]
            try:
                sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

            except Exception as e:
                print(e)
                sock = None
            if sock is not None:
                try:
                    sock.connect((host, port))
                except Exception as e:
                    print(e)
            return sock

    def run(self):

        # self.params.emit(self.polet)
        while self.running:
            if self.socket is not None:
                print("gop")
                self.socket.send("hello")
                client_data = self.socket.recv(1024)
                orientation = client_data.decode().split(" ")
                print(orientation)
                self.change_param(orientation)
            # time.sleep(1)
            else:
                # self.update_params()
                pass
            print("obnovil")
            time.sleep(0.05)
            # print(self.polet)
            self.params.emit(self.polet)


    def close(self):
        if self.socket:
            self.running = False
            self.socket.send("exit")
            self.socket.close()


    def change_param(self,orientation):
        self.polet.roll =float(orientation[1])
        self.polet.pitch =-float(orientation[0])
        self.polet.heading =float(orientation[2])
        self.polet.alt = float(orientation[3])

    def update_params(self):
        # Update the display of the vehicle state
        self.polet.roll = random.uniform(-1, 1)
        self.polet.pitch = random.uniform(-1, 1)
        # self.polet.pitch = random.random()
        # pfd.heading = random.randint(0,90)
        self.polet.heading = random.randint(20, 50)
        self.polet.airspeed = random.randint(25, 50)
        self.polet.vspeed = random.random()  # variometr
        self.polet.alt = random.randint(500, 700)  # altmeter высотаметр
        # self.polet.skipskid = 5  # индикатор скольжения, с английского "скитаться"
        self.polet.skipskid = random.randint(-5, 7)  # индикатор скольжения, с английского "скитаться"
        self.polet.battery = 80
        self.polet.arm = True
