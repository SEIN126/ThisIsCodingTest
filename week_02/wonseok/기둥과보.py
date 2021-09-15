def solution(n, build_frame):
    answer = []
    
    # 벽면 초기화
    wall = [[0]*(n+1) for _ in range(n+1)]
    # 벽면에 설치된게 뭔가 (0 기둥, 1 보)
    what_wall = [[2]*(n+1) for _ in range(n+1)]
    
    for cmd in build_frame:
        x, y = cmd[0], 5-cmd[1]  # 좌표 값
        what, how = cmd[2], cmd[3]  # 무엇(0 기둥, 1 보), 어떻게(0 삭제, 1 설치)
        # print("=======", x,y,what,how)
        
        # 기둥
        if what == 0:
            # 기둥 설치
            if how == 1:
                # print("기둥 설치")
                # 기둥 설치를 위한 조건
                if y == 5 or wall[y][x] >= 1:
                    wall[y][x] += 1
                    wall[y-1][x] += 1
                    # 기둥 위치 기록
                    what_wall[5-y][x] = what
                    answer.append([x, 5-y, what])
            # 기둥 삭제  <= 보 뿐만 아니라 기둥도 삭제 가능한지 확인해야한다.....
            else:
                # print("기둥 삭제")
                wall[y][x] -= 1
                wall[y-1][x] -= 1
                # 기둥 삭제
                what_wall[5-y][x] = 0
                answer.remove([x, 5-y, what])
        # 보
        else:
            # 보 설치
            if how == 1:
                # print("보 설치")
                # 보 설치를 위한 조건
                if wall[y][x] >= 1 or wall[y][x+1] >= 1 or (wall[y][x] >= 1 and wall[y][x+1] >= 1):
                    wall[y][x] += 1
                    wall[y][x+1] += 1
                    # 기둥 위치 기록
                    what_wall[5-y][x] = what
                    answer.append([x, 5-y, what])
            # 보 삭제  <====  보 삭제에서 문제.... 보를 삭제 해도 되는지 아닌지 판단해야한다....
            else:
                # 이전 것이 보일 경우 그 보는 기둥에 걸려있어여햔다.
                # 이후 것이 보일 경우 그 보는 기둥에 걸려있어야한다
                # 둘다 만족해야 삭제 가능.
                if ((what_wall[5-y][x-1] == 1) and (what_wall[5-y][x-1] == 1)) and ((what_wall[5-y][x+1] == 1) and (what_wall[5-y+1][x+1] == 1)):
                    # print("보 삭제")
                    wall[y][x] -= 1
                    wall[y][x+1] -= 1
                    # 보 삭제
                    what_wall[5-y][x] = 0
                    answer.remove([x, 5-y, what])
        # print(wall)

    answer.sort()
    return answer




