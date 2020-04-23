# coding:utf-8
import requests
import json
import Xicidaili_spider
import re
import pymongo
import time

headers = {
    'Host': 'www.endata.com.cn',
    'Origin': 'http://www.endata.com.cn',
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
areaIds = [
           {"id": 2, "name": "加拿大"}, {"id": 7, "name": "意大利"}, {"id": 14, "name": "西班牙"}, {"id": 42, "name": "墨西哥"},
           {"id": 11, "name": "澳大利亚"}, {"id": 43, "name": "印度"}, {"id": 2102, "name": "尼日利亚"},
           {"id": 24, "name": "丹麦"}, {"id": 20, "name": "荷兰"}, {"id": 26, "name": "瑞典"}, {"id": 32, "name": "捷克"},
           {"id": 8, "name": "巴西"}, {"id": 22, "name": "阿根廷"}, {"id": 19, "name": "比利时"}, {"id": 9, "name": "菲律宾"},
           {"id": 6, "name": "瑞士"}, {"id": 45, "name": "芬兰"}, {"id": 33, "name": "匈牙利"}, {"id": 17, "name": "奥地利"},
           {"id": 31, "name": "俄罗斯"}, {"id": 29, "name": "韩国"}, {"id": 69, "name": "爱尔兰"}, {"id": 3, "name": "波兰"},
           {"id": 44, "name": "葡萄牙"}, {"id": 13, "name": "挪威"}, {"id": 10, "name": "以色列"}, {"id": 21, "name": "希腊"},
           {"id": 74, "name": "古巴"}, {"id": 60, "name": "智利"}, {"id": 15, "name": "土耳其"}, {"id": 28, "name": "新西兰"},
           {"id": 39, "name": "立陶宛"}, {"id": 41, "name": "马耳他"}, {"id": 75, "name": "伊朗"}, {"id": 54, "name": "泰国"},
           {"id": 46, "name": "保加利亚"}, {"id": 64, "name": "克罗地亚"}, {"id": 51, "name": "印度尼西亚"},
           {"id": 23, "name": "哥伦比亚"}, {"id": 66, "name": "罗马尼亚"}, {"id": 18, "name": "南非"},
           {"id": 35, "name": "马来西亚"}, {"id": 48, "name": "塞浦路斯"}, {"id": 49, "name": "巴拿马"},
           {"id": 82, "name": "南联盟"}, {"id": 5, "name": "新加坡"}, {"id": 27, "name": "秘鲁"}, {"id": 52, "name": "黎巴嫩"},
           {"id": 53, "name": "波多黎各"}, {"id": 38, "name": "埃及"}, {"id": 47, "name": "委内瑞拉"},
           {"id": 55, "name": "牙买加"}, {"id": 36, "name": "爱沙尼亚"}, {"id": 56, "name": "特立尼达和多巴哥"},
           {"id": 65, "name": "斯洛文尼亚"}, {"id": 57, "name": "多米尼加"}, {"id": 12, "name": "冰岛"},
           {"id": 34, "name": "卢森堡"}, {"id": 58, "name": "危地马拉"}, {"id": 68, "name": "斯洛伐克"},
           {"id": 59, "name": "乌拉圭"}, {"id": 61, "name": "厄瓜多尔"}, {"id": 62, "name": "玻利维亚"},
           {"id": 63, "name": "拉脱维亚"}, {"id": 67, "name": "南斯拉夫"}, {"id": 70, "name": "肯尼亚"},
           {"id": 72, "name": "乌克兰"}, {"id": 73, "name": "摩洛哥"}, {"id": 76, "name": "坦桑尼亚"},
           {"id": 77, "name": "波黑"}, {"id": 78, "name": "越南"}, {"id": 79, "name": "津巴布韦"},
           {"id": 80, "name": "阿尔及利亚"}, {"id": 81, "name": "巴勒斯坦"}, {"id": 83, "name": "塞内加尔"},
           {"id": 84, "name": "巴基斯坦"}, {"id": 85, "name": "阿尔巴尼亚"}, {"id": 86, "name": "格鲁吉亚"},
           {"id": 87, "name": "布基纳法索"}, {"id": 88, "name": "亚美尼亚"}, {"id": 89, "name": "海地"},
           {"id": 90, "name": "吉尔吉斯坦"}, {"id": 91, "name": "尼泊尔"}, {"id": 92, "name": "哈萨克斯坦"},
           {"id": 93, "name": "突尼斯"}, {"id": 94, "name": "卢旺达"}, {"id": 95, "name": "纳米比亚"},
           {"id": 96, "name": "乌兹别克斯坦"}, {"id": 97, "name": "斯里兰卡"}, {"id": 98, "name": "喀麦隆"},
           {"id": 99, "name": "加纳"}, {"id": 100, "name": "巴哈马"}, {"id": 101, "name": "中国澳门"},
           {"id": 102, "name": "西德"}, {"id": 103, "name": "前苏联"}, {"id": 104, "name": "捷克斯洛伐克"},
           {"id": 105, "name": "东德"}, {"id": 106, "name": "摩纳哥"}, {"id": 107, "name": "列支敦士登"},
           {"id": 108, "name": "利比亚"}, {"id": 109, "name": "象牙海岸"}, {"id": 110, "name": "乍得"},
           {"id": 111, "name": "博茨瓦纳"}, {"id": 112, "name": "阿富汗"}, {"id": 113, "name": "格陵兰岛"},
           {"id": 114, "name": "蒙古"}, {"id": 118, "name": "科威特"}, {"id": 128, "name": "巴林"},
           {"id": 137, "name": "白俄罗斯"}, {"id": 148, "name": "哥斯达黎加"}, {"id": 151, "name": "萨尔瓦多"},
           {"id": 152, "name": "洪都拉斯"}, {"id": 156, "name": "阿拉伯"}, {"id": 158, "name": "马其顿"},
           {"id": 2087, "name": "百慕大群岛"}, {"id": 2088, "name": "苏里南河(荷兰)"}, {"id": 2089, "name": "巴巴多斯岛"},
           {"id": 2090, "name": "叙利亚"}, {"id": 2091, "name": "塞尔维亚"}, {"id": 2092, "name": "全世界"},
           {"id": 2093, "name": "巴拉圭"}, {"id": 2094, "name": "孟加拉国"}, {"id": 2095, "name": "约旦"},
           {"id": 2096, "name": "阿曼"}, {"id": 2097, "name": "新喀里多尼亚"}, {"id": 2099, "name": "卡塔尔"},
           {"id": 2103, "name": "法罗群岛"}, {"id": 2104, "name": "阿鲁巴岛"}, {"id": 2106, "name": "伯利兹城"},
           {"id": 2107, "name": "尼加拉瓜"}, {"id": 2119, "name": "佛得角"}, {"id": 2120, "name": "圭亚那"},
           {"id": 2121, "name": "塞舌尔"}, {"id": 2123, "name": "安哥拉"}, {"id": 2125, "name": "毛里求斯"},
           {"id": 2127, "name": "斐济"}, {"id": 2128, "name": "波斯尼亚"}, {"id": 2131, "name": "莫桑比克"},
           {"id": 2132, "name": "苏丹"}, {"id": 2141, "name": "伊拉克"}, {"id": 2142, "name": "北朝鲜"},
           {"id": 2143, "name": "塞尔维亚和黑山"}, {"id": 2144, "name": "缅甸"}, {"id": 2145, "name": "马达加斯加岛"},
           {"id": 2146, "name": "阿塞拜疆"}, {"id": 2147, "name": "安道尔"}, {"id": 2148, "name": "瓜德罗普岛"},
           {"id": 2149, "name": "马提尼克岛"}, {"id": 2150, "name": "汤加"}, {"id": 2151, "name": "尼日尔"},
           {"id": 2152, "name": "厄立特里亚"}, {"id": 2153, "name": "不丹"}, {"id": 2154, "name": "老挝国"},
           {"id": 2155, "name": "加蓬"}, {"id": 2156, "name": "贝宁湾"}, {"id": 2157, "name": "柬埔寨"},
           {"id": 2158, "name": "多哥"}, {"id": 2159, "name": "中非共和国"}, {"id": 2160, "name": "几内亚"},
           {"id": 2161, "name": "马里"}, {"id": 2162, "name": "塔吉克斯坦"}, {"id": 2163, "name": "巴布亚新几内亚"},
           {"id": 2164, "name": "赞比亚"}, {"id": 2165, "name": "沙特阿拉伯"}, {"id": 2166, "name": "刚果"},
           {"id": 2167, "name": "土库曼斯坦"}, {"id": 2168, "name": "乌干达"}, {"id": 2169, "name": "毛利塔尼亚"},
           {"id": 2170, "name": "摩尔多瓦"}, {"id": 2171, "name": "科索沃"}, {"id": 2172, "name": "埃塞俄比亚"},
           {"id": 2174, "name": "特克斯科斯群岛"}, {"id": 2175, "name": "特克斯和凯科斯群岛"}, {"id": 2176, "name": "利比里"},
           {"id": 2177, "name": "索马里"}, {"id": 2178, "name": "荷属安的列斯群岛"}, {"id": 2179, "name": "刚果民主共和国"},
           {"id": 2180, "name": "也门共和国大使馆"}, {"id": 2181, "name": "莱索托王国大使馆"}, {"id": 2182, "name": "被占领巴勒斯坦领土"},
           {"id": 2183, "name": "安提瓜和巴布达"}, {"id": 2184, "name": "纽埃"}, {"id": 2185, "name": "法属玻利尼西亚"},
           {"id": 2186, "name": "刚果民主共和国"}, {"id": 2187, "name": "几内亚比绍"}, {"id": 2188, "name": "西撒哈拉"},
           {"id": 2189, "name": "布隆迪共和国大使馆"}, {"id": 2190, "name": "圣马力诺"}, {"id": 2194, "name": "中国澳门"},
           {"id": 2202, "name": "几内亚比绍"}]

def getHtmlData(url):
    movies = []
    dailiIP = Xicidaili_spider.getProxies()
    data = {
        'areaId': '1',
        'typeId': '0',
        'year': '0',
        'initial': '',
        'pageIndex': '1',
        'pageSize': '10',
        'MethodName': 'BoxOffice_GetMovieData_List',
    }
    dataCollection = creatDatabaseCollection()
    for areaId in areaIds:
        data['areaId'] = areaId.get('id')
        response = requests.get(url=url,
                                data=data,
                                # proxies=dailiIP,
                                timeout=20, )
        response.encoding = response.apparent_encoding
        response = json.loads(response.text)
        if response.get('Data').get('Table1')[0].get('TotalCounts') == 0:
            continue
        else:
            # print(areaId.get('id'))
            # print(int(response.get('Data').get('Table1')[0].get('TotalPage')))
            for TotalPage in range(int(response.get('Data').get('Table1')[0].get('TotalPage'))):
                data['pageIndex'] = '{}'.format(TotalPage + 1)
                print('正在获取（{}）地区第{}页数据'.format(areaId.get('name'),(TotalPage + 1)))
                # print(data)
                response = requests.get(url=url,
                                        data=data,
                                        # proxies=dailiIP,
                                        timeout=20, )
                response.encoding = response.apparent_encoding
                response = json.loads(response.text)
                # print(response)
                movies = movies + getMoviesIDList(response)
                dataToMongdb(getMoviesIDList(response),dataCollection)
    # print(movies)
    # 存储
    # dataToMongdb(movies, creatDatabaseCollection())
    print(movies)
    return None
def getMoviesIDList(response):
    moviesIdList = []
    for m_id in response.get('Data').get('Table'):
        # moviesUrls.append('http://www.endata.com.cn/BoxOffice/MovieStock/movieShow.html?id={}}'.format(m_id.get('ID')))
        moviesIdList.append(m_id.get('ID'))
    # print(moviesUrls)
    return getMovieInfo(moviesIdList)

def getMovieInfo(moviesIdList):
    movieInfo = []
    pattern = re.compile(r'\|\d+')
    for movieID in moviesIdList:
        data = {
            'movieId': '{}'.format(movieID),
            'MethodName': 'BoxOffice_GetMovieData_Details',
        }
        res = requests.post(url='http://www.endata.com.cn/API/GetData.ashx', data=data, headers=headers, timeout=20)
        res.encoding = res.apparent_encoding
        res = json.loads(res.text)
        res = res.get('Data').get('Table')[0]
        MovieId = res.get('MovieId')
        MovieName = res.get('MovieName')
        RealTimeBox = res.get('RealTimeBox')  # 实时票房
        SumBoxOffice = res.get('SumBoxOffice')  # 累计票房
        MovieFxAll = res.get('MovieFxAll')  # 发行公司
        MovieZz = res.get('MovieZz')  # 制片公司
        if MovieFxAll != None:
            MovieFxAll = re.sub(pattern, '', MovieFxAll)
            if MovieFxAll[-1] == '/':
                MovieFxAll = MovieFxAll[:-1]
        if MovieZz != None:
            MovieZz = re.sub(pattern, '', MovieZz)
            if MovieZz[-1] == '/':
                MovieZz = MovieZz[:-1]
        # print(MovieId)
        movieInfo.append({
            'MovieName': MovieName,
            'MovieId': MovieId,
            'RealTimeBox': RealTimeBox,
            'SumBoxOffice': SumBoxOffice,
            'MovieFxAll': MovieFxAll,
            'MovieZz': MovieZz,
        })
        print('正在爬取《{}》'.format(MovieName))
        time.sleep(1)
    # print(movieInfo)
    # break
    return movieInfo

def dataToMongdb(movieInfo, mycol):
    for m_info in movieInfo:
        print('正在存储《{}》的信息'.format(m_info.get('MovieName')))
        mycol.insert_one(m_info)


def creatDatabaseCollection():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["SecondClass"]
    dblist = myclient.list_database_names()
    # dblist = myclient.database_names()
    if "SecondClass" in dblist:
        print("数据库已存在！")
    # mycol = mydb["movie_append"]
    mycol = mydb["movie_collection"]
    collist = mydb.list_collection_names()
    # collist = mydb.collection_names()
    if "movie_collection" in collist:  # 判断 sites 集合是否存在
        print("集合已存在！")
    return mycol
def readDataForMongodb(mycol):
    mycol = mycol.find_one({"MovieId":641515})
    print(mycol)

if __name__ == '__main__':
    getHtmlData('http://www.endata.com.cn/API/GetData.ashx')
    # getMoviesIDList({'Status': 1, 'Msg': '', 'Data': {'Table': [{'rowNum': 1, 'ID': 641515, 'MovieName': '战狼2', 'MovieEnName': 'Wolf Warriors 2', 'releaseYear': 2017, 'defaultImage': 'http://images.entgroup.cn/group1/M00/00/C2/wKgASVznzXuAZSQEAAB9n21g2SM514.jpg', 'amount': 5679285847.0, 'BoxOffice': 567929}, {'rowNum': 2, 'ID': 662685, 'MovieName': '哪吒之魔童降世', 'MovieEnName': 'Ne Zha', 'releaseYear': 2019, 'defaultImage': 'http://images.entgroup.cn/group2/M00/02/8A/wKgAS10-kBmAKrbcAABr892L23I638.jpg', 'amount': 5013345127.0, 'BoxOffice': 501335}, {'rowNum': 3, 'ID': 642412, 'MovieName': '流浪地球', 'MovieEnName': 'The Wandering Earth', 'releaseYear': 2019, 'defaultImage': 'http://images.entgroup.cn/group1/M00/00/AB/wKgASVzny4uAEWvcAABfH3c7ZxA728.jpg', 'amount': 4684410830.0, 'BoxOffice': 468441}, {'rowNum': 4, 'ID': 655823, 'MovieName': '红海行动', 'MovieEnName': 'Operation Red Sea', 'releaseYear': 2018, 'defaultImage': 'http://images.entgroup.cn/group2/M00/00/55/wKgAS1zny8GAcqTMAAB5ad6sOkg158.jpg', 'amount': 3650787000.0, 'BoxOffice': 365079}, {'rowNum': 5, 'ID': 663419, 'MovieName': '唐人街探案2', 'MovieEnName': 'Detective Chinatown Vol 2', 'releaseYear': 2018, 'defaultImage': 'http://images.entgroup.cn/group2/M00/00/50/wKgAS1znyuSAWjHMAACH710vKVc225.jpg', 'amount': 3397687917.0, 'BoxOffice': 339769}, {'rowNum': 6, 'ID': 626153, 'MovieName': '美人鱼', 'MovieEnName': 'The Mermaid', 'releaseYear': 2016, 'defaultImage': 'http://images.entgroup.cn/group2/M00/00/5E/wKgASlznzS2AcWCeAABwl8jFKb8737.jpg', 'amount': 3392109138.0, 'BoxOffice': 339211}, {'rowNum': 7, 'ID': 691481, 'MovieName': '我和我的祖国', 'MovieEnName': 'My People, My Country', 'releaseYear': 2019, 'defaultImage': 'http://images.entgroup.cn/group1/M00/05/1F/wKgASV1-9TiAGhZmAACCZzeu0MY565.jpg', 'amount': 3171189437.0, 'BoxOffice': 317119}, {'rowNum': 8, 'ID': 676313, 'MovieName': '我不是药神', 'MovieEnName': 'Dying to Survive', 'releaseYear': 2018, 'defaultImage': 'http://images.entgroup.cn/group1/M00/00/A8/wKgASVzny1SAAagSAACIKvFmOFA557.jpg', 'amount': 3099961018.0, 'BoxOffice': 309996}, {'rowNum': 9, 'ID': 681319, 'MovieName': '中国机长', 'MovieEnName': 'The Captain', 'releaseYear': 2019, 'defaultImage': 'http://images.entgroup.cn/group1/M00/05/1F/wKgASV2AgMGAB6kZAAB8yi1T_ZQ512.jpg', 'amount': 2912412039.0, 'BoxOffice': 291241}, {'rowNum': 10, 'ID': 671983, 'MovieName': '西虹市首富', 'MovieEnName': 'Hello Mr. Billionaire', 'releaseYear': 2018, 'defaultImage': 'http://images.entgroup.cn/group2/M00/00/42/wKgASlznyK6AY_1SAABzXedgJUU849.jpg', 'amount': 2547571698.0, 'BoxOffice': 254757}], 'Table1': [{'TotalCounts': 11484, 'TotalPage': 1149.0}]}})
    # readDataForMongodb(creatDatabaseCollection())
