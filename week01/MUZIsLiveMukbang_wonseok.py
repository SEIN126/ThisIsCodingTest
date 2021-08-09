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



# 위 보다 빠르지만 효율설 실패...
import numpy as np

def solution(food_times, k):
    f_t = np.array(food_times)
    left = np.arange(1, len(f_t) + 1)
    
    if np.sum(f_t) == k:
        return -1
    
    epoch = 1
    while True:
        mask = np.where(f_t >= epoch)
        length = len(f_t[mask])
        
        if k >= length:
            k -= length
            epoch += 1
        else:
            left = left[mask]
            return int(left[k])
            break
