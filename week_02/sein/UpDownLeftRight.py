move = list(map(str, input().split()))
print(move)
x, y = 1, 1

command = ['U', 'D', 'L', 'R']
x_m = [-1, 1, 0, 0]
y_m = [0, 0, -1, 1]

for mo in move:
  # 이동이 어떤 커맨드와 매칭되는지 확인
  for idx in range(len(command)) :
    if mo == command[idx] :
      x_n = x + x_m[idx]
      y_n = y + y_m[idx]
  # 이동이 끝난 후 좌표 체크
  if x_n < 1 or x_n > N or y_n < 1 or y_n > N :
    continue
  x = x_n
  y = y_n
print(x, y)