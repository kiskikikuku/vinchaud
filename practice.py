table = [[0 for i in range(10)] for row in range(10)] # 10X10 크기의 상자 생성

for i in range(10):
    table[i] = list(map(int, input().split()))

x = int(1)
y = int(1)

while table[x][y] !=2:
    table[x][y]=9
    if x<9 and y<9:
        if table[x][y+1]!=1:
         y = y+1
        else :
         x = x+1

table[x][y]=9

for i in range(10):
    for j in range(10):
        print(table[i][j], end=' ')
    print()