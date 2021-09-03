score = input()


# 중간 지점
n = len(score) // 2

# 앞부분 점수 계산
f_point = 0
for i in score[:n]:
  f_point += int(i)
# 뒷부분 점수 계산
b_point = 0
for i in score[n:]:
  b_point += int(i)

# 앞, 뒤 점수 확인 및 결과 출력
if f_point == b_point:
  print("LUCKY")
else:
  print("READY")
