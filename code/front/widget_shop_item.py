from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from code.front.ui.ui_class_widget_shop import Ui_item_widget


class shop_widget(QWidget, Ui_item_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
