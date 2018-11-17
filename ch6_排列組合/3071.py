def fact(n = 0) :
    total = 1
    for i in range(1, n+1) :
        total = total * i
    return total

def P(n, m) :
    return fact(n) / fact(n - m)

n1 = int(input())
n2 = int(input())
ans = P(n1, n2)
print(int(ans))