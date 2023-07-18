import os
import sys

if __name__ == '__main__':
    os.system(f"pyrcc5 ../src_img/my_qrc.qrc -o my_qrc_rc.py")

    uis = ['main_widget_damagochi_ver2', '']
    for ui in uis:
        # os.system(f'python  -m PyQt5.uic.pyuic --from-imports -x {ui}.ui -o ui_class_{ui}.py')
        os.system(f'python  -m PyQt5.uic.pyuic --import-from=code.front.ui -x {ui}.ui -o ui_class_{ui}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name2}.ui -o {name2}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name3}.ui -o {name3}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name6}.ui -o {name6}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name7}.ui -o {name7}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name4}.ui -o {name4}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name5}.ui -o {name5}.py')
    # os.system(f'python -m PyQt5.uic.pyuic -x {name3}.ui -o {name3}.py')
