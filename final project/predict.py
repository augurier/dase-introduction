import pandas as pd
 
# 加载数据
df0 = pd.read_csv('all.csv',encoding='gb18030')
df = df0.dropna(axis=0, inplace=False)
x = df[df.columns.difference(['id', 'player_name', 'is_allstar'])].values
y = df['is_allstar'].values 
 
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=9)

 
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=100000)
model.fit(X_train,y_train)
 
# 预测分类结果
y_pred = model.predict(X_test)
 
# 预测概率
y_pred_proba = model.predict_proba(X_test)
#print(y_pred_proba[:5])
 
# 模型准确率
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_pred,y_test)
print(accuracy)


df3 = pd.read_csv('history24.csv',encoding='gb18030')
df2 = df3.dropna(axis=0, inplace=False)
x_23 = df2[df2.columns.difference(['id', 'player_name'])].values
y_23 = model.predict_proba(x_23)#预测概率
z_23 = model.predict(x_23)#01分类

cnt = 0
result = []
for i in range(0,len(y_23)):
    if(y_23[i][1] >= 0.3):
        result.append([df2['player_name'][i], y_23[i][1]])
        #print(df2['player_name'][i], y_23[i][1])
        cnt += 1

result.sort(key=lambda x:x[1],reverse=True)
for i in result:
    print(i)
print("total: ",cnt)