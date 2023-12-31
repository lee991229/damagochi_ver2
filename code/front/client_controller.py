import random
import sys

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPoint, Qt, pyqtSignal

from code.front.class_timers import TmierClass
from code.front.ui.ui_class_main_widget_damagochi_ver2 import Ui_frame_damagochi
from network.class_client import ClientApp
from code.front.widget_screen import Screen
from code.front.class_custom_message_box import NoFrameMessageBox


class ClientController(QtWidgets.QWidget):
    log_in_signal = pyqtSignal(bool)
    assert_same_id_signal = pyqtSignal(bool)
    assert_join_signal = pyqtSignal(bool)
    set_progressBar = pyqtSignal()
    get_item_list_signal = pyqtSignal(list)
    recv_message = pyqtSignal(str)
    def __init__(self, client_app=ClientApp):
        super().__init__()
        self.client_app = client_app
        self.client_app.set_widget(self)
        self.widget_screen = Screen(self)
        self.timer = TmierClass(self)
        self.valid_duplication_id = None

        # 시그날 애밋
        self.initial_trigger_setting()

        # ui 동작 관련 변수
        self.list_widget_geometry_x = None
        self.list_widget_geometry_y = None
        self.drag_start_position = QPoint(0, 0)

    # 시그날
    def initial_trigger_setting(self):
        self.valid_duplication_id = False
        self.assert_same_id_signal.connect(self.assert_same_name_res)
        self.assert_join_signal.connect(self.sign_up_res)
        self.log_in_signal.connect(self.log_in)
        self.set_progressBar.connect(self.set_screen_character_progressBar)
        self.get_item_list_signal.connect(self.set_shop_item_list)
        #채팅 시그날
        self.recv_message.connect(self.set_recv_message)
    def run(self):
        self.widget_screen.show()



    def mousePressEvent(self, widget, event):
        self.drag_start_position = QPoint(widget.x(), widget.y())
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.globalPos() - widget.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, widget, event):
        if event.buttons() == Qt.LeftButton:
            widget.move(event.globalPos() - self.drag_start_position)
            event.accept()

    # def set_widget_screen_login(self):
    #     self.widget_screen.widget_screen_login()
    # 채팅 ===============================================================================
    def set_recv_message(self, chat):
        self.widget_screen.chat_input(chat)

    def chat_test(self, user_chat):
        self.client_app.send_chat_all_clients(user_chat)

    # 게임화면=============================================================================


    def set_shop_item_list(self, items_list):
        self.widget_screen.set_shop_widget(items_list)

    def get_shop_item_list(self):
        self.client_app.send_get_shop_item_list()

    def set_game_timer(self):
        self.timer.timer1.start()
    def click_eat_btn(self):
        self.client_app.user_character_hunger += 10
        self.set_screen_character_progressBar()
    def click_play_btn(self):
        self.client_app.user_character_affection += 10
        self.set_screen_character_progressBar()

    def click_wash_btn(self):
        print('깨끗해짐;')
        # self.client_app.user_character_affection

    def character_timer_event(self):
        self.timer_event_character_hunger()  # 배고픔 수치 줄어듬
        # 애정도 수치 줄어듬
        if self.client_app.user_character_hunger <= 20:
            self.timer_event_character_affection()
        # 건강 수치 줄어듬
        if self.client_app.user_character_hunger <= 0 and self.client_app.user_character_affection <= 20:
            self.timer_event_character_health()
        self.set_screen_character_progressBar()

    def timer_event_character_hunger(self):
        self.client_app.user_character_hunger -= random.randint(1, 5)
        if self.client_app.user_character_hunger < 0:
            self.client_app.user_character_hunger = 0
        # print('배가 고파져', self.client_app.user_character_hunger)

    def timer_event_character_affection(self):
        self.client_app.user_character_affection -= random.randint(1, 5)
        if self.client_app.user_character_affection < 0:
            self.client_app.user_character_affection = 0
        # print('배가고파 애정도가 떨어져', self.client_app.user_character_affection)

    def timer_event_character_health(self):
        self.client_app.user_character_health -= random.randint(1, 5)
        if self.client_app.user_character_health < 0:
            self.client_app.user_character_health = 0
        # print('배고프고 애정도도 낮아서 건강이 나빠져', self.client_app.user_character_health)

    def set_screen_character_progressBar(self):
        bar1 = self.client_app.user_character_hunger
        bar2 = self.client_app.user_character_affection
        self.widget_screen.set_character_progressBar(bar1, bar2)

    # 회원가입=============================================================================
    # 회원가입 승인결과
    def sign_up_res(self, return_result: bool):
        if return_result is True:
            result = NoFrameMessageBox(self, "성공", "회원가입 성공", "about")
            self.widget_screen.login_screen()
            return
        elif return_result is False:
            return NoFrameMessageBox(self, "실패", "회원가입 실패", "about")

    # 회원가입 아이디 중복확인
    def assert_same_name_res(self, return_result: bool):
        if return_result is True:
            self.valid_duplication_id = True
            self.widget_screen.user_name_duplicate_check_true("(사용가능)ID:")
            # return NoFrameMessageBox(self, "가능", "중복 없는 아이디, 써도됌", "about")
        elif return_result is False:
            self.widget_screen.user_name_duplicate_check_true("(사용불가)ID:")
            # return NoFrameMessageBox(self, "불가능", "중복 아이디, 새로 쓰기", "about")

    # 회원가입 승인요청
    def join_access(self):
        join_username = self.widget_screen.lineEdit_join_username.text()
        join_pw = self.widget_screen.lineedit_join_pw_1.text()
        join_nickname = self.widget_screen.lineEdit_join_nickname.text()
        self.client_app.send_join_id_and_pw_for_join_access(join_username, join_pw, join_nickname)

    # 회원가입 아이디 중복체크
    def username_duplicatecheck(self, assert_username):
        self.client_app.send_username_duplicatecheck(assert_username)

    # 회원가입=============================================================================
    # 로그인 ==============================================================================

    # 유저가 아이디 비밀번호를 입력하고 로그인버튼 클릭시
    def assert_login_data(self, usr_inp_name, usr_inp_pw):
        self.client_app.send_login_id_and_pw_for_login_access(usr_inp_name, usr_inp_pw)

    # 로그인 성공
    def log_in(self, return_result: bool):
        if return_result is True:
            result = NoFrameMessageBox(self, "성공", "로그인 성공", "about")
            # todo: 캐릭터 조회,생성
            self.get_user_character()
            self.set_game_timer()
            # # 캐릭터 stat정보 불러오기
            # self.get_user_character_stat()
            self.widget_screen.widget_game_screen()
            return
        elif return_result is False:
            return NoFrameMessageBox(self, "실패", "로그인 실패", "about")

    def get_user_character(self):
        self.client_app.send_get_user_character()
    # def get_user_character_stat(self):
    #     self.client_app.send_get_user_character_stat()
    # 로그인 ==============================================================================

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     myWindow = WidgetMain()
#     myWindow.show()
#
#     # mywindow2.show()
#     app.exec_()
# # 커서 이미지 변경
# # num = random.randint(1, 4)
# custom_cursor_pixmap = QPixmap(f'./img/cursor/4.png')
# cursor = QCursor(custom_cursor_pixmap)
# app.setOverrideCursor(cursor)
# # 폰트 적용
# fontDB = QFontDatabase()
# fontDB.addApplicationFont('./font/Pretendard-Regular.ttf')
# app.setFont(QFont('Pretendard'))
