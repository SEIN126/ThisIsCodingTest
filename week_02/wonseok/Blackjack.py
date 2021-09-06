import itertools

N, M = map(int, input().split())

card_list = list(map(int, input().split()))

possible_list = list(itertools.permutations(card_list, 3))

answer = 0
for cards in possible_list:
  pos_answer = sum(cards)
  if pos_answer <= M:
    answer = max(answer, pos_answer)
print(answer)
