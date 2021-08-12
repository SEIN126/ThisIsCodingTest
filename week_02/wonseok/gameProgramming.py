n, m = map(int, input().split())

# 방문 여부를 저장하는 2차원 리스트
visited = [[0] * m for _ in range(n)]

# 현재 위치, 바라보는 방향
x, y, direction = map(int, input().split())
visited[x][y] = 1  # numpy는 array[x, y]로 가능. list와 다르다.

# 지도 생성
map_ = []
for i in range(n):
  map_.append(list(map(int, input().split())))

# 바라보는 방향으로 이동했을 때의 위치
dx = [-1, 0 , 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수
def turn_left():
  global direction
  direction += 1
  if direction == 4:
    direction = 0
  return direction


count = 1
turn_time = 0
while True:
  # 바라보는 방향
  turn_left()
  # 정면을 바라보는 위치
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전 후 정면에 가보지 않은 칸이 존재하고 땅인 경우 이동
  if visited[nx][ny] == 0 and map_[nx][ny] == 0:
    visited[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  else:
    turn_time += 1

  # 4 방향 모든 가봤거만 못 갈 때
  if turn_time == 4:
    # 뒤를 돌아볼때 위치
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 갈 수 있다면 이동
    if map_[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_time = 0

print(count)
