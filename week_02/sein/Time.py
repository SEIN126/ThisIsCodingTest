N = int(input())

cnt = 0

# 24를 입력받는다 해도,
# 전체 경우의 수는 24*60*60 = 86400 번이므로 100,000개, 즉 10만개도 되지 않는다.
# 통상적으로 data가 백만개까지는 완전 탐색으로 가능.
for h in range(N+1):
  for m in range(60):
    for s in range(60):
      t = str(h) + str(s) + str(m)
      if '3' in t :
        cnt += 1

print(cnt)