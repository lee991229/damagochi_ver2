from code.front.ui.ui_class_widget_chat_room import Ui_talk_room_widget
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class ChatRoom(QWidget, Ui_talk_room_widget):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)