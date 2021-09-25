import itertools
        
N = int(input())

days = []
data = []
for n in range(N):
    days.append(n)
    data.append(list(map(int, input().split())))


# 1~N개의 날짜 조합구한다. 
# (ex. [1,2,3] N=3개 => [1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]])
# 날짜조합마다 상담 가능한 모든날에 대한 금액을 더한다.
# 모든 조합에 대한 금액합의 최대값을 업데이트한다.

result = 0  # 출력값 초기화
# 1~N개 상담날에 대한 모든 조합 
# (ex. [1,2,...,n], N개 => [1],[2],...,[n],...,[1,2,...,n])
for i in range(1, len(data)+1):
    for selecteddays in itertools.combinations(days, i):
        # 각 상담날짜 조합에 대해
        # 상담 가능한 날짜의 금액 더해준다.
        money = 0  # 금액 초기화
        nextday = 0  # 다음상담가능날 초기화
        for d in selecteddays:
            # 다음날짜가 다음상담가능날 보다 크거나 같으면 진행
            if d >= nextday:  
                startday = d  # 상담날
                nextday = startday + data[d][0]  # 다음상담가능날
                if nextday <= N:  # 퇴사일 안에 상담이 가능하면
                    money += data[startday][1]  # 금액 합한다.
                else:  # 퇴사일 안에 상담 불가능하면 break
                    break
        result = max(result, money)  # 최대금액 업데이트
print(result)
