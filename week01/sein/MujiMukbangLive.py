import heapq

# example
food_times = [3, 3, 3]
k = 9

def solution(food_times, k):
    pq = []
    # priority queue에 [food_time, idx] 저장
    for i in range(len(food_times)):
        heapq.heappush(pq, (food_times[i], i + 1))
    # food 갯수
    food_n = len(food_times)
    # 꺼낸 음식
    before = 0
    while (pq):
        # 가장 시간이 적게 걸리는 음식을 다 먹는데 걸리는 시간
        t = (pq[0][0] - before) * food_n

        # 음식을 하나 다먹었는데 시간이 남음
        if k - t >= 0:
            k = k - t
            # 음식을 빼줌
            before, _ = heapq.heappop(pq)
            # 갯수도 빼줌
            food_n = food_n - 1
            # 음식을 다 먹은 case
            if not pq:
                return -1
        # 음식을 다 먹기에 시간이 부족한 상황
        else:
            # 먹을 수 있는 idx 구함
            idx = k % food_n
            # 음식 순서에 따라서 다시 정렬
            pq.sort(key=lambda x: x[1])
            answer = pq[idx][1]
            break
    return answer

# check the solution, -1
print(solution(food_times, k))