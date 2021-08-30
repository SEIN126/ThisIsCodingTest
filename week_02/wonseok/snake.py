N = int(input())
# 기본 지도 map_:0
map_ = [[0]*N for _ in range(N)]

# 사과가 있는 위치 map_:1
K = int(input())
for k in range(K):
  ax, ay = map(int, input().split())
  map_[ax-1][ay-1] = 1

# 방향 전환 순서
L = int(input())
order = []
for l in range(L):
  x, C = input().split()
  order.append((int(x), C))

# direction: 0, 1, 2, 3
# direction: 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 방향 전환 함수
def turn(direction, cmd):
  if cmd == "D":
    direction = (direction + 1) % 4
  else:
    direction = (direction -1) %  4
  return direction  


x, y = 1, 1  # 현재 위치
direction = 0  # 시작 방향
map_[x-1][y-1] = 2  # 방문 했던 위치 표시
q = [(x, y)]  # 뱀이 차지 하고 있는 위치
index = 0  # 방향 전환 인덱스
t = 0  # 시간

while True:
  # 방향 전환이 필요한지 확인
  if index < L and order[index][0] == t:
    direction = turn(direction, order[index][1])
    index += 1
  
  # 다음 이동할 위치 확인
  t += 1
  nx = x + dx[direction]
  ny = y + dy[direction]

  # 다음 위치로 이동이 불가능 한 경우

  # 다음 이동할 위치가 벽인 경우
  if not 1<=nx<=N or not 1<=ny<=N:
    break
  # 다음 이동할 위치가 몸통인 경우
  if map_[nx-1][ny-1] == 2:
    break
  
  # 다음 위치로 이동이 가능한 경우

  # 다음 위치에 사과가 있는 경우
  if map_[nx-1][ny-1] == 1:
    x, y = nx, ny  # 다음 위치로 이동
    map_[x-1][y-1] = 2  # 이동한 위치 표시
    q.append((x, y))  # 뱀이 차지하는 위치 저장
  #다음 위치에 사과가 없는 경우
  else:
    x, y = nx, ny  # 다음 위치로 이동
    map_[x-1][y-1] = 2  # 이동한 위치 표시
    q.append((x, y))  # 뱀이 차지하는 위치 저장

    tx, ty = q.pop(0)  # 뱀의 꼬리 위치 확인 및 삭제
    map_[tx-1][ty-1] = 0  # 뱀의 꼬리 였던 위치 다시 map_:0 으로 변경

  print(map_)

print(t)
