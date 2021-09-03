N = int(input())
map_ = [[0]*N for _ in range(N)]

K = int(input())

# 사과가 있는 위치 리스트 만든다
apple = [[0]*N for _ in range(N)]
for k in range(K):
  ax, ay = map(int, input().split())
  apple[ax-1][ay-1] = 1
  
  
# direction 
# 동 남 서 북
# 0  1  2  3
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
# 방향 전환 함수
def turn(direction, turning):
  if turning == "D":
    direction += 1 
    if direction == 4:
      direction = 0
  else:
    direction += -1
    if direction == -1:
      direction = 3
      
  return direction
  
L = int(input())
order =[]
for l in range(L):
  x, C = input().split()
  order.append((int(x), C))
  
  
# 시작 방향은 북쪽
direction = 0
# 시작 지점
x, y = 1, 1
# 의이 차지 하고 있는 위치
q = [(x, y)]
map_[x-1][y-1] = 1
# 방향 전환 인덱스
index = 0
t = 0
print(map_)
print("========초기=========")

while True:
  # 방향이전환이 필우할 경우
  if index <L and order[index][0] == t:
    print(index, order)
    direction = turn(direction, order[index][1])
    index += 1

  
  
  # 방향 전환이 아닐때
  nx = x + dx[direction]
  ny = y + dy[direction]
  print("===nx, ny:", nx, ny)
  
  # 다음 위치가 벽인 경우
  if not 1<=nx<=N or not 1<=ny<=N:
    t += 1
    print(" 벽과 충돌!! ")
    break
  
  # 다음 위치가 벽이 아닌 경우
  # 다음 위치가 몸통인 경우
  if map_[nx-1][ny-1] == 1:
    t += 1
    print("몸통과 충동 !!")
    break
  # 다음 위치로 이동이 가능한 경우
  else:
    # 다음 위치에 사과가 있는 경우
    if apple[nx-1][ny-1] == 1:
      apple[nx-1][ny-1] = 0  # <============이것 때문에 wrong!! 사과 먹었으면 없애줘야지~~~
      #  꼬리를 놔두고 머리는 다음 위치로 이동
      x, y = nx, ny
      q.append((nx, ny))
      map_[x-1][y-1] = 1
    # 다음 위치에 사과가 없는 경우
    else:
      # 꼬리를 가지고 다음 위치로 이동
      x, y = nx, ny
      q.append((nx, ny))
      px, py = q.pop(0)
      map_[x-1][y-1] = 1
      map_[px-1][py-1] = 0
    t += 1
      
  print(map_)  
print(t)
