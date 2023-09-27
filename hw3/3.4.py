class node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class listnode:
    def __init__(self):
        self.head = None
    
    def create(self, datalist):
        self.head = node(datalist[0])
        curr = self.head
        for i in range(1,len(datalist)):
            newnode = node(datalist[i])
            curr.next = newnode
            curr = curr.next

    def insert(self, num):
        newnode = node(num, self.head)
        self.head = newnode

    def delete(self, num):
        curr = self.head
        if(curr.val == num):
            self.head = curr.next
            return
        while(curr.next != None):
            if(curr.next.val == num):
                delnode = curr.next
                curr.next = delnode.next
                return
            else:
                curr = curr.next

    def search(self, num):
        curr = self.head
        while(curr != None):
            if(curr.val == num):
                print("存在")
                return
            else:
                curr = curr.next
        print("不存在")

    def recover(self, num, newnum):
        curr = self.head
        while(curr != None):
            if(curr.val == num):
                curr.val = newnum
                return
            else:
                curr = curr.next

    def printnode(self):
        curr = self.head
        while(curr != None):
            print(curr.val,end=" ")
            curr = curr.next

datalist = [int(x) for x in input("请输入一串数，用逗号分隔：").split(',')]
nodelist = listnode()
nodelist.create(datalist)
nodelist.printnode()

num = int(input("请输入要插入的数："))
nodelist.insert(num)
nodelist.printnode()

num = int(input("请输入要删除的数："))
nodelist.delete(num)
nodelist.printnode()

num = int(input("请输入要查找的数："))
nodelist.search(num)

num = int(input("请输入要修改的数："))
num2 = int(input("请输入修改后的数："))
nodelist.recover(num, num2)
nodelist.printnode()

