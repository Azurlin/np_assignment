# -*- coding: utf-8 -*-
import ftplib
import re
 
class pFtpClient:
    def __init__(self,username,password): 
        server_address = '127.0.0.1'
        #创建FTP实例，并显示欢迎界面
        self.ftp = ftplib.FTP(server_address)
        print(self.ftp.getwelcome())
        #登录，输入服务器里添加过的用户名和口令
        self.ftp.login(username, password)
    #文件上传
    def upload(self,fname): # 参数fname为本地文件路径
        fd = open(fname, 'rb')
        fn = re.search(r"\w+\.\w+",fname).group()#从路径中匹配出文件名
        if self.isfile(fn):
            try:            
                #以二进制的形式上传
                self.ftp.storbinary("STOR %s" %fn, fd)
                fd.close()
                print("upload finished")
            except Exception as e:
                print('上传失败'+e)
        else:
            print('无效文件类型')
    #文件下载
    def download(self,path,fname): #path 本地路径 fname文件名
        #构建文件的存储路径
        localfile = open(path+'/'+fname, 'wb')
        try:
            #以二进制形式下载，注意第二个参数是fd.write
            self.ftp.retrbinary("RETR "+ fname, localfile.write)
            localfile.close()
            print("download finished")
        except Exception as e:
            print('下载失败'+e)
    def getAllFlieInf(self):#返回文件路径和该目录下的所有文件的名称、大小、修改日期
        fileInfList =[]       
        path = self.ftp.pwd()
        print('当前目录：'+path )
        entries = self.ftp.nlst(path) #目录下的文件      
        print(len(entries), "entries:")
        for entry in sorted(entries):
            if self.isfile(entry):
                try:
                    getinf = self.fileInf(entry) #getinf[0] 是文件修改时间 1是文件大小
                    fileInfList.append([entry,getinf[0],getinf[1]])
                except:
                    fileInfList.append(['无法识别文件','--','--'])
            else:
                fileInfList.insert(1,[entry,'--','文件夹'])
        return fileInfList,path
    def isfile(self,file):#判断是否为目录 file文件名
        ju = re.search(r"\w\.\w",file)
        if ju is None:
           print('是文件夹')
           return False
        else:
           return True
    def fileInf(self,filename):#获取文件信息  filename 文件名  
        self.ftp.voidcmd('TYPE I')        
        #文件大小
        try:
            fsize = self.ftp.size(filename)#返回文件大小的单位是B
        except:           
            print('err:获取该文件信息失败:'+filename)
            return
        filesize = '%.3f'%(fsize/1024)+'KB'#换算成KB 保留三位小数
        print('文件大小:'+filesize)              
        #获取修改时间
        L = list(self.ftp.sendcmd('MDTM '+filename)) #通过MDTM获取文件修改时间 保存到列表里方便取某一段数据
        #处理MDTM的返回值 在测试的过程中发现通过MDTM获取的时间 并非时间戳而是一种特殊的编码-->年月日没有问题 小时部分的编码没有查到是什么格式
        #但是通过对比观察几组数据可知 返回的字符串第14位和第15位的含义是小时 并且从01--24对应的是从9点--8点 通过下面的语句简单处理一下返回值并保存为一个字符串
        #021744--->10:17:44 022301--->10:23:01
        #2019/12/13
        ht = int(L[12]+L[13]) 
        if(ht < 16):
            if(ht == 16):
                hour = '00'
            else:
                hour = str(ht+8)
        else:
            hour=str(ht-16)
        modifydate = L[4]+L[5]+L[6]+L[7]+'年'+L[8]+L[9]+'月'+L[10]+L[11]+'日'+hour+':'+L[14]+L[15]+':'+L[16]+L[17]
        print('修改日期：'+modifydate)
        return modifydate,filesize



'''       
fp = pFtpClient()
fp.pwdcmd()
fp.upload()    
'''   
'''
8+n
01:   9

02:17:44
02:23:01

03    11


24 8
23 7
22 6
21 5
20 4
19 3
18 2
17 1
16 24
15 23
14 22
13 21
12 20
11 19
10 18
9  17
8  16
7  15
6  14
5  13
4  12
3  11
2  10
1  9

'''