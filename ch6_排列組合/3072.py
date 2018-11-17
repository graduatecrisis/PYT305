import math
def C(n, m) :
    return math.factorial(n) / (math.factorial(m) * math.factorial(n - m))
n1 = int(input())
n2 = int(input())
ans = C(n1, n2)
print(int(ans))