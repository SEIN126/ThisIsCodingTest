from itertools import permutations

def solution(n, weak, dist):
  # 친구들 다 투입 해도 안될때를 위해 초기화
  answer = len(dist) + 1

  # 원형의 weak를 일자로 펴준다
  len_weak = len(weak)
  for w in range(len_weak):
    weak.append(weak[w] + n)

  for start in range(len_weak):
    # 모든 친구의 순열
    for friends in permutations(dist, len(dist)):
      count = 1  # 시작 지점마다 필요한 친구의 수 초기화
      next_pos = weak[start] + friends[count - 1]  #첫번째 친구가 이동 할 수 있는 위치

      # 갈 수 있는 위치와 모든 weak 확인
      for index in range(start, start + len_weak):
        # 다음 weak까지 갈 수 없다면 다음 친구 투입
        if next_pos < weak[index]:
          count += 1
          # 더 이상 투입할 친구가 없다면
          if count > len(dist):
            break
          next_pos = weak[index] + friends[count - 1]  # 다음 친구가 갈 수 있는 위치
      answer = min(answer, count)

  if answer > len(dist):
    return -1
  else:
    return answer


print(solution(12, [1,5,6,10], [1,2,3,4]))
print(solution(12, [1,3,4,9,10], [3,5,7]))
