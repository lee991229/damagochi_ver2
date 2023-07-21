from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from code.front.ui.ui_class_main_widget_damagochi_ver2 import Ui_frame_damagochi
from code.front.widget_chat_room import ChatRoom
from code.front.widget_menu import UiDialogMenu

from code.front.widget_shop_item import shop_widget


def menu_dialog(screen):
    mywindow2 = UiDialogMenu(screen)  # 캐릭터 버튼 프래스 이밴트 다이얼 로그
    mywindow2.exec()


# def chat_room(screen):
#     mywindow3 = ChatRoom(screen)  # 캐릭터 버튼 프래스 이밴트 다이얼 로그
#     mywindow3.show()

class Screen(QWidget, Ui_frame_damagochi):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.shop_widget = shop_widget
        self.chat_room = ChatRoom(self)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.client_controller = client_controller
        self.set_btn_trigger()  # 버튼 시그널 받는 메서드
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 저장
        self.join_username = None
        self.join_pw = None
        self.join_usernickname = None

    def mousePressEvent(self, event):
        self.client_controller.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        self.client_controller.mouseMoveEvent(self, event)

    # 버튼 시그널 메서드
    def set_btn_trigger(self):
        self.btn_login.clicked.connect(lambda state: self.assert_login())
        self.btn_join.clicked.connect(lambda state: self.join_screen())
        self.btn_join_duplicatecheck.clicked.connect(lambda state: self.user_name_duplicate_check())
        self.btn_join_register.clicked.connect(lambda state: self.register_event())
        self.btn_join_cancel.clicked.connect(lambda state: self.login_screen())
        # 게임 화면 버튼
        self.btn_shop.clicked.connect(lambda state: (self.shop_screen(), self.client_controller.get_shop_item_list()))
        self.btn_menu.clicked.connect(lambda state: (menu_dialog(self)))

        pass

    # 채팅방 관련 함수=====================================================================
    def chat_input(self):
        pass

    # 메뉴 다이얼 로그 이벤트============================================================

    def show_chat_room(self):
        self.chat_room.show()
        print('채팅방이 열려요')

    def game_logout(self):
        self.login_screen()
        # todo: 클라이언트에 저장된 유저정보 초기화
        print('로그아웃해요')

    # 화면 전환===================================================================================================
    # 로그인 화면 전환
    def login_screen(self):
        self.stackedWidget_damagochi.setCurrentWidget(self.stackedwidget_page_1)

    # 게임 화면 전환
    def widget_game_screen(self):

        self.stackedWidget_damagochi.setCurrentWidget(self.stackedwidget_page_3)

    # 회원 가입 화면 전환
    def join_screen(self):
        self.stackedWidget_damagochi.setCurrentWidget(self.stackedwidget_page_2)

    def shop_screen(self):
        self.stackedWidget_damagochi.setCurrentWidget(self.stackedwidget_page_4)

    # =====회원가입==========================================================================================================

    # 유저 아이디 중복 체크
    def user_name_duplicate_check(self):
        assert_username = self.lineEdit_join_username.text()
        if assert_username != '':
            self.client_controller.username_duplicatecheck(assert_username)
        else:
            self.user_name_duplicate_check_true("(사용불가)ID:")

    # 아이디 중복체크후 라벨에 결과 보여주기
    def user_name_duplicate_check_true(self, text):
        self.label.setText(text)

    # 이름 확인
    def assert_not_blank_nickname(self):
        choice_nickname = self.lineEdit_join_nickname.text()
        if choice_nickname != "":
            return True
        else:
            return False

    # 패스워드 확인
    def assert_same_password(self):
        reconfirm_pw = self.lineedit_join_pw_2.text()
        pw = self.lineedit_join_pw_1.text()
        if pw == reconfirm_pw and pw != "":  # 비밀 번호와 비밀 번호 확인이 일치하면
            return True
        else:
            return False

    def show_label_join_warning(self, text):
        self.label_join_warning.setText(text)

    # 회원가입
    def register_event(self):
        if self.client_controller.valid_duplication_id is False:
            self.show_label_join_warning('아이디 중복체크를 해주세요')
            return
        elif self.assert_same_password() is False:  # 비밀번호 비밀번호 확인 비교
            self.show_label_join_warning('비밀번호를 확인 하세요')
            return
        elif self.assert_not_blank_nickname() is False:  # 사용 가능 닉네임 검사
            self.show_label_join_warning('이름을 확인하세요')
            return
        else:
            self.client_controller.join_access()

    # =====회원가입==========================================================================================================

    # 로그인 버튼

    def assert_login(self):
        usr_inp_name = self.line_edit_id.text()
        usr_inp_pw = self.line_edit_pw.text()
        # if len(usr_inp_name) == 0:  # 아이디 칸이 비어 있거나 잘못 적었을때
        #     self.no_input_id()
        #     return
        # elif len(usr_inp_pw) == 0:  # 비밀 번호 칸이 비어 있거나 잘못 적었을때
        #     self.no_input_pw()
        #     return

        self.client_controller.assert_login_data(usr_inp_name, usr_inp_pw)

    # 게임화면=============================================================================
    def set_character_progressBar(self, bar1, bar2):
        self.progressBar.setValue(bar1)
        self.progressBar_2.setValue(bar2)

    def set_shop_widget(self, items_list):
        for i in items_list:
            item_widget = self.shop_widget(i)
            self.verticalLayout_19.addWidget(item_widget)
