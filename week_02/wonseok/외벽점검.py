from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    
    length = len(weak)  # 공사가 필요한 위치 수
    # 원형을 일자로 펴준다
    for i in range(length):
        weak.append(weak[i] + n)
    
    # 0~>length 돌아가면서 확인
    for start in range(length):
        # 친구 투입하는 순서 경우의 수 모두 고려
        for distance in permutations(dist, len(dist)):
            # 첫번째 친구 투입
            count = 1
            position = weak[start] + distance[count-1]  # 친구가 갈 수 있는 위치
            
            for k in range(start+1, j+length):
                # 다음 위치까지 친구가 도달 못 한다면
                if position < weak[k]:
                    # 다음 친구 투입
                    count += 1  
                    if count > len(dist):  # 모든 친구가 다 투입 되었다면 종료
                        break
                    position = weak[k] + distance[count-1]  # 다음 친구가 갈 수 있는 위치
            answer = min(answer, count)  # 투입된 친구의 수

    if answer > len(dist):
        return -1
    else:
        return answer
                    
                    
                
            
    
    
    
    
    return answer
