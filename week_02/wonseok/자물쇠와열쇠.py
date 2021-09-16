# 90도 회전 함수
def rotate(a):
    n = len(a)
    m = len(a[0])
    
    result = [[0]*n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def check(key, lock):
    print("===========Check======")
    print(lock)
    print(key)
    key_col = 0
    for c in range(len(lock)):
        key_row = 0
        for r in range(len(lock[0])):
            # 홈과 홈 또는 돌기와 돌기가 만날 경우
            if lock[c][r] == key[key_col][key_row]:
                return False
            key_row += 1
        key_col += 1
    return True
    
def solution(key, lock):
    # 원본, 90도 회전, 180도 회전, 270도 회전한 key의 list
    key_list = [key, rotate(key), rotate(rotate(key)), rotate(rotate(rotate(key)))]
    
    # 모든 위치에 모든 가능한 회전된 키를 삽입해본다.
    row_len = len(lock[0])
    col_len = len(lock)
    for c in range(col_len):
        for r in range(row_len):
            new_lock = [row[r:row_len] for row in lock[c:col_len]]
            for k in key_list:
                if check(k, new_lock):
                    return True
    
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
