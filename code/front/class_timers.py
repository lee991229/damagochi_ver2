from PyQt5.QtCore import QTimer
import random


def make_timer(time):
    t = QTimer()
    # print(id(t))
    # print(type(t))
    t.setInterval(time)
    return t

class TmierClass():
    def __init__(self, client_controller):
        self.client_controller = client_controller

        self.timer1 = make_timer(time=5000)
        self.timer1.timeout.connect(lambda x=None, wash=0: (
            self.client_controller.character_timer_event()))  # dirty_stat 메서드를 발동해 더러움 수치에 따라 질병에 걸릴수 있다 character_stat_data에 더러움 스탯을 저장
