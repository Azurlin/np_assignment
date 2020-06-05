# -*- coding: utf-8 -*-
import sys
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog
#导入designer工具生成的login模块
from Ui_Show import Ui_Form
from Ui_Edit import Ui_Dialog
  
class MyMainForm(QMainWindow, Ui_Form):
     def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent) 
        self.setupUi(self)
class ChildWindow(QDialog,Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
     #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
     app = QApplication(sys.argv)
     #初始化
     myWin = MyMainForm()
     child = ChildWindow()  

     btn=myWin.insertButton
     btn.clicked.connect(child.show)
     
     btn2 = child.addButton
     btn2.clicked.connect(myWin.updateInfo) 
  
     #将窗口控件显示在屏幕上
     myWin.show()
     #程序运行，sys.exit方法确保程序完整退出。
     sys.exit(app.exec_())


