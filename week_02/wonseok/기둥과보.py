def possible(answer):
    for x, y, what in answer:
        # 기둥일 경우
        if what == 0:
            # 기둥 설치 가능한 경우
            # "바닥위" / "보의 한쪽 끝 위" / "다른 기둥 위"
            if y == 0 or ([x-1, y, 1] in answer) or ([x, y, 1] in answer) or ([x, y-1, 0] in answer):
                continue
            else:
                return False
        # 보일 경우
        else:
            # 보 설치 가능한 경우
            # "한쪽 끝이 기둥" / "양쪽 끝이 다른 보"
            if ([x,y-1,0] in answer) or ([x+1,y-1,0] in answer) or (([x-1,y,1] in answer) and ([x+1,y,1] in answer)):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for cmd in build_frame:
        x, y, what, how = cmd
        # 삭제 하는 경우
        if how == 0:
            answer.remove([x, y, what])
            if not possible(answer):
                answer.append([x, y, what])
        # 설치 하는 경우
        else:
            answer.append([x,y,what])
            if not possible(answer):
                answer.remove([x, y, what])
    return sorted(answer)
