
d_x=[1, 0, -1, 0]
d_y=[0, 1, 0, -1]
N=int(input())
ind=0
maap  = [[0 for i in range(N)] for j in range(N)]
K=int(input())
for i in range(K):
    m,n=map(int,input().split())
    maap[m-1][n-1]=1
L=int(input())
x=0
y=0
snake=[[0,0]]
maap[x][y]=2
time=0
k=0
di = []
for i in range(L):
    di.append(list(map(str,input().split())))
while(True):
    if k<L:
        if time==int(di[k][0]):
            if di[k][1]=='L':
                ind= (ind-1)%4
            else:
                ind= (ind+1)%4
            k+=1
    x+=d_x[ind]
    y+=d_y[ind]    
    time+=1
    if 0<=x<N and 0<=y<N and maap[y][x]!=2:
        snake.append([x,y])
        if maap[y][x]==0:
            maap[snake[0][1]][snake[0][0]]=0
            del snake[0]
        maap[y][x]=2
    else:
        break    
print(time)
