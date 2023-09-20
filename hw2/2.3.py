path1 = [[6],[6,7,8],[7,9],[8,9],[9,10],[1,2],[2,3],[2,4],[3,5],[5]]
state = ['人羊狼菜','人狼菜','人羊狼','人羊菜','人羊','狼菜','狼','菜','羊','空']
def findPath(n,path):
    if(n == 10):
        for i in path:
            print(state[i - 1],end=" ")
        print()
        return
    pnow = path + [n]
    for i in path1[n-1]:
        if(not(i in pnow)):
            findPath(i,pnow)

findPath(1,[])
