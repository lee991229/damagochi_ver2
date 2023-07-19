import os
from multiprocessing import Process
from socket import *
from threading import Thread, Event
# from Common.class_json import *

import select

from code.domain.class_db_connector import DBConnector
from common.class_json import *

# from Code.domain.class_db_connector import DBConnector
# 사용할 구분자
header_split = chr(1)
list_split_1 = chr(2)
list_split_2 = chr(3)


class Server:
    HOST = '127.0.0.12'
    PORT = 9999
    BUFFER = 50000
    FORMAT = "utf-8"
    HEADER_LENGTH = 30

    # assert_username = f"{'assert_username':<{HEADER_LENGTH}}"
    # join_user = f"{'join_user':<{HEADER_LENGTH}}"
    # login = f"{'login':<{HEADER_LENGTH}}"
    # enter_square = f"{'enter_square':<{HEADER_LENGTH}}"
    # all_user_list = f"{'all_user_list':<{HEADER_LENGTH}}"
    # user_talk_room_list = f"{'user_talk_room_list':<{HEADER_LENGTH}}"
    # talk_room_user_list_se = f"{'talk_room_user_list_se':<{HEADER_LENGTH}}"
    # out_talk_room = f"{'out_talk_room':<{HEADER_LENGTH}}"
    # send_msg_se = f"{'send_msg_se':<{HEADER_LENGTH}}"
    # invite_user_talk_room = f"{'invite_user_talk_room':<{HEADER_LENGTH}}"
    # make_talk_room = f"{'make_talk_room':<{HEADER_LENGTH}}"
    # talk_room_msg = f"{'talk_room_msg':<{HEADER_LENGTH}}"
    # pass_encoded = f"{'pass':<{BUFFER - HEADER_LENGTH}}".encode(FORMAT)
    # dot_encoded = f"{'.':<{BUFFER - HEADER_LENGTH}}".encode(FORMAT)

    def __init__(self, db_conn: DBConnector):
        # 서버 소켓 설정
        self.db_conn = db_conn
        self.server_socket = None
        self.config = None
        self.sockets_list = list()
        self.clients = dict()
        self.thread_for_run = None
        self.run_signal = True

        self.decoder = KKODecoder()
        self.encoder = KKOEncoder()

    def set_config(self, configure):
        self.config = configure
        print('서버 설정 적용됨')

    def start(self):
        if self.thread_for_run is not None:  # 실행중이면 종료 시키기
            return
        self.server_socket = socket(AF_INET, SOCK_STREAM)  # AF_INET(ipv4를 의미)
        self.server_socket.bind((self.HOST, self.PORT))  # 바인딩
        self.server_socket.listen()  # 리슨 시작
        self.sockets_list.clear()  # 소켓리스트 클리어
        self.sockets_list.append(self.server_socket)
        self.run_signal = True
        self.thread_for_run = Thread(target=self.run)
        self.thread_for_run.start()

    def stop(self):
        self.run_signal = False
        if self.thread_for_run is not None:
            self.thread_for_run.join()
        self.server_socket.close()
        self.thread_for_run = None

    def run(self):
        while True:
            if self.run_signal is False:
                break
            try:
                read_sockets, _, exception_sockets = select.select(self.sockets_list, [], self.sockets_list, 0.1)

            except Exception:
                continue

            for notified_socket in read_sockets:
                if notified_socket == self.server_socket:
                    client_socket, client_address = self.server_socket.accept()
                    user = self.receive_message(client_socket)
                    if user is False:
                        continue
                    self.sockets_list.append(client_socket)
                    self.clients[client_socket] = user

                else:
                    message = self.receive_message(notified_socket)

                    if message is False:
                        self.sockets_list.remove(notified_socket)
                        del self.clients[notified_socket]
                        continue

            for notified_socket in exception_sockets:
                self.sockets_list.remove(notified_socket)
                del self.clients[notified_socket]

    def send_message(self, client_socket: socket, result):
        print(f"Server SENDED: ({result})")
        client_socket.send(result)

    def receive_message(self, client_socket: socket, UserTalkRoom=None):
        try:
            recv_message = client_socket.recv(self.BUFFER)
            decode_msg = recv_message.decode(self.FORMAT).strip()
            header = decode_msg.split(header_split)[0]
            substance = decode_msg.split(header_split)[1]
            if header == 'login':  # 로그인
                data = substance.split(list_split_1)
                login_name, login_pw = data
                self.db_conn.user_log_in(login_name, login_pw)

            elif header == 'assertu_username':  # 아이디 중복
                data = substance.split(list_split_1)
                join_username = substance
                result = self.db_conn.assertu_username(join_username)
                if result is True:
                    response_header = f"{f'assertu_username{header_split}{True}':{self.BUFFER}}".encode(self.FORMAT)
                    client_socket.send(response_header)
                elif result is False:
                    response_header = f"{f'assertu_username{header_split}{False}':{self.BUFFER}}".encode(self.FORMAT)
                    client_socket.send(response_header)

            elif header == 'join_access':  # 로그인
                data = substance.split(list_split_1)
                print(data)
                # join_name, join_pw, join_nickname = data
                # print(join_name, join_pw, join_nickname)
                self.db_conn.insert_user(data)
        except:
            return False

    def fixed_volume(self, header, data):
        header_msg = f"{header:<{self.HEADER_LENGTH}}".encode(self.FORMAT)
        data_msg = f"{data:<{self.BUFFER - self.HEADER_LENGTH}}".encode(self.FORMAT)
        return header_msg + data_msg

# import os
# from multiprocessing import Process
# from socket import *
# from threading import Thread, Event
# # from Common.class_json import *
#
# import select
#
# # from Code.domain.class_db_connector import DBConnector
#
#
# class Server:
#     HOST = '127.0.0.1'
#     PORT = 9999
#     BUFFER = 50000
#     FORMAT = "utf-8"
#     HEADER_LENGTH = 30
#
#     # def __init__(self, db_conn: DBConnector):
#     def __init__(self):
#         # 서버 소켓 설정
#         self.server_socket = None
#         self.config = None
#         self.sockets_list = list()
#         self.clients = dict()
#         self.thread_for_run = None
#         self.run_signal = True
#
#         # self.decoder = KKODecoder()
#         # self.encoder = KKOEncoder()
#
#     def set_config(self, configure):
#         self.config = configure
#         print('서버 설정 적용됨')
#
#     def start(self):
#         if self.thread_for_run is not None:  # 실행중이면 종료 시키기
#             return
#         self.server_socket = socket(AF_INET, SOCK_STREAM)  # AF_INET(ipv4를 의미)
#         self.server_socket.bind((self.HOST, self.PORT))  # 바인딩
#         self.server_socket.listen()  # 리슨 시작
#         self.sockets_list.clear()  # 소켓리스트 클리어
#         self.sockets_list.append(self.server_socket)
#         self.run_signal = True
#         self.thread_for_run = Thread(target=self.run)
#         self.thread_for_run.start()
#
#     def stop(self):
#         self.run_signal = False
#         if self.thread_for_run is not None:
#             self.thread_for_run.join()
#         self.server_socket.close()
#         self.thread_for_run = None
#
#     def run(self):
#         while True:
#             if self.run_signal is False:
#                 break
#             try:
#                 read_sockets, _, exception_sockets = select.select(self.sockets_list, [], self.sockets_list, 0.1)
#             except Exception:
#                 continue
#             for notified_socket in read_sockets:
#                 if notified_socket == self.server_socket:
#                     client_socket, client_address = self.server_socket.accept()
#                     user = self.receive_message(client_socket)
#                     if user is False:
#                         continue
#                     self.sockets_list.append(client_socket)
#                     self.clients[client_socket] = user
#
#                 else:
#                     message = self.receive_message(notified_socket)
#
#                     if message is False:
#                         self.sockets_list.remove(notified_socket)
#                         del self.clients[notified_socket]
#                         continue
#
#             for notified_socket in exception_sockets:
#                 self.sockets_list.remove(notified_socket)
#                 del self.clients[notified_socket]
