# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Edit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pandas import DataFrame
import pandas as pd
class Ui_Dialog(object):
    def setupUi(self, Form):
        self.filePath = 'info_class.xlsx'
        self.queryItem = ['number','name','gender','age','phone','address']
        Form.setObjectName("编辑窗口")
        Form.resize(624, 376)
        self.numberInp = QtWidgets.QLineEdit(Form)
        self.numberInp.setGeometry(QtCore.QRect(270, 30, 161, 31))
        self.numberInp.setObjectName("numberInp")
        self.nameInp = QtWidgets.QLineEdit(Form)
        self.nameInp.setGeometry(QtCore.QRect(270, 70, 161, 31))
        self.nameInp.setObjectName("nameInp")
        self.genderInp = QtWidgets.QLineEdit(Form)
        self.genderInp.setGeometry(QtCore.QRect(270, 110, 161, 31))
        self.genderInp.setObjectName("genderInp")
        self.ageInp = QtWidgets.QLineEdit(Form)
        self.ageInp.setGeometry(QtCore.QRect(270, 150, 161, 31))
        self.ageInp.setObjectName("ageInp")
        self.phoneInp = QtWidgets.QLineEdit(Form)
        self.phoneInp.setGeometry(QtCore.QRect(270, 190, 161, 31))
        self.phoneInp.setObjectName("phoneInp")
        self.addressInp = QtWidgets.QLineEdit(Form)
        self.addressInp.setGeometry(QtCore.QRect(270, 230, 161, 31))
        self.addressInp.setObjectName("addressInp")
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(250, 310, 93, 28))
        self.addButton.setObjectName("addButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 30, 51, 31))
        self.label.setStyleSheet("font: 14pt \"Adobe 黑体 Std R\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 70, 51, 31))
        self.label_2.setStyleSheet("font: 14pt \"Adobe 黑体 Std R\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 110, 51, 31))
        self.label_3.setStyleSheet("font: 14pt \"Adobe 黑体 Std R\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(200, 150, 51, 31))
        self.label_4.setStyleSheet("font: 14pt \"Adobe 黑体 Std R\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(160, 190, 91, 31))
        self.label_5.setStyleSheet("font: 14pt \"Adobe 黑体 Std R\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(160, 230, 91, 31))
        self.label_6.setStyleSheet("font: 14pt \"Adobe 黑体 Std R\";")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "添加数据"))
        self.addButton.setText(_translate("Form", "添加"))
        self.label.setText(_translate("Form", "学号"))
        self.label_2.setText(_translate("Form", "姓名"))
        self.label_3.setText(_translate("Form", "性别"))
        self.label_4.setText(_translate("Form", "年龄"))
        self.label_5.setText(_translate("Form", "联系方式"))
        self.label_6.setText(_translate("Form", "家庭地址"))
        
        self.addButton.clicked.connect(self.addInfo)
        
    def addInfo(self):
        df = pd.read_excel(self.filePath,sheet_name="Sheet1")
        df.loc[df.shape[0]] = {'number':self.numberInp.text(),
                              'name':self.nameInp.text(),
                              'gender':self.genderInp.text(),
                              'age':self.ageInp.text(),
                              'phone':self.phoneInp.text(),
                              'address':self.addressInp.text()
                              }
        df.to_excel(self.filePath, sheet_name='Sheet1', index=False, header=True)
        
        self.accept()
