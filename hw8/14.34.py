from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

vectorizer = TfidfVectorizer() 
train=fetch_20newsgroups(subset='train')
test=fetch_20newsgroups(subset='test')
train_v=vectorizer.fit_transform(train.data)
test_v=vectorizer.transform(test.data)
print(train_v)
print(test_v)


model = eval('MultinomialNB()')

model.fit(train_v,train.target)
print("训练准确率为:",model.score(train_v,train.target))
print("测试准确率为:",model.score(test_v,test.target))

