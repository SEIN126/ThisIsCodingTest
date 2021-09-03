from itertools import permutations

def solution(n, weak, dist):
  answer = len(dist) + 1  ## 친구들을 다 투입 해도 안 될 경우 생각해서 초기화

  num_weak = len(weak)  # weak의 전체 갯수
  # 원형을 일자 형태로 바꾼다.
  for l in range(num_weak):
    weak.append(weak[l] + n)

  # friends 순열조합
  friends_list = list(permutations(dist, len(dist)))

  for start in range(num_weak):
    for friends in friends_list:
      count = 1  # 투입한 친구의 수
      position = weak[start] + friends[count-1]  # 첫번째 투입한 친구가 갈 수 있는 위치

      for index in range(start, start+num_weak):
        if position < weak[index]:
          count += 1  # 다음 친구 투입
          if count < len(dist):  # 다음 친구 투입이 불가할 경우
            break
          position = weak[index] + friends[count-1]

      answer = min(answer, count)
      

  if answer > len(dist):
    return -1

  return answer

print(solution(12, [1,5,6,10], [1,2,3,4]))
print(solution(12, [1,3,4,9,10], [3,5,7]))
