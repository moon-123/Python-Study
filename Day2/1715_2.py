# 가장 큰 수는 1번, 가장 작은 수는 n - 1번

N = int(input())

stackList = []
result = 0

for _ in range(N):
    stackList.append(int(input()))

stackList.sort(reverse=True)
x = stackList.pop()

while True:
    y = stackList.pop()
    x += y + x

    if len(stackList) == 0:
        break

print(x)
