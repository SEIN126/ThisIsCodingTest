N, M = map(int, input().split())

result = 0
for n in range(N):
  list_ = list(map(int, input().split()))
  
  # 현재 줄의 min 값
  min_ = min(list_)
  
  # 전고 현재 줄의 min 값 중에서 max 값
  result = max(min_, result)

print(result)
