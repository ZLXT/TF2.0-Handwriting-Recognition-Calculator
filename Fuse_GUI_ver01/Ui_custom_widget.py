# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ZLXT\Desktop\custom\custom_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 640)
        Form.setMinimumSize(QtCore.QSize(1200, 640))
        Form.setMaximumSize(QtCore.QSize(1200, 640))
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 1179, 602))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.painboard = PaintBoard(self.layoutWidget)
        self.painboard.setMinimumSize(QtCore.QSize(1024, 512))
        self.painboard.setMaximumSize(QtCore.QSize(1024, 512))
        self.painboard.setStyleSheet("border:2px solid rgb(170, 0, 255);")
        self.painboard.setObjectName("painboard")
        self.verticalLayout_2.addWidget(self.painboard)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.func_label = QtWidgets.QLabel(self.layoutWidget)
        self.func_label.setMinimumSize(QtCore.QSize(1024, 35))
        self.func_label.setMaximumSize(QtCore.QSize(1024, 35))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.func_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.func_label.setFont(font)
        self.func_label.setAcceptDrops(False)
        self.func_label.setStyleSheet("color: rgb(255, 0, 0);\n"
"border:2px solid rgb(0, 170, 255);\n"
"")
        self.func_label.setScaledContents(False)
        self.func_label.setObjectName("func_label")
        self.verticalLayout.addWidget(self.func_label)
        self.res_label = QtWidgets.QLabel(self.layoutWidget)
        self.res_label.setMinimumSize(QtCore.QSize(1024, 35))
        self.res_label.setMaximumSize(QtCore.QSize(1024, 35))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.res_label.setFont(font)
        self.res_label.setStyleSheet("color: rgb(255, 0, 0);\n"
"border:2px solid rgb(0, 170, 255);")
        self.res_label.setObjectName("res_label")
        self.verticalLayout.addWidget(self.res_label)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pic_label = QtWidgets.QLabel(self.layoutWidget)
        self.pic_label.setMinimumSize(QtCore.QSize(140, 140))
        self.pic_label.setMaximumSize(QtCore.QSize(140, 140))
        self.pic_label.setStyleSheet("border:2px solid rgb(170, 0, 255);")
        self.pic_label.setText("")
        self.pic_label.setObjectName("pic_label")
        self.verticalLayout_3.addWidget(self.pic_label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.formLayout.setObjectName("formLayout")
        self.Next_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Next_button.setFont(font)
        self.Next_button.setObjectName("Next_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Next_button)
        self.clean_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clean_button.setFont(font)
        self.clean_button.setObjectName("clean_button")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.clean_button)
        self.use_model_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.use_model_button.setFont(font)
        self.use_model_button.setObjectName("use_model_button")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.use_model_button)
        self.eraser_check = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.eraser_check.setFont(font)
        self.eraser_check.setToolTipDuration(-1)
        self.eraser_check.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.eraser_check.setAutoFillBackground(False)
        self.eraser_check.setIconSize(QtCore.QSize(30, 30))
        self.eraser_check.setAutoRepeat(False)
        self.eraser_check.setAutoExclusive(False)
        self.eraser_check.setAutoRepeatInterval(100)
        self.eraser_check.setTristate(False)
        self.eraser_check.setObjectName("eraser_check")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.eraser_check)
        self.eraser_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.eraser_label.setFont(font)
        self.eraser_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.eraser_label.setObjectName("eraser_label")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.eraser_label)
        self.eraser_spinbox = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.eraser_spinbox.setFont(font)
        self.eraser_spinbox.setMinimum(10)
        self.eraser_spinbox.setMaximum(80)
        self.eraser_spinbox.setSingleStep(2)
        self.eraser_spinbox.setProperty("value", 20)
        self.eraser_spinbox.setObjectName("eraser_spinbox")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.eraser_spinbox)
        spacerItem = QtWidgets.QSpacerItem(40, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        self.clean_button.clicked.connect(Form.clean_draw)
        self.use_model_button.clicked.connect(Form.use_model)
        self.eraser_check.stateChanged['int'].connect(Form.eraser)
        self.eraser_spinbox.valueChanged['int'].connect(Form.change_eraser_size)
        self.Next_button.clicked.connect(Form.next_pic)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Draw_Window"))
        self.func_label.setText(_translate("Form", "公式为:None"))
        self.res_label.setText(_translate("Form", "结果为:None"))
        self.Next_button.setText(_translate("Form", "Next"))
        self.clean_button.setText(_translate("Form", "清空绘板"))
        self.use_model_button.setText(_translate("Form", "识别"))
        self.eraser_check.setText(_translate("Form", "橡皮"))
        self.eraser_label.setText(_translate("Form", "橡皮大小"))
from PaintBoard import PaintBoard
