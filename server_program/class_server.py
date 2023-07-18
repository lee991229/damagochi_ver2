import os
from multiprocessing import Process
from socket import *
from threading import Thread, Event
# from Common.class_json import *

import select

# from Code.domain.class_db_connector import DBConnector


class Server:
    HOST = '127.0.0.1'
    PORT = 9999
    BUFFER = 50000
    FORMAT = "utf-8"
    HEADER_LENGTH = 30

    assert_username = f"{'assert_username':<{HEADER_LENGTH}}"
    join_user = f"{'join_user':<{HEADER_LENGTH}}"
    login = f"{'login':<{HEADER_LENGTH}}"
    enter_square = f"{'enter_square':<{HEADER_LENGTH}}"
    all_user_list = f"{'all_user_list':<{HEADER_LENGTH}}"
    user_talk_room_list = f"{'user_talk_room_list':<{HEADER_LENGTH}}"
    talk_room_user_list_se = f"{'talk_room_user_list_se':<{HEADER_LENGTH}}"
    out_talk_room = f"{'out_talk_room':<{HEADER_LENGTH}}"
    send_msg_se = f"{'send_msg_se':<{HEADER_LENGTH}}"
    invite_user_talk_room = f"{'invite_user_talk_room':<{HEADER_LENGTH}}"
    make_talk_room = f"{'make_talk_room':<{HEADER_LENGTH}}"
    talk_room_msg = f"{'talk_room_msg':<{HEADER_LENGTH}}"
    pass_encoded = f"{'pass':<{BUFFER - HEADER_LENGTH}}".encode(FORMAT)
    dot_encoded = f"{'.':<{BUFFER - HEADER_LENGTH}}".encode(FORMAT)

    HEADER_LIST = {
        assert_username: assert_username.encode(FORMAT),
        join_user: join_user.encode(FORMAT),
        login: login.encode(FORMAT),
    }

    def __init__(self):
        # 서버 소켓 설정

        self.server_socket = None
        self.config = None
        self.sockets_list = list()
        self.clients = dict()
        self.thread_for_run = None
        self.run_signal = True

        # self.decoder = KKODecoder()
        # self.encoder = KKOEncoder()

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
            print(recv_message)
            request_header = recv_message[:self.HEADER_LENGTH].strip().decode(self.FORMAT)
            request_data = recv_message[self.HEADER_LENGTH:].strip().decode(self.FORMAT)
            print(f"Server RECEIVED: ({request_header},{request_data})")

            # 아이디 중복
            if request_header == self.assert_username.strip():
                result = self.db_conn.assert_same_login_id(request_data)
                if result is True:
                    response_header = self.assert_username.encode(self.FORMAT)
                    result = response_header + self.pass_encoded
                    self.send_message(client_socket, result)
                elif result is False:
                    response_header = self.assert_username.encode(self.FORMAT)
                    result = response_header + self.dot_encoded
                    self.send_message(client_socket, result)
            # 회원가입
            elif request_header == self.join_user.strip():
                object_ = self.decoder.decode_any(request_data)
                result = self.db_conn.user_sign_up(object_.username, object_.password, object_.nickname)
                if result is False:
                    response_header = self.join_user.encode(self.FORMAT)
                    result = response_header + self.dot_encoded
                    self.send_message(client_socket, result)
                else:
                    response_header = self.join_user.encode(self.FORMAT)
                    result = response_header + self.pass_encoded
                    self.send_message(client_socket, result)
            # 로그인
            elif request_header == self.login.strip():
                object_ = self.decoder.decode_any(request_data)
                result = self.db_conn.user_log_in(object_.username, object_.password)
                if result is False:
                    response_header = self.login.encode(self.FORMAT)
                    result = response_header + self.dot_encoded
                    self.send_message(client_socket, result)
                else:
                    response_header = self.login.encode(self.FORMAT)
                    result_str = result.toJSON()
                    result_data = f"{result_str:<{self.BUFFER - self.HEADER_LENGTH}}".encode(self.FORMAT)
                    result = response_header + result_data
                    self.send_message(client_socket, result)
            # 필수 단톡방 입장
            elif request_header == self.enter_square.strip():
                room = self.db_conn.find_user_by_talk_room_id(1)
                object_ = self.decoder.decode_any(request_data)
                # 해당 톡방에 유저가 이미 존재하는지 확인
                # 리스트가 None값이면 자동으로 유저를 insert되게 한다
                response_header = self.enter_square.encode(self.FORMAT)
                if room is None:
                    object_user_talk_room = UserTalkRoom(None, object_.user_id, 1)
                    self.db_conn.insert_user_talk_room(object_user_talk_room)
                # 최초 입장인지 아닌지
                elif object_ not in room:
                    objcet_ = self.decoder.decode_any(request_data)
                    object_user_talk_room = UserTalkRoom(None, objcet_.user_id, 1)
                    self.db_conn.insert_user_talk_room(object_user_talk_room)
                result = response_header + self.pass_encoded
                self.send_message(client_socket, result)
            # 본인 제외 모든 유저 보내기
            elif request_header == self.all_user_list.strip():
                response_header = self.all_user_list.encode(self.FORMAT)
                object_ = self.decoder.decode_any(request_data)
                result = self.db_conn.find_all_user()
                if result is None:
                    result = response_header + self.dot_encoded
                    self.send_message(client_socket, result)
                else:
                    result_str = self.encoder.encode(result)
                    return_result = result_str.encode(self.FORMAT)
                    result = response_header + return_result
                    self.send_message(client_socket, result)

            # 채팅방 리스트 보내기
            elif request_header == self.user_talk_room_list.strip():
                response_header = self.user_talk_room_list.encode(self.FORMAT)
                object_ = self.decoder.decode_any(request_data)
                result = self.db_conn.find_user_talk_room_by_user_id(object_.user_id)
                room_list = list()
                for i in result:
                    room_list.append(self.db_conn.find_talk_room_by_talk_room_id(i.talk_room_id))
                room_list_str = self.encoder.encode(room_list)
                return_result = room_list_str.encode(self.FORMAT)
                result = response_header + return_result
                self.send_message(client_socket, result)



            # 채팅방 나가기
            elif request_header == self.out_talk_room.strip():
                response_header = self.out_talk_room.encode(self.FORMAT)
                obj_ = self.decoder.decode_any(request_data)
                self.db_conn.delete_user_talk_room_by_user_id_and_talk_room_id(obj_.user_id, obj_.talk_room_id)
                result = response_header + self.pass_encoded
                self.send_message(client_socket, result)

            # 발신자 제외한 해당 채팅방에 있는 모든 클라이언트에게 메시지 전송
            # 메시지 db 저장
            elif request_header == self.send_msg_se.strip():
                response_header = self.send_msg_se.encode(self.FORMAT)
                obj_ = self.decoder.decode_any(request_data)
                # 메시지 내용 db에 저장
                self.db_conn.insert_message(obj_.sender_user_id, obj_.talk_room_id, obj_.send_time_stamp, obj_.contents,
                                            obj_.long_contents_id)
                socket_list = self.sockets_list.copy()
                socket_list.remove(self.server_socket)
                return_result = request_data.encode(self.FORMAT)
                for socket_ in socket_list:
                    result = response_header + return_result
                    self.send_message(socket_, result)

            # 유대 초대 요청
            elif request_header == self.invite_user_talk_room.strip():
                response_header = self.invite_user_talk_room.encode(self.FORMAT)
                obj_ = self.decoder.decode_any(request_data)
                self.db_conn.insert_user_talk_room(obj_)
                result = response_header + self.pass_encoded
                self.send_message(client_socket, result)

            # 방 만들기 요처
            elif request_header == self.make_talk_room.strip():
                response_header = self.make_talk_room.encode(self.FORMAT)
                obj_ = self.decoder.decode_any(request_data) # TalkRoom
                created_talk_room_obj = self.db_conn.insert_talk_room(obj_)
                created_talk_room_obj_str = created_talk_room_obj.toJSON()
                encoded_data = f"{created_talk_room_obj_str:<{self.BUFFER - self.HEADER_LENGTH}}".encode("utf-8")
                result = response_header + encoded_data
                self.send_message(client_socket, result)

            # 톡방에 참여하고 있는 유저 객체 보내기
            elif request_header == self.talk_room_user_list_se.strip():
                obj_ = self.decoder.decode_any(request_data)  # talk room obj
                user_obj_list = self.db_conn.find_user_by_talk_room_id(obj_.talk_room_id)
                if user_obj_list is not None:
                    result = f"{self.talk_room_user_list_se.strip()}%{obj_.talk_room_id}"
                    response_header = f"{result:<{self.HEADER_LENGTH}}".encode(self.FORMAT)
                else:
                    response_header = f"{self.talk_room_user_list_se}".encode(self.FORMAT)
                if user_obj_list is None:
                    result = response_header + self.dot_encoded
                    self.send_message(client_socket, result)
                else:
                    user_obj_list_str = self.encoder.encode(user_obj_list)
                    return_result = f"{user_obj_list_str:<{self.BUFFER - self.HEADER_LENGTH}}".encode(self.FORMAT)
                    result = response_header + return_result
                    self.send_message(client_socket, result)

            # 이전 메시지 불러오기
            elif request_header == self.talk_room_msg.strip():
                response_header = self.talk_room_msg
                obj_ = self.decoder.decode_any(request_data)
                talk_room_id = obj_.talk_room_id
                print(1)

                message_list = self.db_conn.find_message_by_talk_room_id(obj_.talk_room_id)
                temp_list = list()
                for m in message_list:
                    temp_list.append(m.toJSON())

                result_header = f"{self.talk_room_msg.strip()}%{talk_room_id}"
                encoded_header = f"{result_header:<{self.HEADER_LENGTH}}".encode('utf-8')
                import json
                encoded_data = f"{json.dumps(temp_list):<{self.BUFFER - self.HEADER_LENGTH}}".encode('utf-8')
                return_result = encoded_header + encoded_data
                print(2)
                result = encoded_header + return_result
                print(3)
                self.send_message(client_socket, result)
                print(4)
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