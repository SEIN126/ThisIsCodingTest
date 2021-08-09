import sys
import math

data = input()
prev = data[0]
count = 0

# 0->1, 1->0으로 몇 번 바뀌는지 찾는다.
for i in range(1, len(data)):
    now = data[i]
    if prev != now:
        count += 1
        
    prev = now

# 0->1 또는 1->0이 
# 총 1번 또는 2번 바뀌면 총 1번만 바꿔주면 된다.
# 총 3번 또는 4번 바뀌면 총 2번만 바꿔주면 된다.
# ...
result = math.ceil(count / 2)

print(result)
