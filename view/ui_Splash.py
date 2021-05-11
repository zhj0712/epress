# ************************************
# *编码: utf-8 
# *作者: 周俊                     
# *文件名: ui_Splash.py                
# *创建时间: 2021-05-02 23:14 
# *功能说明:  
# *版本: V1.0
# *更新时间: 
# ************************************

from PyQt5 import QtCore, QtWidgets

class Ui_Form_load(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(633, 426)
        Form.setStyleSheet("")
        self.prg = QtWidgets.QProgressBar(Form)
        self.prg.setGeometry(QtCore.QRect(20, 360, 591, 8))
        self.prg.setStyleSheet("")
        self.prg.setProperty("value", 27)
        self.prg.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.prg.setTextVisible(False)
        self.prg.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.prg.setObjectName("prg")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 0, 591, 411))
        self.label.setStyleSheet("image: url(img/111.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lab1 = QtWidgets.QLabel(Form)
        self.lab1.setGeometry(QtCore.QRect(30, 340, 141, 16))
        self.lab1.setStyleSheet("color: rgb(255, 255, 255);")
        self.lab1.setObjectName("lab1")
        self.label.raise_()
        self.prg.raise_()
        self.lab1.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lab1.setText(_translate("Form", "正在加载...100%"))

