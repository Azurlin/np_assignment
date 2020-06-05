# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Show.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from pandas import DataFrame
import pandas as pd
'''
class MyEditForm(QMainWindow, Ui_FormE):
     def __init__(self, parent=None):
        super(MyEditForm, self).__init__(parent) 
        self.setupUi(self)
'''     
class Ui_Form(object):
    def setupUi(self, Form):
        self.coutlist = []
        self.filePath = 'info_class.xlsx'         
        self.queryItem = ['number','name','gender','age','phone','address'] 
        Form.setObjectName("查询窗口")
        Form.resize(966, 697)
        self.chooseBox = QtWidgets.QComboBox(Form)
        self.chooseBox.setGeometry(QtCore.QRect(160, 30, 101, 31))
        self.chooseBox.setObjectName("chooseBox")
        self.chooseBox.addItem("")
        self.chooseBox.addItem("")
        self.chooseBox.addItem("")
        self.chooseBox.addItem("")
        self.chooseBox.addItem("")
        self.chooseBox.addItem("")
        self.inputContext = QtWidgets.QLineEdit(Form)
        self.inputContext.setGeometry(QtCore.QRect(310, 30, 281, 31))
        self.inputContext.setText("")
        self.inputContext.setObjectName("inputContext")
        self.queryButton = QtWidgets.QPushButton(Form)
        self.queryButton.setGeometry(QtCore.QRect(640, 30, 101, 31))
        self.queryButton.setObjectName("queryButton")
        self.table = QtWidgets.QTableWidget(Form)
        self.table.setGeometry(QtCore.QRect(80, 90, 801, 521))
        self.table.setObjectName("table")
        self.table.setColumnCount(6)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        self.insertButton = QtWidgets.QPushButton(Form)
        self.insertButton.setGeometry(QtCore.QRect(270, 640, 93, 28))
        self.insertButton.setObjectName("insertButton")
        self.delButton = QtWidgets.QPushButton(Form)
        self.delButton.setGeometry(QtCore.QRect(430, 640, 93, 28))
        self.delButton.setObjectName("delButton")
        self.updateButton = QtWidgets.QPushButton(Form)
        self.updateButton.setGeometry(QtCore.QRect(590, 640, 93, 28))
        self.updateButton.setObjectName("updateButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "查询窗口"))
        self.chooseBox.setItemText(0, _translate("Form", "学号"))
        self.chooseBox.setItemText(1, _translate("Form", "姓名"))
        self.chooseBox.setItemText(2, _translate("Form", "性别"))
        self.chooseBox.setItemText(3, _translate("Form", "年龄"))
        self.chooseBox.setItemText(4, _translate("Form", "联系方式"))
        self.chooseBox.setItemText(5, _translate("Form", "地址"))
        self.queryButton.setText(_translate("Form", "查询"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "学号"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "姓名"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "性别"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "年龄"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("Form", "联系方式"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("Form", "地址"))
        self.insertButton.setText(_translate("Form", "添加"))
        self.delButton.setText(_translate("Form", "删除"))
        self.updateButton.setText(_translate("Form", "更新"))
        self.showInfo()
        #添加事件监听
        self.queryButton.clicked.connect(self.queryInfo)
        self.delButton.clicked.connect(self.delInfo)
        self.updateButton.clicked.connect(self.modifyInfo_after)
        self.table.doubleClicked.connect(self.modifyInfo_before)
       # self.insertButton.clicked.connect(self.insertInfo)
    #初始化展示列表    
    def showInfo(self):
        data = pd.read_excel(self.filePath,sheet_name="Sheet1")       
        for i in range(data.shape[0]):
            row = self.table.rowCount()
            self.table.insertRow(row)
            for j in range(len(self.queryItem)):
                #print(data[self.queryItem[j]][i])
                item = QTableWidgetItem(str(data[self.queryItem[j]][i]))   
                self.table.setItem(row, j, item)
    #查询-----下拉框选择项 输入对应值查询
    def queryInfo(self):
        try:
            source = self.inputContext.text() #获取输入框值
            it = self.chooseBox.currentText() #获取下拉框值
        except:
            print("err")
        for i in range(self.table.rowCount()):
            self.table.removeRow(0) #清空列表                       
        data = pd.read_excel(self.filePath,sheet_name="Sheet1")       
        itItem = {'学号':'number','姓名':'name','性别':'gender','年龄':'age','联系方式':'phone','地址':'address'}
        for i in range(data.shape[1]):
            try:
                if(str(data[itItem[it]][i]) == str(source)):
                    row = self.table.rowCount()
                    self.table.insertRow(row)                
                    for j in range(len(self.queryItem)):
                        item = QTableWidgetItem(str(data[self.queryItem[j]][i]))   
                        self.table.setItem(row, j, item)
            except:
                print("---")
                
    #删除------删除选中行
    def delInfo(self):
        data = pd.read_excel(self.filePath,sheet_name="Sheet1")
        selectrow = self.table.selectedItems()[0].row() #获取行数
        contents = self.table.item(selectrow,0).text() # 获取 选中 行 获取学号
        for i in range(data.shape[0]):
            if str(data['number'][i]) == str(contents):
                data = data.drop(i, axis=0) #从数据表中删除
                self.table.removeRow(selectrow)#从列表中删除
        data.to_excel(self.filePath, sheet_name='Sheet1', index=False, header=True)  #保存修改后的额内容           
    #刷新列表  
    def updateInfo(self):
        for i in range(self.table.rowCount()):
            self.table.removeRow(0)
        self.showInfo()
    #修改数据 --- 记录双击的行号列号存在列表中 可以同时修改多条 修改完成后点击更新保存
    def modifyInfo_after(self):
        data = pd.read_excel(self.filePath,sheet_name="Sheet1")  
        for i in range(len(self.coutlist)):
            contents = self.table.item(self.coutlist[i][0],self.coutlist[i][1]).text()
            data.iloc[self.coutlist[i][0],self.coutlist[i][1]] = contents
        data.to_excel(self.filePath, sheet_name='Sheet1', index=False, header=True)  #保存修改后的额内容
        self.coutlist = []
        self.updateInfo()
    #双击监听保存行列
    def modifyInfo_before(self):
        selectrow = self.table.selectedItems()[0].row() #获取行数
        selectcolum = self.table.selectedItems()[0].column() #获取列数
        rclist = [selectrow,selectcolum]#记录行号列号 
        self.coutlist.append(rclist)
        
        
        
