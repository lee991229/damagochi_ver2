import sys
import time

from PyQt5.QtWidgets import QApplication

from code.front.client_controller import ClientController
from common.common_module import *
from network.class_client2 import ClientApp2

if __name__ == '__main__':
    app = QApplication(sys.argv)

    client_object = ClientApp2()

    client_controller = ClientController(client_object)

    client_controller.run()

    sys.excepthook = lambda exctype, value, traceback: show_error_message(str(value), traceback)

    sys.exit(app.exec_())

