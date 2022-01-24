n = int(input())
time_table = list(map(int, input().split()))
time_table.sort()
total_waiting_time = int(0)

for i in range(n):
    total_waiting_time += (n-i)*time_table[i]
    
print(total_waiting_time)