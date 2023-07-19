import datetime
import socket
import time
from threading import *

# 사용할 구분자
header_split = chr(1)
list_split_1 = chr(2)
list_split_2 = chr(3)


class ClientApp:
    HOST = '127.0.0.12'
    PORT = 9999
    BUFFER = 50000
    FORMAT = "utf-8"
    HEADER_LENGTH = 30

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))
        self.client_widget = None

        # 로그인한 유저 정보 저장
        self.user_id = None
        self.user_pw = None
        self.username = None
        self.user_nickname = None

        # 클라이언트 recv 스레드
        self.receive_thread = Thread(target=self.receive_message)
        self.receive_thread.daemon = True
        self.receive_thread.start()
    def send_join_id_and_pw_for_join_access(self, join_username, join_pw, join_nickname):
        client_sand_data = f"{f'join_access{header_split}{join_username}{list_split_1}{join_pw}{list_split_1}{join_nickname}':{self.BUFFER}}".encode(self.FORMAT)
        self.client_socket.send(client_sand_data)

    def set_widget(self, widget_):
        self.client_widget = widget_

    def send_username_duplicatecheck(self, join_inp_username):
        print(join_inp_username, '3')
        client_sand_data = f"{f'assertu_username{header_split}{join_inp_username}':{self.BUFFER}}".encode(self.FORMAT)
        self.client_socket.send(client_sand_data)

    def send_login_id_and_pw_for_login_access(self, login_username, login_pw):
        client_sand_data = f"{f'login{header_split}{login_username}{list_split_1}{login_pw}':{self.BUFFER}}".encode(
            self.FORMAT)
        self.client_socket.send(client_sand_data)

    def receive_message(self):
        while True:
            return_result = self.client_socket.recv(self.BUFFER).decode(self.FORMAT).strip()
            print(return_result)
            response_header = return_result.split(header_split)[0]
            response_substance = return_result.split(header_split)[1]

            if response_header == 'assertu_username':  # 로그인
                if response_substance == 'True':
                    self.client_widget.assert_same_id_signal.emit(True)
                else:
                    self.client_widget.assert_same_id_signal.emit(False)
