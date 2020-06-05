from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
from fclient import pFtpClient
class pui:
    def login(self):
        root = Tk()
        root.title("请登录")
        def reg():
            '''登录校验'''
            username = user.get()
            passwd = pwd.get()
           # user = len(username)
            #pwd = len(passwd)
            try:
                self.u = pFtpClient(username,passwd)
                root.quit()
                root.destroy()
                ui.pyframe()
            except:
                msg['fg'] = 'red'
                msg.configure(text='登录失败！', fg='red')                  
        # 登录结果提示
        root.geometry('300x200+500+200')
        root.resizable(0,0)
        msg = Label(root, text='')
        msg.pack()  # 跨越两列显示
        
        # 第一行用户名输入框
        user = Label(root, text='用户名：')
        user.pack()
        user = Entry(root)
        user.pack()
        
        # 第二行密码输入框
        pwd = Label(root, text='密码：')
        pwd.pack()
        pwd = Entry(root)
        pwd['show'] = '*'  # 隐藏显示
        pwd.pack()
        
        # 第三行登录按钮
        btn = Frame(root)
        login = Button(btn, text='登录', width=6, command=reg)
        login.grid(row=0, column=0)
        cancel = Button(btn, text='取消', width=6, command=root.quit)
        cancel.grid(row=0, column=1)
        btn.pack()
        
        root.mainloop()
    def pyframe(self):        
        #self.u = pFtpClient()
        self.root = Tk()
        self.root.geometry("600x400+200+50")
        self.root.title('摸鱼网盘')
        self.root.resizable(0,0) #禁止更改窗口大小
        
        self.labelx=Label(self.root)
        self.labelx.pack()
        #主要按钮
        self.buttonx1=Button(self.labelx,text="上级目录",command=self.backDir,font=("宋体",15))
        self.buttonx1.grid(row=1,column=0) #设置按钮在子容器的位置
        self.buttonx2=Button(self.labelx,text="主目录",command=self.backMainDir,font=("宋体",15))
        self.buttonx2.grid(row=1,column=1) #设置按钮在子容器的位置
        self.buttonx3=Button(self.labelx,text="新建目录",command=self.makeNewDir,font=("宋体",15))
        self.buttonx3.grid(row=1,column=2) #设置按钮在子容器的位置
        #self.buttonxdel=Button(self.labelx,text="删除目录",command=self.delDir,font=("宋体",15))
        #self.buttonxdel.grid(row=1,column=3) #设置按钮在子容器的位置        
        #目录显示、输入框
        self.labelpath = Label(self.root)
        self.L1 = Label(self.labelpath, text="目录:")
        self.L1.grid(row=1,column=0)
        self.e = Variable()#绑定变量
        self.E1 = Entry(self.labelpath,textvariable=self.e,bd =2,width=50)
        self.e.set('当前目录')#设置输入框的默认值
        
        self.E1.grid(row=1,column=1)
        self.but=Button(self.labelpath,text="打开目录",command=self.openDir,font=("宋体",10))
        self.but.grid(row=1,column=2) #设置按钮在子容器的位置
        self.but=Button(self.labelpath,text="刷新",command=self.updatetree,font=("宋体",10))
        self.but.grid(row=1,column=3) #设置按钮在子容器的位置
        self.labelpath.pack()
        #文件显示列表       
        self.tree = ttk.Treeview(self.root,columns=['1','2','3','4'],show='headings')
        self.tree.column('1',width=50,anchor='center')
        self.tree.column('2',width=150,anchor='center')
        self.tree.column('3',width=100,anchor='center')
        self.tree.column('4',width=200,anchor='center')
        self.tree.heading('1',text='序号')
        self.tree.heading('2',text='文件名')
        self.tree.heading('3',text='文件大小')
        self.tree.heading('4',text='修改时间')
        self.updatetree()
        self.tree.pack()
        def treeviewClick(event):#获取单击选择的文件名
            print ('单击')
            for item in self.tree.selection():
                self.clickfilename = self.tree.item(item,"values")
                print(self.clickfilename[1])#输出所选行的第一列的值
        def treeviewDoubleClick(event):#用于双击打开文件目录
            print('双击')
            for item in self.tree.selection():
                self.doubleclickfilename = self.tree.item(item,"values")
                print(self.doubleclickfilename[1])#输出所选行的第一列的值
            try:
                self.cwdDir()               
            except:
                print('非目录')
                #pass
            
        self.tree.bind('<ButtonRelease-1>', treeviewClick)#绑定单击事件
        self.tree.bind('<Double-Button-1>', treeviewDoubleClick)#双击事件
        
        self.labelfile = Label(self.root)
        self.buttonx4=Button(self.labelfile,text="下载文件",command=self.downloadFile,font=("宋体",15))
        self.buttonx4.grid(row=1,column=1) #设置按钮在子容器的位置
        self.buttonx5=Button(self.labelfile,text="上传文件",command=self.uploadFile,font=("宋体",15))
        self.buttonx5.grid(row=1,column=2) #设置按钮在子容器的位置
        self.labelfile.pack()
        
        self.root.mainloop()        
    def makeNewDir(self):
        def on_click():
            print(dire.get())
            try:
                self.u.ftp.mkd(dire.get())
            except Exception as e:
                print('创建目录失败'+e)
            self.updatetree()
            dirwin.destroy()
            
        dirwin = Toplevel()
        dirwin.title('新目录')
        dirwin.geometry("300x100+350+200")
        dirl = Label(dirwin,text='输入新的目录名')
        dirl.pack()       
        dire = StringVar()#绑定变量
        dirE = Entry(dirwin,textvariable=dire,bd =2,width=30)
        dirE.pack()
        dirbutton = Button(dirwin,text="确定",command=on_click,font=("宋体",15))
        dirbutton.pack()        
        dirwin.mainloop()         
    def cwdDir(self):#双击切换目录
        path = self.u.ftp.pwd()+'/'+self.doubleclickfilename[1]
        self.u.ftp.cwd(path)
        self.updatetree()
    def openDir(self):#打开目录
        path = self.e.get()
        try:
            self.u.ftp.cwd(path)
        except Exception as e:
            print(e)            
        self.updatetree()
    def backMainDir(self):#返回主目录
        self.u.ftp.cwd('/')
        self.updatetree()
    def backDir(self):#返回上级目录
        self.u.ftp.sendcmd('CDUP')
        self.updatetree()
    def deltree(self):#清空显示的文件列表           
        delx=self.tree.get_children()
        for item in delx:
            self.tree.delete(item)
    def updatetree(self):#更新显示路径和文件显示列表     
        self.deltree()#调用函数清空文件显示列表
        clow = []
        finflist = self.u.getAllFlieInf()
        #print(finflist[0])
        #更新显示路径
        self.e.set(finflist[1]) #设置输入框的值
        #更新文件列表
        if finflist[0]:#判断是否为空目录 空目录直接return
            for value in finflist[0]:
                clow.append([len(clow)+1,value[0],value[2],value[1]])                  
                self.tree.insert('','end',values=clow[len(clow)-1])#插入数据
            return
        else:
            print('空目录')
            return
            
    def downloadFile(self):#弹出路径选择框，选择并下载文件
        wind =Tk()
        wind.withdraw()
        if self.clickfilename[1]:
            Folderpath = filedialog.askdirectory()#弹出路径选择框 返回选择目录的路径
            #print(Folderpath)
            self.u.download(Folderpath,self.clickfilename[1])
            tkinter.messagebox.showinfo('提示','下载完成')
        else:
            print('选择文件')
        wind.quit()
        wind.destroy()
        wind.mainloop()    
    def uploadFile(self):#弹出文件选择框，选择并上传文件
        winu =Tk()
        winu.withdraw()
        #Folderpath = filedialog.askdirectory()
        Filepath = filedialog.askopenfilename()#弹出文件选择框 返回选择文件的完整路径
        self.u.upload(Filepath)
        tkinter.messagebox.showinfo('提示','上传完成')
        self.updatetree()
        winu.quit()
        winu.destroy()
        winu.mainloop()

'''
ui = pui()
ui.login()
'''