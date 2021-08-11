# data = input().split()
# N = int(data[0])
# K = int(data[1])
N, K = map(int, input().split())

tokens = []
for i in range(N):
  token = int(input())
  # if token <= K:
  tokens.append(token)

count = 0
for i in reversed(tokens):
  if K >= i:
    count += (K//i)
    # K -= i * (K//i)
    K = K%i

  if K == 0:
    break

print(count)
