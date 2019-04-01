import socket
import fcntl
import struct
import datetime
 
class IPAddress():
    def __init__(self):
        print(datetime.datetime.now().time())
 
    def get_interface_ipaddress(self, network):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', network[:15])
        )[20:24])
 
    def get_ipaddress(self, network='wlan0'):
        return self.get_interface_ipaddress(network)
