import itertools
N, M = map(int, input().split())

chicken, house = [], []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 2:
            chicken.append([i,j])
        elif row[j] == 1:
            house.append([i,j])
            
result = float("inf")  # 출력 초기화

## 순열로 하면 중복 되는것 때문에 시간 초과 된다!!
"""
# 폐업 시키지 않을 치킨 집의 순열 만큼 반복하여 확인
for ckn in itertools.permutations(chicken, M):
    total_distance = 0  # 모든 집의 치킨거리의 합
    # 선택된 치킨 집을 대상으로 거리 조사
    for H in house:
        distance = float("inf")  # 현재 집의 치킨거리 초기화
        for C in ckn:
            dist = abs(H[0]-C[0]) + abs(H[1]-C[1])
            distance = min(distance, dist)  # 치킨집중에서 적은 거리의 치킨집 치킨거리로 선택
        total_distance += distance  # 모든 집에 대한 치킨거리 더하기
    # 폐업하지 않은 치킨집을 대상으로 조사한 모든집의 치킨거리의 합
    result = min(result, total_distance)  # 치킨거리의 합 비교하여 작은거 선택
"""


# 조합으로 해야 중복된거 없이 할 수 있어 통과!!
# 폐업 시키지 않을 치킨 집의 조합만큼 반복확인
for ckn in itertools.combinations(chicken, M):
    total_distance = 0  # 모든 집의 치킨거리의 합
    # 선택된 치킨 집을 대상으로 거리 조사
    for H in house:
        distance = float("inf")  # 현재 집의 치킨거리 초기화
        for C in ckn:
            dist = abs(H[0]-C[0]) + abs(H[1]-C[1])
            distance = min(distance, dist)  # 치킨집중에서 적은 거리의 치킨집 치킨거리로 선택
        total_distance += distance  # 모든 집에 대한 치킨거리 더하기
    # 폐업하지 않은 치킨집을 대상으로 조사한 모든집의 치킨거리의 합
    result = min(result, total_distance)  # 치킨거리의 합 비교하여 작은거 선택

print(result)
