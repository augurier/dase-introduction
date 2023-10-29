from sklearn.datasets import load_iris  
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from sklearn.linear_model import LogisticRegression  
from sklearn.model_selection import train_test_split  
from sklearn import metrics  

def countDis(i, iris_all, length):
    m1x = np.mean(iris_all[iris_all["target"]==i]["petal length (cm)"])
    m1y = np.mean(iris_all[iris_all["target"]==i]["petal width (cm)"])
    v1 = np.array([m1x,m1y])
    print("label{}中心点: ".format(i), m1x, ",", m1y)

    for j in range(i * length, (i+1) * length):
        v2 = np.array([iris_all[iris_all["target"]==i]["petal length (cm)"][j],iris_all[iris_all["target"]==i]["petal width (cm)"][j]])
        print(np.linalg.norm(v1-v2), end=" ")
    print('\n')



#11.6
iris = load_iris() 
df = pd.DataFrame(data=iris.data, columns=iris.feature_names) 

iris_target = iris.target
iris_all = df.copy() 
iris_all['target'] = iris_target
length = len(iris_all[iris_all["target"]==0]["petal length (cm)"])

train_x,test_x,train_y,test_y = train_test_split(df,iris_target,test_size=0.3,random_state=180)

#11.7
model = LogisticRegression()
model.fit(train_x, train_y)
prediction = model.predict(test_x)
accuracy = metrics.accuracy_score(prediction, test_y)
print('The accuracy of the Logistic Regression is:', accuracy)
print('\n')

#11.8
countDis(0,iris_all,length)
countDis(1,iris_all,length)
countDis(2,iris_all,length)

#11.9
X = iris.data  # 我们只取特征空间用于K-means聚类

# K-means聚类
kmeans = KMeans(n_clusters=3)  # 选择3作为聚类数量，因为我们知道有三类鸢尾花
kmeans.fit(X)

# 获取聚类标签和中心点
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_

# 可视化聚类结果
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis')  # 根据K-means聚类的标签给每个点上色

# 画出聚类的中心点
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, alpha=0.75)

plt.title("K-means Clustering on Iris Dataset")
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

plt.show()