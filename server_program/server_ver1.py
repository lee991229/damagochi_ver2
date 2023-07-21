import sys

from code.domain.class_db_connector import DBConnector
from server_program.class_server import Server

if __name__ == '__main__':
    conn = DBConnector()
    conn.create_tables()
    # item_test = ['item_name', 'hunger', 'affection', 'health', 'exp']
    item_list = [['1번 아이템', 10, 10, 0, 0],['2번 아이템', 10, 10, 0, 0]]

    # item_dict = list()
    # for i in range(len(item_list)):
    #     item_dict.append(dict(zip(item_test,item_list[i])))
    # print(item_dict)
    for i in item_list:
        conn.item_sign_up(i)
    # item_id, item_name, hunger, affection, health, exp
    server = Server(conn)
    server.start()
