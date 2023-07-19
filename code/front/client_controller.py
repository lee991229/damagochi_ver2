import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPoint, Qt, pyqtSignal

from code.front.ui.ui_class_main_widget_damagochi_ver2 import Ui_frame_damagochi
from network.class_client import ClientApp
from code.front.widget_screen import Screen


class ClientController(QtWidgets.QWidget):

    assert_same_id_signal = pyqtSignal(bool)

    def __init__(self, client_app=ClientApp):
        super().__init__()
        self.client_app = client_app
        self.client_app.set_widget(self)
        self.widget_screen = Screen(self)
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

# 회원가입=============================================================================

    def assert_same_name_res(self, return_result: bool):
        if return_result is True:
            self.valid_duplication_id = True
            self.widget_screen.user_name_duplicate_check_true("(사용가능)ID:")
            # return NoFrameMessageBox(self, "가능", "중복 없는 아이디, 써도됌", "about")
        elif return_result is False:
            self.widget_screen.user_name_duplicate_check_true("(사용불가)ID:")
            # return NoFrameMessageBox(self, "불가능", "중복 아이디, 새로 쓰기", "about")
    def join_access(self):
        join_username = self.widget_screen.lineEdit_join_username.text()
        join_pw = self.widget_screen.lineedit_join_pw_1.text()
        join_nickname = self.widget_screen.lineEdit_join_nickname.text()
        self.client_app.send_join_id_and_pw_for_join_access(join_username, join_pw, join_nickname)

    #회원가입 아이디 중복체크
    def username_duplicatecheck(self, assert_username):
        self.client_app.send_username_duplicatecheck(assert_username)

        pass

    # 회원가입=============================================================================

    # 유저가 아이디 비밀번호를 입력하고 로그인버튼 클릭시
    def assert_login_data(self, usr_inp_name, usr_inp_pw):
        self.client_app.username = usr_inp_name
        self.client_app.user_pw = usr_inp_pw
        self.client_app.send_login_id_and_pw_for_login_access(usr_inp_name, usr_inp_pw)
        # self.client_app.user_id = None
        # self.client_app.user_nickname = None

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
