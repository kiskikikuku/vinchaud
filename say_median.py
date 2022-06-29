import heapq

heap = []

n = int(input())

for i in range(n):
    heapq.heappush(heap, int(input()))    
    if(i % 2 ==0):
        print(heap[int(i/2)])
    else:
        print(heap[int((i+1)/2)])


print(heap)