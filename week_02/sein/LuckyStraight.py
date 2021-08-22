N = input()
# 중간 부분
half = len(N)//2
# map object로 매핑 후 앞, 뒷부분 sum 계산(근데 이부분 무조건 slicing 들어가서 big O 더이상 못줄일거같음..))
front = sum(map(int, N[:half]))
back  = sum(map(int, N[half:]))
# print
print('LUCKY' if front == back else 'READY')