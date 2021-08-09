N = int(input())
data = list(map(int, input().split()))
# sorting to desc
data.sort(reverse=True)
# group 수
group_n = 0
# data index
data_idx = 0
# data_idx가 사람 수 N보다 커지면 끝
while(data_idx < N):
  data_idx += data[data_idx]
  group_n += 1

print(group_n)