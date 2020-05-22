from Ui_custom_widget import Ui_Form
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
import Vertical_Projection as vp
import Change_Size as cs
import Use_Model as um
import Calculator as cal
from PIL import Image, ImageQt
from cv2 import cv2
import numpy as np
import os


class Window(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.num = 0
        self.cut_picture = []
        self.pic_input = []
        self.output_lab = []
        self.result = 0
        self.equation = ""

    def clean_draw(self):
        self.painboard.Clear()
        self.num = 0
        self.cut_picture = []
        self.pic_input = []
        self.output_lab = []
        self.result = 0
        self.equation = ""
        self.pic_label.setPixmap(QPixmap(""))
        self.func_label.setText("公式为:None")
        self.res_label.setText("结果为:None")
        imagelist = os.listdir('./pic/')
        for i in range(0,len(imagelist)):
            jpg_path = './pic/' + imagelist[i]
            os.remove(jpg_path)
    def use_model(self):
        if self.painboard.IsEmpty() == False:
            #print("ok")
            image = self.painboard.GetContentAsQImage()#图片为QImage类型
            image = ImageQt.fromqimage(image)#转为PIL.image类型
            image = np.asarray(image)#转换为cv2类型
            self.cut_picture = vp.Vertical_Projection(image)#将图像进行分割为单个
            self.pic_input = cs.Change_Size(self.cut_picture)#将图片改为28*28像素大小
            self.output_lab = um.Use_Model(self.pic_input)#加载模型并使用模型进行预测
            self.result,self.equation = cal.Calculator(self.output_lab)#输出识别公式和结果
            self.func_label.setText("公式为:" + self.equation)
            self.res_label.setText("结果为:" + str(self.result))
            self.next_pic()
        else :
            #print("no")
            pass

    def eraser(self):
        if self.eraser_check.isChecked():
            self.painboard.EraserMode = True #进入橡皮擦模式
        else:
            self.painboard.EraserMode = False 

    def change_eraser_size(self):
        penThickness = self.eraser_spinbox.value()
        self.painboard.ChangePenThickness(penThickness)

    def next_pic(self):
        if self.pic_input:
            imagelist = os.listdir('./pic/')
            jpg_path = './pic/' + imagelist[self.num]
            jpg = QtGui.QPixmap(jpg_path).scaled(self.pic_label.width(), self.pic_label.height())
            self.pic_label.setPixmap(jpg)
            self.pic_label.setScaledContents(True)
            if self.num == (len(self.pic_input)-1):
                self.num = 0
            else:
                self.num += 1
        else:
            pass



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv) 

    window = Window()
    window.show()  
    exit(app.exec_())