import datetime
import socket
import time
from threading import *


class ClientApp:
    HOST = '이종혁'
    PORT = 9999
    BUFFER = 50000
    FORMAT = "utf-8"
    HEADER_LENGTH = 30

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))
        self.client_widget = None

    def set_widget(self, widget_):
        self.client_widget = widget_
