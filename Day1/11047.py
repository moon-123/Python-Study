N, K = map(int, input().split())

coinList = []
result = 0

for _ in range(N):
    coinList.append(int(input()))

for c in range(N):
    ele = coinList.pop()
    if ele > K:
        continue

    elif ele == K:
        result += 1
        break

    else:
        count = K // ele
        result += count
        K -= count * ele
    
print(result)