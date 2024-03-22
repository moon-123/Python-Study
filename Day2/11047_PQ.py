from queue import PriorityQueue

N, K = map(int, input().split())

coinQue = PriorityQueue()
result = 0

for _ in range(N):
    coinQue.put(int(input()))

while coinQue.empty() != -1:
    el = coinQue.get()
    print(el)
    if el > K:
        continue
    elif el == K:
        result += 1
        break
    else:
        tick = K // el
        result += tick
        K %= el * tick

print(result)
