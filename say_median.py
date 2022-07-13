import heapq

maxheap = []
minheap = []

n = int(input())

median = int(input())

print(median)

for i in range(n-1):
    temp = int(input())
    if median < temp:
        heapq.heappush(maxheap, (-i, temp))
    else:
        heapq.heappush(temp, minheap)
    