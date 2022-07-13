a, b, v = map(int, input().split()) # map(함수, 리스트): 리스트를 함수로 변환
# -> 공백 구분으로 입력받은 문자열을 정수로 변환한다.

#a: 일당 등반 높이, b: 일당 하강 높이, v: 막대 높이
day = (v-b) / (a-b) # 날짜 계산
print(int(day) if day == int(day) else int(day)+1)
