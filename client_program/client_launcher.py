import sys
import time

from PyQt5.QtWidgets import QApplication

from client_program.client_config import ClientConfigure
from code.front.client_controller import ClientController
from common.common_module import *
from network.class_client import ClientApp

if __name__ == '__main__':
    # damagochi_client = ClientApp()
    # configure = ClientConfigure()
    # damagochi_client.set_config(configure)
    # damagochi_client.start()
    app = QApplication(sys.argv)

    client_object = ClientApp()

    client_controller = ClientController(client_object)

    client_controller.run()

    sys.excepthook = lambda exctype, value, traceback: show_error_message(str(value), traceback)

    sys.exit(app.exec_())
    # time.sleep(10)
    # kkotalk_client.exit()
