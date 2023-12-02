import lxml.etree
import requests
import csv
import pymysql


fp = './spider_allstar23.csv'
with open(fp, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'player_name', 'appearances_time', 'field_goal_percentage', 'shots_made', 'shots_try', 'three_pointer_percentage',
                      'three_shots_made', 'three_shots_try', 'free_throws_percentage', 'free_throw_made', 'free_throws_try', 'rebounds', 
                    'assists', 'steals', 'blocks', 'turnovers', 'fouls', 'scores']) # write header

urls = ['https://nba.hupu.com/stats/players/pts']
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36'}
for url in urls:
    html = requests.get(url, headers=headers)
    selector = lxml.etree.HTML(html.text)
    infos = selector.xpath('//*[@id="data_js"]/div[4]/div/table/tbody')
    
    for info in infos:
        for n in range(2, 52):
            try:
                id = info.xpath('tr[{}]/td[1]/text()'.format(n))[0]

                player_html = info.xpath('tr[{}]/td[2]/a/@href'.format(n))[0]
                detail_html = requests.get(player_html, headers=headers)
                selector2 = lxml.etree.HTML(detail_html.text)
                #球员页面

                player_name = selector2.xpath('/html/body/div[3]/p/b/text()')[0]
                info2 = selector2.xpath('/html/body/div[3]/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/table[1]/tbody')[0]
                rebounds = info2.xpath('tr[3]/td[9]/text()')[0]
                assists = info2.xpath('tr[3]/td[10]/text()')[0]
                steals = info2.xpath('tr[3]/td[11]/text()')[0]
                blocks = info2.xpath('tr[3]/td[12]/text()')[0]
                turnovers = info2.xpath('tr[3]/td[13]/text()')[0]
                fouls = info2.xpath('tr[3]/td[14]/text()')[0]
                #主页

                scores = info.xpath('tr[{}]/td[4]/text()'.format(n))[0]
                
                shots = info.xpath('tr[{}]/td[5]/text()'.format(n))[0]
                shots_made = shots.split('-')[0]
                shots_try = shots.split('-')[1]
                field_goal_percentage = info.xpath('tr[{}]/td[6]/text()'.format(n))[0]

                three_shots = info.xpath('tr[{}]/td[7]/text()'.format(n))[0]
                three_shots_made = three_shots.split('-')[0]
                three_shots_try = three_shots.split('-')[1]
                three_pointer_percentage = info.xpath('tr[{}]/td[8]/text()'.format(n))[0]

                free_throw = info.xpath('tr[{}]/td[9]/text()'.format(n))[0]
                free_throw_made = free_throw.split('-')[0]
                free_throws_try = free_throw.split('-')[1]
                free_throws_percentage = info.xpath('tr[{}]/td[10]/text()'.format(n))[0]

                appearances_time = info.xpath('tr[{}]/td[12]/text()'.format(n))[0]

                #write
                with open(fp, 'a', newline='') as file:
                    writer = csv.writer(file)                    
                    writer.writerow([id, player_name, appearances_time, field_goal_percentage, shots_made, shots_try, three_pointer_percentage,
                    three_shots_made, three_shots_try, free_throws_percentage, free_throw_made, free_throws_try, rebounds, 
                     assists, steals, blocks, turnovers, fouls, scores])
               
            except:
                continue
                

print("spider success!")