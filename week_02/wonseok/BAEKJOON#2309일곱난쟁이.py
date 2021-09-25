import itertools

# 9난쟁이 리스트 생성
data = []
for _ in range(9):
    data.append(int(input()))

# 9난쟁이 중에서 7난쟁이 조합 생성
# 조합 중에서 합이 100이면 조합을 오름차순으로 출력하고 break
for dwalfs in itertools.combinations(data, 7):
    if sum(dwalfs) == 100:
        for i in sorted(dwalfs):
            print(i)
        break
    
