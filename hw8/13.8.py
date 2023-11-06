from sklearn.datasets import  fetch_20newsgroups
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report


# 1 下载新闻数据
fetch_20newsgroups(data_home="www.cs.cmu.edu/afs/cs/project/theo-11/www/naive-bayes.html", # 文件下载的路径
                   subset='train', # 加载那一部分数据集 train/test
                   categories=None, # 选取哪一类数据集[类别列表]，默认20类
                   shuffle=True,  # 将数据集随机排序
                   random_state=42, # 随机数生成器
                   remove=(), # ('headers','footers','quotes') 去除部分文本
                   download_if_missing=True # 如果没有下载过，重新下载
                   )
news = fetch_20newsgroups(subset="all")


# 2 分割训练数据和测试数据
x_train, x_test, y_train, y_test = train_test_split(news.data,
                                                    news.target,
                                                    test_size=0.25,
                                                    random_state=33)


# 3.1 采用普通统计CountVectorizer提取特征向量
# 默认配置不去除停用词
count_vec = CountVectorizer()
x_count_train = count_vec.fit_transform(x_train)
x_count_test = count_vec.transform(x_test)
# 去除停用词
count_stop_vec = CountVectorizer(analyzer='word', stop_words='english')
x_count_stop_train = count_stop_vec.fit_transform(x_train)
x_count_stop_test = count_stop_vec.transform(x_test)

# 3.2 采用TfidfVectorizer提取文本特征向量
# 默认配置不去除停用词
tfid_vec = TfidfVectorizer()
x_tfid_train = tfid_vec.fit_transform(x_train)
x_tfid_test = tfid_vec.transform(x_test)
# 去除停用词
tfid_stop_vec = TfidfVectorizer(analyzer='word', stop_words='english')
x_tfid_stop_train = tfid_stop_vec.fit_transform(x_train)
x_tfid_stop_test = tfid_stop_vec.transform(x_test)


# 4 使用朴素贝叶斯分类器  分别对两种提取出来的特征值进行学习和预测
# 对普通通统计CountVectorizer提取特征向量 学习和预测
mnb_count = MultinomialNB()
mnb_count.fit(x_count_train, y_train)   # 学习
mnb_count_y_predict = mnb_count.predict(x_count_test)   # 预测
# 去除停用词
mnb_count_stop = MultinomialNB()
mnb_count_stop.fit(x_count_stop_train, y_train)   # 学习
mnb_count_stop_y_predict = mnb_count_stop.predict(x_count_stop_test)    # 预测

# 对TfidfVectorizer提取文本特征向量 学习和预测
mnb_tfid = MultinomialNB()
mnb_tfid.fit(x_tfid_train, y_train)
mnb_tfid_y_predict = mnb_tfid.predict(x_tfid_test)
# 去除停用词
mnb_tfid_stop = MultinomialNB()
mnb_tfid_stop.fit(x_tfid_stop_train, y_train)   # 学习
mnb_tfid_stop_y_predict = mnb_tfid_stop.predict(x_tfid_stop_test)    # 预测

# 5 模型评估
# 对普通统计CountVectorizer提取的特征学习模型进行评估
print("未去除停用词的CountVectorizer提取的特征学习模型准确率：", mnb_count.score(x_count_test, y_test))
print("更加详细的评估指标:\n", classification_report(mnb_count_y_predict, y_test))
print("去除停用词的CountVectorizer提取的特征学习模型准确率：", mnb_count_stop.score(x_count_stop_test, y_test))
print("更加详细的评估指标:\n", classification_report(mnb_count_stop_y_predict, y_test))

# 对TfidVectorizer提取的特征学习模型进行评估
print("TfidVectorizer提取的特征学习模型准确率：", mnb_tfid.score(x_tfid_test, y_test))
print("更加详细的评估指标:\n", classification_report(mnb_tfid_y_predict, y_test))
print("去除停用词的TfidVectorizer提取的特征学习模型准确率：", mnb_tfid_stop.score(x_tfid_stop_test, y_test))
print("更加详细的评估指标:\n", classification_report(mnb_tfid_stop_y_predict, y_test))


