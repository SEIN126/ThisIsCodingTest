N = int(input())

# 한수 count
count = 0
# 1부터 입력된 수까지 한수인지 확인
for n in range(1, N+1):
  n_str = str(n)

  # 1, 2자리 수는 무조건 한수
  if len(n_str) == 1 or len(n_str) == 2:
    count += 1
  # 3자리 수 이상은 한수 확인해야됨
  # 첫번째랑 두번째 수의 차이 저장하고 나머지 인접한 수들의 차이를 하나씩 비교
  else:
    # 첫번째랑 두번째 수의 차이 저장
    b_diff = int(n_str[1]) - int(n_str[0])
    
    # 첫째자리부터 하나씩 확인
    for i in range(len(n_str)):
      # 마지막 자리까지 break 안걸리고 왔으면 넌 한수다!
      if i == len(n_str)-1:
        count += 1
        break
      
      # 모든 인접한 수의 차이 계산하고 비교, 만약 다르면 break 걸고 넌 한수가 아니다..
      diff = int(n_str[i+1]) - int(n_str[i])
      if diff != b_diff:
        break

print(count)
