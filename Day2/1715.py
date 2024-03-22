# 가장 큰 수는 1번, 가장 작은 수는 n - 1번

N = int(input())

stackList = []
result = 0

for _ in range(N):
    stackList.append(int(input()))

stackList.sort()

for i in range(N):
    if i == N - 1:
        result += stackList.pop() * 2
    else:
        result += stackList.pop() * (i + 1)

print(result)
