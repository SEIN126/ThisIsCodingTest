N, K = map(int, input().split())


count = 0

while True:
  # N이 K보다 작으면 N이 1이 될때까지 빼준다. => 빼준만큼 count
  if N < K:
    count += N -1
    break
  
  # N이 K로 안 나눠진다면 K의 배수가 될때까지 빼준다. => 빼준만큼 count
  if N % K != 0:
    count += N % K
    N -= count
  
  # N을 K로 나눠준다. => 누눴으니 한번 count
  N = N // K
  count += 1
  
  # N이 1이면 stop
  if N == 1:
    break

print(count)
