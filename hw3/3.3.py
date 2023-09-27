import re
def if_id(id):
    ans = re.match('(^\d{15}$)|(^\d{17}([0-9]|X)$)',id)
    if(ans == None):
        print("不是")
    else:
        print("可能是")
        
id = input("请输入字符串：")
if_id(id)