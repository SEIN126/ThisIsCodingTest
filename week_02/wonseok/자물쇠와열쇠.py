import copy
# 90도 회전 함수
def rotate(a):
    n = len(a)
    m = len(a[0])
    
    result = [[0]*n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def check(key, lock, c, r):
    print("===========Check======")
    print(lock)
    print(key)
    lock_copy = copy.deepcopy(lock)
    key_col = 0
    for cc in range(c, len(lock_copy)):
        key_row = 0
        for rr in range(r, len(lock_copy[0])):
            lock_copy[cc][rr] += key[key_col][key_row]   
            key_row += 1
        key_col += 1

    print(lock_copy)
    for lock_row in lock_copy:
      for i in lock_row:
        if i != 1:
          return False
    return True
    
def solution(key, lock):
    # 원본, 90도 회전, 180도 회전, 270도 회전한 key의 list
    key_list = [key, rotate(key), rotate(rotate(key)), rotate(rotate(rotate(key)))]
    lock_list = [lock, rotate(lock), rotate(rotate(lock)), rotate(rotate(rotate(lock)))]
    
    # 모든 위치에 모든 가능한 회전된 키를 삽입해본다.
    for locks in lock_list:
        row_len = len(locks[0])
        col_len = len(locks)
        for c in range(col_len):
            for r in range(row_len):
                for k in key_list:
                    if check(k, locks, c, r):
                        return True
    
    return False
