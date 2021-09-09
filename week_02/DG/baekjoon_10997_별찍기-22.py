N=int(input())
x= ['*****','*','* ***']
y= ['*   *','*****']
if N==1:
    print('*')
else:

    for i in range(1,N-1):
        x[0]='* '+x[0]+'**'
        x[1]='* *'+' '*(4*i+1)+'*'
        for j in range(2,len(x)):
            x[j]='* '+x[j]+' *'
        x.insert(0,'*')
        x.insert(0,'*'*(4*i+5))
    x.append('*'+' *'*2*(N-1))
    x.append('*'+' *'*2*(N-1))
    for i in range(1, N-1):
        for j in range(len(y)):
            y[j]='* '+y[j]+' *'
        y.append('*'+' '*(4*i+3)+'*')
        y.append('*'*(4*i+5))
        # print(y)
    
    
    
    
    for i in range(len(x)):
        print(x[i])
    for i in range(len(y)):
        print(y[i])
