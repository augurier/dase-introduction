import csv
from lxml import etree
import requests
import pymysql
db = pymysql.connect(host='127.0.0.1', port = 3306, user = 'root', passwd = 'lidu12345', db = 'user_db')
cursor = db.cursor()
create_tb_sql = '''create table if not exists movie(
    id int AUTO_INCREMENT PRIMARY KEY,
    name varchar(255),
    crew varchar(255),
    feature varchar(255),
    comment varchar(255)
);'''
cursor.execute(create_tb_sql)
db.commit()

with open('movie_data.csv','w',newline='',encoding = 'utf-8') as fp:
    writer = csv.writer(fp)
    writer.writerow(('name','actor','information','date','star','evaluate','introduction'))

    urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0,250,25)]
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86 64) AppleWebKit/537.36(KHTML,like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36'
    }

    #3.通过 request 请求访问网页并几获取网页内容
    for url in urls:
        html = requests.get(url,headers=headers)
        selector = etree.HTML(html.text)  #catch html text
        infos = selector.xpath("//ol[@class='grid_view']/li")
        #visit all the urls and get information
    #4.解析网页内容
        for info in infos:
            name = info.xpath(".//div[@class='item']//div[@class='info']//div[@class='hd']//a/span[1]/text()")
            crew = info.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//p[1]/text()[1]")
            feature = info.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//p[1]/text()[2]")
            comment = info.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//div[@class='star']//span[4]/text()")
            seq = " "
            movie = name + crew + feature + comment
            movies = seq.join(movie)
            writer.writerow((movies))

            name0 = seq.join(name)[:255:]
            crew0 = seq.join(crew)[:255:]
            feature0 = seq.join(feature)[:255:]
            comment0 = seq.join(comment)[:255:]
            sql = "insert into movie(name,crew,feature,comment) values('%s','%s','%s','%s');"%(name0,crew0,feature0,comment0)
            cursor.execute(sql)
            db.commit()
cursor.close()
db.close()