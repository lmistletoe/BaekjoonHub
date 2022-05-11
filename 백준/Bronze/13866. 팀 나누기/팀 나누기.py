li = list(map(int, input().split()))
li.sort()
A = li[0] + li[3]
B = li[1] + li[2]
print(abs(A-B))