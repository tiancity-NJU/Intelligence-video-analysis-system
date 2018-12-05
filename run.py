from UI.ui_window import ui
import sys
import os
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow

# sys.path.append("/data/szk/PycharmProjects/IVAN_v2")

#os.environ["CUDA_VISIBLE_DEVICES"] = "3"

if __name__ == '__main__':

    # a=cv2.imread('/home/yxy/Pictures/0.jpg')
    # # cv2.imshow('Y',a)
    # cv2.waitKey(0)
    app = QApplication(sys.argv)
    mainWindow = ui()
    mainWindow.show()
    sys.exit(app.exec_())
