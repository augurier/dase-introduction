import lxml.etree
import requests
import csv


fp = './history24.csv'
with open(fp, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'player_name', 'appearances_time', 'field_goal_percentage', 'shots_made', 'shots_try', 'three_pointer_percentage',
                      'three_shots_made', 'three_shots_try', 'free_throws_percentage', 'free_throw_made', 'free_throws_try', 'rebounds', 
                    'assists', 'steals', 'blocks', 'turnovers', 'fouls', 'scores']) # write header

urls = ['https://www.basketball-reference.com/leagues/NBA_2024_per_game.html']
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36'}
for url in urls:
    html = requests.get(url, headers=headers)
    selector = lxml.etree.HTML(html.text)
    infos = selector.xpath('//*[@id="per_game_stats"]/tbody')
    pre_name = ''
    for info in infos:
        for n in range(1, 1000):
            try:
                id = n
                scores = info.xpath('tr[{}]/td[29]/text()'.format(n))[0]                
                player_name = info.xpath('tr[{}]/td[1]/a/text()'.format(n))[0]
                if(player_name == pre_name):
                    continue
                else:
                    pre_name = player_name  


                
                shots_made = info.xpath('tr[{}]/td[8]/text()'.format(n))[0]
                shots_try = info.xpath('tr[{}]/td[9]/text()'.format(n))[0]
                field_goal_percentage = info.xpath('tr[{}]/td[10]/text()'.format(n))[0]

                three_shots_made = info.xpath('tr[{}]/td[11]/text()'.format(n))[0]
                three_shots_try = info.xpath('tr[{}]/td[12]/text()'.format(n))[0]
                three_pointer_percentage = info.xpath('tr[{}]/td[13]/text()'.format(n))[0]

                free_throw_made = info.xpath('tr[{}]/td[18]/text()'.format(n))[0]
                free_throws_try = info.xpath('tr[{}]/td[19]/text()'.format(n))[0]
                free_throws_percentage = info.xpath('tr[{}]/td[20]/text()'.format(n))[0]

                rebounds = info.xpath('tr[{}]/td[23]/text()'.format(n))[0]
                assists = info.xpath('tr[{}]/td[24]/text()'.format(n))[0]
                steals = info.xpath('tr[{}]/td[25]/text()'.format(n))[0]
                blocks = info.xpath('tr[{}]/td[26]/text()'.format(n))[0]
                turnovers = info.xpath('tr[{}]/td[27]/text()'.format(n))[0]
                fouls = info.xpath('tr[{}]/td[28]/text()'.format(n))[0]

                appearances_time = info.xpath('tr[{}]/td[7]/text()'.format(n))[0]

                #write
                with open(fp, 'a', newline='') as file:
                    writer = csv.writer(file)
                    try:                    
                        writer.writerow([id, player_name, appearances_time, field_goal_percentage, shots_made, shots_try, three_pointer_percentage,
                    three_shots_made, three_shots_try, free_throws_percentage, free_throw_made, free_throws_try, rebounds, 
                     assists, steals, blocks, turnovers, fouls, scores])
                    except:
                        if(float(scores) > 18):
                            player_name = 'foreign_star'
                        else:
                            player_name = 'foreign_player'
                        writer.writerow([id, player_name, appearances_time, field_goal_percentage, shots_made, shots_try, three_pointer_percentage,
                    three_shots_made, three_shots_try, free_throws_percentage, free_throw_made, free_throws_try, rebounds, 
                     assists, steals, blocks, turnovers, fouls, scores])
               
            except:
                continue
                

print("spider success!")