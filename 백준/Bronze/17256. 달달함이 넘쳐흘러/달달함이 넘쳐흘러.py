A_X, A_Y, A_Z = map(int, input().split())
C_X, C_Y, C_Z = map(int, input().split())
print(C_X-A_Z, C_Y//A_Y, C_Z-A_X, end="")