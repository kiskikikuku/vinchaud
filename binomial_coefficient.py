def fact_re(a):
    result = 1
    for i in range(a, 1, -1):
        result *= i

    return result

n, k = map(int, input().split())

print(int(fact_re(n) / (fact_re(n-k)*fact_re(k))))