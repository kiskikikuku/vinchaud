table = [[0 for i in range(10)] for row in range(10)] # 10X10 크기의 상자 생성

for i in range(10):
    table[i] = list(map(int, input().split()))

x = int(1)
y = int(1) #개미의 출발 좌표(2,2이므로 두 번째 행렬의 인덱스 1,1 대입)

while (table[x][y] !=2): #멈춘 칸의 값이 2(먹이)가 아닌 경우 반복
    if (x>=9 or y>=9): #상자의 범위를 벗어나는 경우 반복문 중단
        break
    table[x][y] = 9
    if table[x][y+1]!=1: #오른쪽 칸이 벽이 아닌경우
         y = y+1
    else :
         x = x+1
         
if (table[x][y]== 2): #먹이 발견한 경우 9로 칠하기
    table[x][y] = 9

for i in range(10):
    for j in range(10):
        print(table[i][j], end=' ')
    print() #전체 출력