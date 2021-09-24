def solution(s):
    answer = len(s)
    # 1 개 단위로 부터 압축뉘단위를 늘려가며 확인
    for step in range(1, len(s) //2 + 1):
        encoded = ""
        prev = s[:step]  
        count = 1
        # 단위(step) 크기만큼 증가시저며 이전 문자열과 비료
        for j in range(step, len(s), step):
            # 이전 상테와 동일 하면 압축 횟수(count) 증가
            if prev == s[j:j+step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우하면)
            else:
                encoded += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1
        # 남아있는 문자열에 대해서 처리
        encoded += prev if count == 1 else str(count) + prev
        # 만들어진 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(encoded))
    return answer

# print(solution("ababcdcdababcdcd"))
