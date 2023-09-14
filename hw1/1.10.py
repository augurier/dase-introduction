def ifSequence(s):
    pre = ''
    for i in s:
        if pre == i:
            print("包含")
            return
        else:
            pre = i
    print("不包含")
    return

s = input("请输入字符串：")
ifSequence(s)
