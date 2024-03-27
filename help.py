# import serial
# from serial.tools import list_ports
# enmu_ports = enumerate(list_ports.comports())
# port = ""
# for n, (p, descriptor, hid) in enmu_ports:
#     print(p)
#     if descriptor == 'USB-Serial Controller D':
#         port = p
# port = "COM13"
import sys
from time import sleep

import bluetooth

# nearby_devices = bluetooth.discover_devices(lookup_names=True)
# print("Found {} devices.".format(len(nearby_devices)))
#
# for addr, name in nearby_devices:
#     print("  {} - {}".format(addr, name))

uuid = "00001101-0000-1000-8000-00805F9B34FB"
addr = "F4:C2:48:C0:4A:7F"
# #
service_matches = bluetooth.find_service(uuid=uuid,address=addr)

if len(service_matches) == 0:
    print("couldn't find the FooBar service")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print(port)
print(name)
print(host)
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host,port))
while True:
    data = input("Vvedite soobshenie: ")
    if not data:
        break
    sock.send(data)
    client_data=sock.recv(1024)
    print(client_data.decode())

sock.close()
