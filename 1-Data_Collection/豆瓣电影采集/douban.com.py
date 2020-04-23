import requests
import json
from selenium import webdriver
import time
from lxml import etree
import pymysql
requests = requests.session()
url1 = []; url = set()
url2 = []; url3 = []
headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'utf-8',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400',
}

db = pymysql.connect(host = 'localhost',user = 'root',password = 'root',db = 'Movie_Url',charset = "utf8")
cursor1 = db.cursor()
# cursor1.execute("drop database if exists Movie_Url")
# print("数据库创建中...")
# cursor1.execute("create database Movie_Url character set utf8")
# cursor1.execute("use Movie_Url")
# cursor1.execute("drop database if exists Movie_Url")
# 建表
# sql = "create table Url(id int  primary key NOT NULL AUTO_INCREMENT,url varchar(100) not null)character set utf8"
# cursor1.execute(sql)

def Login(url):
    params = {
        'name' : '13272731335',
        'password' : 'cx5201314hyp'
    }
    response = requests.post(url,params = params,headers=headers)

def getUrl_200():
    for x in range(0,200,20):
        print(x)
        response = requests.get('https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start='+str(x)+'&genres=情色',headers=headers)
        response.encoding = "utf-8"
        [url1.append(i["url"]) for i in response.json()['data']]
        print(url1)
def getUrl200_400():
    for x in range(200,400,20):
        print(x)
        response = requests.get('https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start='+str(x)+'&genres=情色',headers=headers)
        response.encoding = "utf-8"
        [ url2.append(i["url"]) for i in response.json()['data']]
        print(url2)
def getUrl400_500():
    for x in range(400,500,20):
        response = requests.get('https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start='+str(x)+'&genres=情色',headers=headers)
        response.encoding = "utf-8"
        [ url3.append(i["url"]) for i in response.json()['data']]
        print(url3)

if __name__ =="__main__":
    # url ="https://accounts.douban.com/j/mobile/login/basic"
    # Login(url)

    # getUrl_200()
    # sql = ("insert into Url(url)" " values (%s)")
    # for j in range(len(url1)):
    #     print("已写入{}条记录".format(j))
    #     cursor1.execute(sql, (url1[j]))
    # cursor1.connection.commit()
    #
    # time.sleep(60)
    #
    # getUrl200_400()
    # print(url2)
    # sql = ("insert into Url(url)" " values (%s)")
    # for j in range(len(url2)):
    #     print("已写入{}条记录".format(j))
    #     cursor1.execute(sql, (url2[j]))
    # cursor1.connection.commit()
    #
    # time.sleep(60)

    getUrl400_500()
    # sql = ("insert into Url(url)" " values (%s)")
    # for j in range(len(url3)):
    #     print("已写入{}条记录".format(j))
    #     cursor1.execute(sql, (url3[j]))
    # cursor1.connection.commit()
