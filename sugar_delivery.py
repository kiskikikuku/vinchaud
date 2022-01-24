n = int(input()) # 배달할 설탕의 정수 무게 'n' 입력받기

x =int(0)

while n>=0:
    if n%5 == 0: # n이 5의 배수인 경우
        x += (n // 5)
        print(x)
        break

    n-=3
    x+=1

else:
    print(-1)
