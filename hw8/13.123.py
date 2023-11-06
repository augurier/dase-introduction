from sklearn.datasets import load_iris  
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split  
from sklearn import metrics  
from collections import Counter, defaultdict
import matplotlib



iris = load_iris() 
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_target = iris.target
iris_all = df.copy() 
iris_all['target'] = iris_target
length = len(iris_all[iris_all["target"]==0]["petal length (cm)"])

#13.1
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
style_list = ['o', '^', 's']
data = iris.data
labels = iris.target_names
cc = defaultdict(list)
for i, d in enumerate(data):
    cc[labels[int(i/50)]].append(d)
p_list = []
c_list = []
for each in [0, 2]:
    for i, (c, ds) in enumerate(cc.items()):
        draw_data = np.array(ds)
        p = plt.plot(draw_data[:, each], draw_data[:, each+1], style_list[i])
        p_list.append(p)
        c_list.append(c)
plt.legend(map(lambda x: x[0], p_list), c_list)
plt.title('鸢尾花花瓣的长度和宽度') if each else plt.title('鸢尾花花萼的长度和宽度')
plt.xlabel('花瓣的长度(cm)') if each else plt.xlabel('花萼的长度(cm)')
plt.ylabel('花瓣的宽度(cm)') if each else plt.ylabel('花萼的宽度(cm)')
plt.subplots_adjust(wspace=1)
plt.show()


#13.2
train_x,test_x,train_y,test_y = train_test_split(df,iris_target,test_size=0.2,random_state=180)

#13.3
knn=KNeighborsClassifier()
knn.fit(train_x,train_y)
print("训练集精确率",knn.score(train_x,train_y))
print("测试集精确率",knn.score(test_x,test_y))

