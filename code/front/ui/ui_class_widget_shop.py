# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_shop.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_item_widget(object):
    def setupUi(self, item_widget):
        item_widget.setObjectName("item_widget")
        item_widget.resize(520, 100)
        item_widget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(item_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_snack_1 = QtWidgets.QWidget(item_widget)
        self.widget_snack_1.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_snack_1.setMaximumSize(QtCore.QSize(199999, 100))
        self.widget_snack_1.setStyleSheet("")
        self.widget_snack_1.setObjectName("widget_snack_1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_snack_1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(self.widget_snack_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(80, 0))
        self.widget.setMaximumSize(QtCore.QSize(80, 100))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_img = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_img.sizePolicy().hasHeightForWidth())
        self.label_img.setSizePolicy(sizePolicy)
        self.label_img.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_img.setStyleSheet("")
        self.label_img.setText("")
        self.label_img.setPixmap(QtGui.QPixmap(":/newPrefix/mon1.png"))
        self.label_img.setScaledContents(True)
        self.label_img.setObjectName("label_img")
        self.verticalLayout_2.addWidget(self.label_img)
        self.horizontalLayout_3.addWidget(self.widget)
        self.widget_snack_in_widget_1 = QtWidgets.QWidget(self.widget_snack_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_snack_in_widget_1.sizePolicy().hasHeightForWidth())
        self.widget_snack_in_widget_1.setSizePolicy(sizePolicy)
        self.widget_snack_in_widget_1.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_snack_in_widget_1.setStyleSheet("")
        self.widget_snack_in_widget_1.setObjectName("widget_snack_in_widget_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_snack_in_widget_1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_name = QtWidgets.QLabel(self.widget_snack_in_widget_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("")
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_snack_in_widget_1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_stat = QtWidgets.QLabel(self.widget_snack_in_widget_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.label_stat.sizePolicy().hasHeightForWidth())
        self.label_stat.setSizePolicy(sizePolicy)
        self.label_stat.setStyleSheet("border-radius:20px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"")
        self.label_stat.setObjectName("label_stat")
        self.gridLayout.addWidget(self.label_stat, 1, 0, 1, 2)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_3.addWidget(self.widget_snack_in_widget_1)
        self.widget_2 = QtWidgets.QWidget(self.widget_snack_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_use = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_use.sizePolicy().hasHeightForWidth())
        self.btn_use.setSizePolicy(sizePolicy)
        self.btn_use.setStyleSheet("")
        self.btn_use.setObjectName("btn_use")
        self.verticalLayout.addWidget(self.btn_use)
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.verticalLayout_4.addWidget(self.widget_snack_1)

        self.retranslateUi(item_widget)
        QtCore.QMetaObject.connectSlotsByName(item_widget)

    def retranslateUi(self, item_widget):
        _translate = QtCore.QCoreApplication.translate
        item_widget.setWindowTitle(_translate("item_widget", "Form"))
        self.label_name.setText(_translate("item_widget", "아이템 이름"))
        self.label.setText(_translate("item_widget", "보유개수"))
        self.label_stat.setText(_translate("item_widget", "올라가는 수치"))
        self.btn_use.setText(_translate("item_widget", "구매"))
from code.front.ui import my_qrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    item_widget = QtWidgets.QWidget()
    ui = Ui_item_widget()
    ui.setupUi(item_widget)
    item_widget.show()
    sys.exit(app.exec_())
