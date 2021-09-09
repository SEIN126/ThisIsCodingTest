import sys
input= sys.stdin.readline
d_x=[-1,0,1,0]
d_y=[0,1,0,-1]
ind=-1
N=int(input())
x=N//2+2
y=N//2+2
A = [[0 for i in range(N+4)] for i in range(2)]
for i in range(N):
    A.append([0,0]+list(map(int,input().split()))+[0,0])
for i in range(2):
    A.append([0 for i in range(N+4)])

Nu=1
s=0
ke=1
while(ke):
    Nu+=1
    ind=(ind+1)%4
    for i in range(Nu//2):
        x+=d_x[ind]
        y+=d_y[ind]
        if x<2:
            ke=0
            break
        if A[y][x]==0:
            continue
        else:
            A[y+2*d_x[ind]][x+2*d_y[ind]]+=int(0.02*A[y][x])
            A[y-2*d_x[ind]][x-2*d_y[ind]]+=int(0.02*A[y][x])
            A[y+d_x[ind]][x+d_y[ind]]+=int(0.07*A[y][x])
            A[y-d_x[ind]][x-d_y[ind]]+=int(0.07*A[y][x])
            A[y+d_x[ind]+d_y[ind]][x+d_y[ind]+d_x[ind]]+=int(0.1*A[y][x])
            A[y-d_x[ind]+d_y[ind]][x-d_y[ind]+d_x[ind]]+=int(0.1*A[y][x])
            A[y+d_x[ind]-d_y[ind]][x+d_y[ind]-d_x[ind]]+=int(0.01*A[y][x])
            A[y-d_x[ind]-d_y[ind]][x-d_y[ind]-d_x[ind]]+=int(0.01*A[y][x])
            A[y+2*d_y[ind]][x+2*d_x[ind]]+=int(0.05*A[y][x])
            A[y+d_y[ind]][x+d_x[ind]]=A[y+d_y[ind]][x+d_x[ind]]+A[y][x]-2*int(0.01*A[y][x])-2*int(0.1*A[y][x])-2*int(0.07*A[y][x])-2*int(0.02*A[y][x])-int(0.05*A[y][x])
            A[y][x]=0

s= sum(A[0])+sum(A[1])+sum(A[-1])+sum(A[-2])

for i in range(2,N+2):
    s+=A[i][0]+A[i][1]+A[i][-1]+A[i][-2]
print(s)
