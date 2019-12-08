import sys
from picreader import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
from PyQt5 import QtCore
from PyQt5.QtGui import QImage,QPixmap
import cv2
import numpy as np

class MyMainWin(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainWin,self).__init__(parent)
        self.setupUi(self)
        self.addWinaction.triggered.connect(self.openmsg)
        self.pushButton.clicked.connect(self.openmsg)
        self.pushButton_2.clicked.connect(self.exit)
        self.pushButton_3.clicked.connect(self.hsv)

    def openmsg(self):
        global file
        file,_ = QFileDialog.getOpenFileName(self, '打开', 'C:/Users/admin/PycharmProjects/MyCV/cv', 'Files (*.jpg *.png)')
        if file:
            self.statusbar.showMessage(file)
            img = QImage(file)
            width = img.width()
            height = img.height()
            if width / self.label.width() >= height / self.label.height():
                ratio = width / self.label.width()
            else:
                ratio = height / self.label.height()
            global new_height,new_img,new_width
            new_width = width / ratio
            new_height = height / ratio
            new_img = img.scaled(new_width, new_height)
            self.label.setPixmap(QPixmap.fromImage(new_img))
    def hsv(self):

        img = cv2.imread(file)
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        lower_blue = np.array([0, 50, 50])
        upper_blue = np.array([50, 255, 255])

        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        res = cv2.bitwise_and(img, img, mask=mask)
        cv2.namedWindow('res',cv2.WINDOW_KEEPRATIO)
        cv2.imshow('res',res)
        cv2.resizeWindow('res',800,600)

    def exit(self):
        app = QApplication.instance()
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWin()
    myWin.show()
    sys.exit(app.exec_())