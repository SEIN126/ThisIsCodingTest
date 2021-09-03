position = input()

row = int(position[1])
col = int(ord(position[0]))-int(ord("a")) + 1 

# movement 총 8가지
# dx dy
# 2  1
# 1  2
# 2  -1 
# 1  -2
# -2 -1
# -1 -2 
# -2 1
# -1 2

movement = [(2,1), (1,2), (2,-1), (1,-2), (-2,-1),(-1,-2),(-2,1),(-1,2)]

count = 0
for m in movement:
  new_row = row + m[0]
  new_col = col + m[1]
  if new_row>=1 and new_row<=8 and new_col>=1 and new_col<=8:
    count += 1 

print(count)
