from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from code.front.login_screen_method import Login
from code.front.ui.ui_class_main_widget_damagochi_ver2 import Ui_frame_damagochi


class Screen(QWidget, Ui_frame_damagochi):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.client_controller = client_controller
        self.set_btn_trigger()  # 버튼 시그널 받는 메서드
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)

    def mousePressEvent(self, event):
        self.client_controller.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        self.client_controller.mouseMoveEvent(self, event)

    # 회원 가입 창 버튼 시그널 메서드
    def set_btn_trigger(self):
        self.btn_login.clicked.connect(lambda state: Login.assert_login(self))
        pass
