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

    def initial_trigger_setting(self):
        self.valid_duplication_id = False
        self.assert_same_id_signal.connect(self.assert_same_name_res)
        self.assert_join_signal.connect(self.sign_up_res)
        self.log_in_signal.connect(self.log_in)

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
    # 게임화면=============================================================================

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

    def set_game_timer(self):
        self.timer.timer1.start()

    def character_timer_event(self):
        print('타이머 돌아가욧')
        self.timer_event_character_hunger()
        # if self.client_app.user_character_hunger <= 20:
        #     self.client_app.user_character_affection =
        # if self.client_app.user_character_hunger <= 0 and self.client_app.user_character_affection <= 20:
        #     self.client_app.user_character_health =

    def timer_event_character_hunger(self):
        character_hunger = int(self.client_app.user_character_hunger)
        self.client_app.user_character_hunger = character_hunger - random.randint(1, 5)
        print(self.client_app.user_character_hunger)

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
