n, k = map(int, input().split())                    #보석 개수, 가방 적재량

jewel = [[0, 0]]                                    #보석 리스트, 0번에 (0,0)보석

for i in range(n):                                  
    jewel.append(list(map(int, input().split())))   #n개만큼 물건 받기

mat = [[0]*(k+1) for _ in range(n+1)]               #dp용 행렬 선언 n*(k+1)

for i in range(1, n+1):                             #첫번째 보석부터
    for j in range(1, k+1):                         #무게 1인 상태부터
        w = jewel[i][0]                             #보석 무게
        v = jewel[i][1]                             #보석 가치

        if j<w:
            mat[i][j] = mat[i-1][j]
        else:
            mat[i][j] = max(mat[i-1][j], mat[i-1][j-w]+v )

print(mat[n][k])