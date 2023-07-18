import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPoint, Qt, pyqtSignal

from code.front.ui.ui_class_main_widget_damagochi_ver2 import Ui_frame_damagochi
from network.class_client import ClientApp
from code.front.widget_screen import Screen


class ClientController(QtWidgets.QWidget):
    def __init__(self, client_app=ClientApp):
        super().__init__()
        self.client_app = client_app
        self.client_app.set_widget(self)
        self.widget_screen = Screen(self)

        # ui 동작 관련 변수
        self.list_widget_geometry_x = None
        self.list_widget_geometry_y = None
        self.drag_start_position = QPoint(0, 0)

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
