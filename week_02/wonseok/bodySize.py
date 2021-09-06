N = int(input())

plist = []
for _ in range(N):
  plist.append(list(map(int, input().split())))

for data in plist:
  count = 1
  for others in plist:
    if data[0] < others[0] and data[1] < others[1]:
      count += 1
  print(count, end=" ")
