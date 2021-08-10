# import numpy as np

# def cycle(f_t, k, left):
#     k -= len(f_t)
#     f_t -= [1]
#     # left = np.delete(left, np.where(f_t == 0))
#     # f_t = np.delete(f_t, np.where(f_t == 0))
#     mask = np.where(f_t != 0)
#     left = left[mask]
#     f_t = f_t[mask]
#     return f_t, k, left

# def solution(food_times, k):
#     f_t = np.array(food_times)
#     answer = 0
#     left = np.arange(1, len(food_times)+1)
    
#     if np.sum(f_t) == k:
#         return -1

#     while True:
#         # print(f_t, left, len(f_t), k)
#         if len(f_t) > k:
#             answer = left[k]
#             break
#         else:
#             f_t, k, left = cycle(f_t, k, left)
            
#     return int(answer)



# # 위 보다 빠르지만 효율설 실패...
# import numpy as np

# def solution(food_times, k):
#     f_t = np.array(food_times)
#     left = np.arange(1, len(f_t) + 1)
    
#     if np.sum(f_t) == k:
#         return -1
    
#     epoch = 1
#     while True:
#         mask = np.where(f_t >= epoch)
#         length = len(f_t[mask])
        
#         if k >= length:
#             k -= length
#             epoch += 1
#         else:
#             left = left[mask]
#             return int(left[k])
#             break



# 유튜브 참고...
from operator import itemgetter

def solution(food_times, k):
    food_dict = []
    food_len = len(food_times)
    # (걸리는 시간, 음식 번호) 의 list를 만든다.
    for i in range(food_len):
        food_dict.append((food_times[i], i + 1))
    # 걸리는 시간 순으로 list를 정렬한다.
    food_dict.sort()
    
    # 걸리는 시간이 작은것 순으로 남은 음식갯수를 곱해서 빼준다
    prev_time = 0
    for i, food in enumerate(food_dict):
        # 현재 음식과 이전 음식 걸리는 시간의 차이
        diff_time = food[0] - prev_time
        
        # 시간의 차이가 있으면 
        if diff_time != 0:
            spent = diff_time * food_len
            if spent <= k:
                k -= spent
                prev_time = food[0]
            else:
                k %= food_len
                left = sorted(food_dict[i:], key = itemgetter(1))
                return left[k][1]
        
        food_len -= 1
            
    return -1
