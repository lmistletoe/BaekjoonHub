N,M,K = map(int, input().split())
N = K//M
M = K%M
print(N, M, end="")