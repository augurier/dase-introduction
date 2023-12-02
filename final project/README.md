# 数据科学导论结课大项目
## 文件信息
all.csv保存了16-23赛季所有球员数据，以及全明星标签。格式无法保存的球员名字用foreign_star 和 foreign_player代替。 

nba_playerdata12-17.xlsx是网上找到的12-17赛季开源数据集。 

history24.csv是当今赛季目前的数据(已更新至12.2日，与展示数据略有出入，因此模型结果略有不同)

allstar_spider(from hupu).py 爬取了虎扑上的数据，但项目中最终没有用到。  

history_spider(from reference).py 爬取了 www.basketball-reference.com/leagues上的数据，修改html网址可以得到历史数据。  

predict.py 用来训练模型与预测，使用了逻辑回归算法  

current_result.txt是根据11.29日数据预测的结果名单
