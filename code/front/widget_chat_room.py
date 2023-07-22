from code.front.ui.ui_class_widget_chat_room import Ui_talk_room_widget
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class ChatRoom(QWidget, Ui_talk_room_widget):
    def __init__(self, screen):
        super().__init__()
        self.setupUi(self)
        self.screen = screen
        self.set_btn_trigger()
    def mousePressEvent(self, event):
        self.screen.client_controller.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        self.screen.client_controller.mouseMoveEvent(self, event)
    def chat_line_edit_input(self):
        user_chat = self.user_chatting_lineedit.text()
        # 클라이언트앱 호출 로직 추가
        self.user_chatting_lineedit.clear()
        self.screen.screen_chat_test(user_chat)
    def set_btn_trigger(self):
        # self.btn_member_plus.clicked.connect(lambda state:
        #                                      self.client_controller.show_member_plus())  # todo: 채팅방에 있는 유저 정보 저장하고 파라미터로 이거 보내
        # self.widget_member_count.mouseDoubleClickEvent = lambda x: (self.client_controller.show_room_member_list())
        self.btn_chat_enter.clicked.connect(lambda state: self.chat_line_edit_input())
        self.btn_flist_close.clicked.connect(lambda state: self.close())
        self.user_chatting_lineedit.returnPressed.connect(lambda : self.chat_line_edit_input())