import pymysql
import requests
import csv
import time
from lxml import etree


db = pymysql.connect(host = 'localhost',user = 'root',password = 'root',db ="movie_url")
conn = db.cursor()
conn.execute("select url from url ")
# fetchall函数返回多条记录
number = conn.fetchall()
url = set(number)

url1 = list(url)
f = open("url.csv",'a',newline="")
try:
    write = csv.writer(f)
    for i in range(len(url1)):
        write.writerow(url1[i])
finally:
    f.close()

headers = {
'Referer':'https://movie.douban.com/subject/1786231/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400',
}
requests = requests.session()
movie = [];url2 = []
def getStr(list):
    list1=[];list2=[];list3 = []
    if len(list) != 0 :
        for i in range(len(list)):
            list1.append(list[i])
        str_list = ','.join(map(str,list1))
        list2.append(str_list)
        return list2
    else:
        return list

def NULL(str):
    s = []
    if str.strip() == '':
        return s
    else:
        return str

def getMovie_Details():
    r = open("url.csv",'r')
    for u in r:
        url2.append(u)
    print(len(url2))
    for i in range(7000,len(url2)):
        print("----------正在爬取第{}部电影----------".format(i+1))

        response = requests.get(url2[i].strip(),headers = headers)
        response.encoding = 'utf-8'
        if response.status_code == 403 or response.status_code == 404:
            break
        html = etree.HTML(response.content,etree.HTMLParser(encoding="utf-8"))
        print(html.xpath('//*[@id="content"]/h1/span[1]/text()'))
        title = next(iter(html.xpath('//*[@id="content"]/h1/span[1]/text()')),'暂无标题信息')
        director = next(iter(html.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')), '暂无导演信息')
        Screenwriter = next(iter(getStr(html.xpath('//*[@id="info"]/span[2]/span[2]/a/text()'))), "暂无编剧信息")
        performer = next(iter(getStr(html.xpath('//span[@class="actor"]/span[2]/a/text()'))), "暂无演员信息")
        Release_time = next(iter(html.xpath('//span[@property="v:initialReleaseDate"]/text()')), '暂无上映时间')
        Film_length = next(iter(html.xpath('//span[@property="v:runtime"]/text()')), '暂无电影时长')
        type = next(iter(html.xpath('//span[@property="v:genre"]/text()')), '暂无电影类型')
        score = next(iter(html.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')), '暂无电影评分')
        movie.append([title, director,Screenwriter, performer, Release_time, Film_length, type,score])
    return movie


if __name__ == "__main__":
    getMovie_Details()
    print(movie)
    f = open("movie.csv",'a',encoding='utf-8-sig',newline="")
    try:
        w = csv.writer(f)
        # w.writerow(("电影名",'导演','编剧','演员','上映时间','片长','类型','评分'))
        for i in range(len(movie)):
            w.writerow((movie[i][0],movie[i][1],movie[i][2],movie[i][3],movie[i][4],movie[i][5],movie[i][6],movie[i][7]))
    finally:
        f.close()