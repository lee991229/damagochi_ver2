from code.front.ui.ui_class_widget_menu import Ui_dialog_menu
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class UiDialogMenu(QDialog, Ui_dialog_menu):
    def __init__(self, screen):
        super().__init__()
        self.setupUi(self)
        self.screen = screen
        self.set_btn_trigger()

    def set_btn_trigger(self):
        self.pushButton.clicked.connect(lambda state: self.screen.show_chat_room())  # 채팅방
        # self.pushButton_2.clicked.connect(self.screen)  # 유저정보
        self.pushButton_3.clicked.connect(lambda state: self.screen.game_logout())  # 로그아웃
