import collections
import sys
input = sys.stdin.readline
N=int(input())
x=[]
for i in range(N):
    x.append(int(input()))
x=sorted(x)
print(round(sum(x)/N))
print(x[N//2])
com = collections.Counter(x).most_common(2)
if len(com)==1:
    print(com[0][0])
else:
    if com[0][1]==com[1][1]:
        if com[0][1]==com[1][1]:
            print(com[1][0])
        else:
            print([0][0])
    else:
        print(com[0][0])
print(max(x)-min(x))
