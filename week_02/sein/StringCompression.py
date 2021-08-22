def solution(sentence):
    count = len(sentence)

    # 1 에서 half 까지 전부 탐색
    for slices in range(1, len(sentence) // 2 + 1):
        # slice 별 압축된 문장의 길이
        tmp_count = 0

        # 연속 중인 지 확인
        # 각각 0에서 1번 반복, 10개이상 반복, 100개이상 반복, 1000개 이상 반복 되는 flag
        flag = 0
        flag_ten = 0
        flag_hun = 0
        flag_tho = 0

        # 비교하기 위한 첫 뭉치
        # range의 경우 나누어떨어지면 slice만큼만 마지막에 냅두고, 아니면 나머지만큼만 냅둔다
        start = sentence[:slices]
        for s in range(slices - 1, len(sentence) - slices if len(sentence) % slices == 0 \
                else len(sentence) - len(sentence) % slices, slices):
            # 같은 경우
            if start == sentence[s + 1: s + 1 + slices]:
                # flag가 안올려져있는 경우 : 해당 start에 대해서 최초로 반복되는 경우를 발견한 경우
                if flag == 0:
                    tmp_count += 1
                    flag = 1
                # 반복은 계속 되고 있는데, 반복되는 횟수가 10, 100, 1000회 넘어가는지 확인
                else:
                    flag += 1
                    if flag >= 9:
                        if flag_ten == 0:
                            tmp_count += 1
                            flag_ten = 1
                    if flag >= 99:
                        if flag_hun == 0:
                            tmp_count += 1
                            flag_hun = 1
                    if flag >= 999:
                        if flag_tho == 0:
                            tmp_count += 1
                            flag_tho = 1

            # 다른 경우
            else:
                # 이전 뭉치에 대한 길이만큼 count 추가
                tmp_count += slices
                # flage 내림
                flag = 0
                flag_ten = 0
                flag_hun = 0
                flag_tho = 0
                # 다음 뭉치로 sen 변환
                start = sentence[s + 1: s + 1 + slices]

        # 마지막 뭉치에 대한 길이 추가
        tmp_count += slices if len(sentence) % slices == 0 else len(sentence) % slices
        # print(slices, tmp_count)
        count = min(tmp_count, count)

    return count