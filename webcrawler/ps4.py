# -*- coding: utf-8 -*-
from tkinter import *
import requests, random
import json, csv, os, time
import pandas as pd
import re , time
from threading import Thread
headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }
def spyder(num):
    for i in range(6,num+6):
        url ="https://store.playstation.com/zh-hant-hk/grid/STORE-MSF86012-GAMESALL/"+str(i)+"?platform=ps4&smcid=pdc%3Azh-hant-hk%3Acht-hk%3Aprimary%2520nav%3Amsg-shop%3Aps4"
        try:
                r = requests.get(url,headers=headers)
                r.status_code
                r.encoding = r.apparent_encoding
        except:
            print( "产生异常",r.status_code)
        match(r.text)
        #time.sleep(3)
        
def match(text):
    matchObj = re.findall( '<script type="application/ld\+json".*\n</script>', text)
    b = re.findall( '"name":".*?,', matchObj[0])
    e = re.findall('"price":.*?}',matchObj[0])
    w = []
    for i in range(len(b)):
        j = b[i][len('"name":"'):-2]
        k = e[i][len('"name":"'):-1]
        x = [j,k]
        w.append(x)
    file_do(w)
    
def file_do(list_info):
    file_state = os.path.exists('rt.csv')
    if ( file_state == False):
        name = ['名称','价格'] # 表头
        file_HT = pd.DataFrame(columns=name, data=list_info)
        # 数据写入
        f = open(r'rt.csv','w', encoding='utf-8-sig')
        
        file_HT.to_csv(r'rt.csv', encoding='utf-8-sig', index=False)
        f.close()
    else:
        with open(r'rt.csv', 'a+',encoding='utf-8-sig', newline='') as file_test:
    				# 追加到文件后面
            writer = csv.writer(file_test)
    				# 写入文件
            writer.writerows(list_info)
def download_picture(text,lst):#下载图片
    matchObj = re.findall( 'https://store.playstation.com/.*?4x', text)
    plst = []
    for i in range(len(matchObj)):
        plst.append(matchObj[i].split(',')[3])
        url = matchObj[i].split(',')[3]
        r = requests.get(url,headers=headers)
        #if(lst[i][0]+'.jpg' =='（預購）Mega Man Zero/ZX Legacy Collection.jpg'):
            #continue
        with open(lst[i][0]+'.jpg','wb') as f:
            f.write(r.content)
def ui():
    root = Tk()
    root.geometry("400x200+200+50")
    root.title('获取psn商品信息')
    root.resizable(0,0) #禁止更改窗口大小
    
    
    labelx1 = Label(root,text = '获取PSN商品信息',font=("宋体",15))
    labelx1.pack()
    
    labelx=Label(root)
    #显示lab标签 网格布局 sticky=W #左对齐 E为右对齐 默认为中间对齐
    labelx.pack() 
    
    buttonx1=Button(labelx,text="获取信息",command =run ,font=("宋体",15))
    buttonx1.grid(row=1,column=0) #设置按钮在子容器的位置
    buttonx3=Button(labelx,text="下载图片",font=("宋体",15))
    buttonx3.grid(row=1,column=2) #设置按钮在子容器的位置
    
    root.mainloop()

def run():
    spyder(2) #页数
            
if __name__ == '__main__':
    ui()



