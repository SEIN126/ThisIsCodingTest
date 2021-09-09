#시간초과 날 때 입력 바꾸기#######
# import sys
# input = sys.stdin.readline
#################################


# print("|\\_/|")
# print("|q p|   /}")
# print("( 0 )\"\"\"\\")
# print('|"^"`    |')
# print("||_/=\\\\__|")


# import sys
# a, b, c = map(int, sys.stdin.readline().split())
# print((a+b)%c)
# print(((a%c)+(b%c))%c)
# print((a*b)%c)
# print(((a%c)*(b%c))%c)


# import sys
# a = int(sys.stdin.readline())
# b = sys.stdin.readline()

# a*(b%10)
# a*(b%100)

# import sys
# a, b = map(int,sys.stdin.readline().split())

# if (a>b):
#     print('>')
# if (a<b):
#     print('<')
# if (a==b):
#     print('==')
    
    
# import sys
# a = int(sys.stdin.readline())

# if (a>=90):
#     print('A')
# elif (a>=80):
#     print('B')
# elif (a>=70):
#     print('C')
# elif (a>=60):
#     print('D')
# else:
#     print('F')
    
    
# import sys
# a = int(sys.stdin.readline())

# if ((a/4)==(a//4)and(a/100)!=(a//100))or(a/400)==(a//400):
#     print(1)
# else:
#     print(0)
    
    
    
    
# # H, M = map(int,input().split())
# import sys
# H, M = 

# x=H*60+M-45
# if x<0:
#     x=x+1440
# a,b = x//60, x%60
# print(a,b)


# import sys
# T = int(input())
# for i in range(T, 0, -1):
#     print(i)

# import sys
# T = int(input())
# for i in range(1, T+1):
#     a,b = map(int,sys.stdin.readline().split())
#     print("Case #%d: %d + %d = %d"%(i,a,b,a+b))
    
# N = int(input())
# for i in range(1,N+1):
#     print(("*"*i).rjust(N))
    
# import sys
# N, X = map(int,input().split())
# a = list(map(int,input().split()))
# for i in range(len(a)):
#     if a[i]<X:
#         print(a[i], end='')
        

# while(True):
#     try:
#         A, B = map(int,input().split())
#         print(A+B)
#     except:
#         break
    
# NN = int(input())
# i=0
# N = NN
# while(True):
#     i+=1
#     if N<10:     
#         x = 11*N
#         if(x==NN):
#             break
#         else:
#             N=x
#     else:
        
#         x = (N%10+(N//10))%10+(N%10)*10
#         if(x==NN):
#             break
#         else:
#             N = x
# print(i)



# N = int(input())
# A = list(map(int,input().split()))
# print(min(A),end=' ')
# print(max(A))



# N = int(input())
# for i in range(2,10):
#     x = int(input())
#     print(i)
#     if x>N:
#         N, itr = x, i
# print(N)
# print(itr)


# a = int(input())
# b = int(input())
# c = int(input())
# x=a*b*c
# x = [int(i) for i in str(x)]
# for i in range(10):
#     print(x.count(i))

# x=set([int(input())%42 for i in range(10)])
# print(len(x))

# import sys
# N = int(input())
# A = list(map(int,sys.stdin.readline().split()))
# M = max(A)
# print( sum(A)/N*100/M)
# import sys
# N = int(input())

# for i in range(N):
#     score=0
#     add_score=1
#     A = list(input())
#     for j in range(len(A)):
#         if j==0:
#             if A[j]=='O':
#                 score+=add_score
#                 add_score+=1
#         else:
#             if A[j]=='O':
#                 score+=add_score
#                 add_score+=1
#             else:
#                 add_score=1
#     print(score)


# v=6
# print(~v) #앞 부호 바꾸고
# print(-~v)
# print(v*-~v)
# print(v*-~v)
# print(v*-~v//2)


# exec("print(sum(v*-~v//2for v in map(len,input().split('X'))));"*int(input()))
# sum(v*-~v//2for v in map(len,input().split('X')))

# X = list(map(len,input().split('X')))
# print(X)



# import time
# itr=1000000000
# v= 100
# t = time.time()
# for i in range(itr):
#     100*-~(100)
# print(time.time()-t)
# t = time.time()
# for j in range(itr):
#     100*(100+1)
# print(time.time()-t)

# N = int(input())
# for i in range(N):
#     x = list(map(int, input().split()))
#     avg = sum(x[1:])/x[0]
#     k = 0
#     for i in x[1:]:
#         if i>avg:
#             k +=1
#     print("%3.3f%%"%(k/x[0]*100))


# while (True):
#     a = list(map(int,input().split()))
#     a = [i**2 for i in a]
#     M = max(a)
#     if M==0:
#         break
#     elif 2*M==sum(a):
#         print("right")
#     else:
#         print("wrong")

'아리스토텔레스의 체'
# n = int(input())
# # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
# sieve = [True] * n

# # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
# m = int(n ** 0.5)
# for i in range(2, m + 1):
#     if sieve[i] == True:           # i가 소수인 경우
#         for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
#             sieve[j] = False
# # 소수 목록 산출
# print( [i for i in range(2, n) if sieve[i] == True])

'2581'
# M = int(input())
# N = int(input())
# s=[]
# for i in range(M,N+1):
#     if i!=1:
#         for j in range(2,i+1):
#             if j==i:
#                 s.append(i)
#             if i%j==0:
#                 break
# if s==[]:
#     print(-1)
# else:
#     print(sum(s))
#     print(min(s))

'11653'
# n = int(input())
# m = int(n**0.5)
# x=2
# if n==1:
#     t=0
# if n!=1:
#     t=1
# while(t):
#     m = int(n**0.5)
#     if x>=m+1:
#         print(n)
#         break
#     for i in range(x, m+1):
#         if n%i!=0:
#             x+=1
#         if n%i==0:
#             print(i)
#             n=int(n/i)
#             break
#         if i==m and n!=1:
#             print(n)
#             t=0
#         if i==m:
#             t=0

'1929'
# M, n = map(int,input().split())
# n = n+1
# sieve = [True] * n
# sieve[0], sieve[1] = False, False
# m = int(n ** 0.5)
# for i in range(2, m + 1):
#     if sieve[i] == True:
#         for j in range(i+i, n, i):
#             sieve[j] = False
# x = [i for i in range(M, n) if sieve[i] == True ]
# for i in range(len(x)):
#     print(x[i])



'4948'
# num = int(input())
# n = 10000
# sieve = [True] * n
# sieve[0], sieve[1] = False, False
# m = int(n ** 0.5)
# for i in range(2, m + 1):
#     if sieve[i] == True:
#         for j in range(i+i, n, i):
#             sieve[j] = False
# x = [i for i in range(2, n) if sieve[i] == True ]

# for i in range(num):
#     k = int(input())
#     det= int(k/2)
    
#     while(1):
#         if det in x:
            
#             if (k-det) in x:
#                 a= det
#                 b= k-det
#                 break
#             else:
#                 det-=1
#         else:
#             det-=1
#     print(a,b)

'6588 yet'

# n = 1000000
# sieve = [True] * n
# sieve[0], sieve[1] = False, False
# m = int(n ** 0.5)
# for i in range(2, m + 1):
#     if sieve[i] == True:
#         for j in range(i+i, n, i):
#             sieve[j] = False
# x = [i for i in range(3, n) if sieve[i] == True ]

# while(1):
#     k = int(input())
#     if k==0:
#         break
#     det= 3
#     while(1):
#         if k<2*det:
#             print("Goldbach's conjectures is wrong.")
#         if det in x and (k-det) in x:
    
#                 a= det
#                 b= k-det
#                 print('%d = %d + %d'%(k , a, b))
#                 break
#         else:
#                 det+=2


'1712'
# a, b, c = map(int,input().split())

# if b>=c:
#     print(-1)
# else:print(int(a/(c-b))+1)

'2292'

# x = int(input())
# n=0
# while(1):
    
#     if x <= 3*n*(n+1)+1:
#         print(n+1)
#         break
#     else: n+=1
'1193'
# x = int(input())
# n=1
# while(1):
#     if x<=n*(n+1)/2:
#         m=n*(n+1)/2-x
#         if n%2==0:
#             print('%d/%d'%((n-m),(1+m)))
#             break
#         else: 
#             print('%d/%d'%((1+m),(n-m)))
#             break
#     else:n+=1
        
    
'2869'
# a, b, v = map(int,input().split())

# if (v-a)%(a-b)==0:
#     print((v-a)//(a-b)+1)
# else:
#     print((v-a)//(a-b)+2)

'1085'
# x, y, w, h = map(int,input().split())

# print(min(x, y, w-x, h-y))

'3009'
# a,b = map(int,input().split())
# x = [a]
# y = [b]
# for i in range(2):
#     c, d = map(int,input().split())
#     if (c in x):
#         x.remove(c)
#     else:
#         x.append(c)
#     if (d in y):
#         y.remove(d)
#     else:
#         y.append(d)
# print(x[0],y[0])

'3053'
# import math

# r = int(input())
# s = r**2
# print(math.pi*s)
# print(2*s)

'1002'
# T = int(input())


# for i in range(T):
#     x1, y1, r1, x2, y2, r2 = map(int,input().split())
#     d = ((x1-x2)**2+(y1-y2)**2)**0.5
#     R = max(r1, r2)
#     r = min(r1, r2)
#     if x1==x2 and y1==y2 and r1==r2:
#         print(-1)
#     elif (d>R and (d>(r1+r2))) or(d<R and (d+r)<R):
#         print(0)
#     elif (d>R and d==(r1+r2))or(d<R and (d+r)==R):
#         print(1)
#     elif (d>R and d<(r1+r2))or(d<R and (d+r)>R) or d==R:
#         print(2)

'10250' 
# T = int(input())
# for i in range(T):
#     H,W,N = map(int,input().split()) #H,W 호텔, N번째 손님
#     assert H*W>=N
#     a = N%H
#     b = N//H+1
#     if a==0:
#         a=H
#         b-=1
#     print(a*100+b)
'2775'
# a = list(range(1,15))
# for j in range(1,15):
#     for i in range(14):
#         if i==0:
#             a.append(1)
#         else:
#             a.append(a[14*j+i-1]+a[14*j+i-14])4
# T = int(input())
# for i in range(T):
#     k = int(input())
#     n = int(input())
#     print(a[14*k+n-1])

'2839'
# n = int(input())
# a = n%5
# x = 0
# while(1):
#     if a%3==0:
#         print(n//5-x+a//3)
#         break
#     else:
#         a+=5
#         if a>n:
#             print(-1)
#             break
#         x+=1    

'10757'
# a,b = map(int,input().split())

# x = a//10
# y = b//10
# xx = a%10
# yy = b%10
# c = x+y
# d = xx+yy
# if (xx+yy)>=10:
#     print('%d%d'%(c+1,d%10))
# else:
#     print('%d%d'%(c,d))

'1011'
# T = int(input())

# for i in range(T):
#     a,b = map(int,input().split())
#     n = b-a
#     i=1
#     x=0
#     while(1):
#         if n<=i:
#             x+=1
#             break
#         if n<=2*i:
#             x+=2
#             break
            
#         if n>2*i:
#             x+=2
#             n-=2*i
            
#         i+=1
#     print(x)

# a= int(input())
# b= int(input())
# print(a+b)

# a,b = map(int,input().split())
# print(a*b-1)


# from pytz import timezone
# from datetime import datetime
# print(datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S'))
'10699'
# import datetime
# print(str(datetime.datetime.now())[:10])


# print('61')
# print('dgleee')

'2525'
# h, m = map(int,input().split())
# c = int(input())
# if m+c%60>=60:
#     m=m+c%60-60
#     h=h+c//60+1
#     if h>=24:
#         h-=24
# else:
#     m=m+c%60
#     h=h+c//60
#     if h>=24:
#         h-=24
# print(h,m)

'2530'
# h, m, s = map(int,input().split())
# c = int(input())
# x = 3600*h+60*m+s+c
# if x>=86400:
#     x= x%86400
# h=x//3600
# x=x%3600
# m=(x)//60
# s=(x)%60
# print(h,m,s)

'2914'
# A, I = map(int,input().split())
# print(A*(I-1)+1)

'5355'

# T=int(input())

# for i in range(T):
#     A = list(map(str, input().split()))
#     A[0]= float(A[0])
#     for i in range(1,len(A)):
#         if A[i]=='@':
#             A[0]=A[0]*3
#         if A[i]=='%':
#             A[0]=A[0]+5
#         if A[i]=='#':
#             A[0]=A[0]-7
            
#     print('%.2f'%A[0])


'2675'

# T=int(input())

# for i in range(T):
#     a, b = map(str,input().split())
#     a = int(a)
#     x = ''
#     for i in range(len(b)):
#       x+=a*b[i]
#     print(x)
    
# a = int(input())
# b = str(input())
# c = int(input())
# if b=='+':
#     x=a+c
# if b=='*':
#     x=a*c
# print(x)

'10817번'
# a = list(map(int,input().split()))
# a.sort()
# print(a[1])

'1789'
# s = int(input())
# n=1
# while(1):
#     if s<n*(n+1)/2:
#         print(n-1)
#         break
#     n+=1
    
'10039'

# a = int(input())
# if a<40:
#     a=40
# b = int(input())
# if b<40:
#     b=40
# c = int(input())
# if c<40:
#     c=40
# d = int(input())
# if d<40:
#     d=40
# e = int(input())
# if e<40:
#     e=40
# print(int((a+b+c+d+e)/5))


'2824'
# import copy
# N = int(input())
# A = list(map(int,input().split()))
# AA = 1
# BB = 1
# for i in range(N):
#     AA*=A[i]
# N = int(input())
# B = list(map(int,input().split()))
# for i in range(N):
#     BB*=B[i]
# a = AA
# b = BB
# while(1):
#     x = b
#     y = a%b
#     if y==0:
#         print(str(x)[-9:])
#         break
#     a = copy.deepcopy(x)
#     b = y


# x=11123456789
# print(str(x)[-9:])


'a,b의 최소공배수'
# import copy
# a = int(input())
# b = int(input())
# while(1):
#     x = b
#     y = a%b
#     if y==0:
#         print(str(x)[-9:])
#         break
#     a = copy.deepcopy(x)
#     b = y
    

'2609번'
# import copy
# c, d = map(int,input().split())

# a = copy.deepcopy(c)
# b = copy.deepcopy(d)
# while(1):
#     x = b
#     y = a%b
#     if y==0:
#         print(str(x)[-9:])
#         print(c*d/x)
#         break
#     a = copy.deepcopy(x)
#     b = y
    
'1850'
# import copy
# a, b = map(int,input().split())

# while(1):
#     x = b
#     y = a%b
#     if y==0:
#         print(x*'1')
        
#         break
#     a = copy.deepcopy(x)
#     b = y

'1934'
# import copy
# T = int(input())
# for i in range(T):
#     c, d = map(int,input().split())
    
#     a = copy.deepcopy(c)
#     b = copy.deepcopy(d)
#     while(1):
#         x = b
#         y = a%b
#         if y==0:
#             # print(str(x)[-9:])
#             print(int(c*d/x))
#             break
#         a = copy.deepcopy(x)
#         b = y
    
'5063'
# N = int(input())
# for i in range(N):
#     r,e,c = map(int,input().split())
#     x = e-c-r
#     if x>0: print('advertise')
#     elif x<0: print('do not advertise')
#     else: print('does not matter')


'2480'
# a = list( map(int,input().split()))
# x = set(a)
# if len(x)==1:
#     print(10000+a[0]*1000)
# if len(x)==2:
#     print((sum(a)-sum(x))*100+1000)
# if len(x)==3:
#     print(max(a)*100)


'4101번'
# while(1):
#     x ,y = map(int,input().split())
#     if x==0 and y==0:break
#     if x>y:print('Yes')
#     else:print('No')

'10156'
# K,N,M = map(int,input().split())
# x = K*N-M
# if x>0:print(x)
# else:print(0)

'2476'
# N = int(input())
# k = 0
# for i in range(N):

#     a = list( map(int,input().split()))
#     x = set(a)
#     if len(x)==1:
#         t = 10000+a[0]*1000
#         if t>k:
#             k=t
#     if len(x)==2:
#         t = (sum(a)-sum(x))*100+1000
#         if t>k:
#             k=t
#     if len(x)==3:
#         t = max(a)*100
#         if t>k:
#             k=t
# print(k)

'2754'
# dic = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7
# ,'B+': 3.3, 'B0': 3.0, 'B-': 2.7
# ,'C+': 2.3, 'C0': 2.0, 'C-': 1.7
# ,'D+': 1.3, 'D0': 1.0, 'D-': 0.7
# ,'F': 0.0}
# print(dic[str(input())])

'7567'
# x = str(input())
# k = 10
# for i in range(1,len(x)):
#     if x[i-1]==x[i]:k+=5
#     if x[i-1]!=x[i]:k+=10
# print(k)

'10102'
# V = int(input())
# x = str(input())
# k = x.count('A')
# if k==V-k:print('Tie')
# elif k>V-k:print('A')
# else:print('B')

'10886'
# N = int(input())
# x = 0
# for i in range(N):
#     x += int(input())
# if x/N>0.5:
#     print('Junhee is cute!')
# else:
#     print('Junhee is not cute!')

'10988'
# x = str(input())
# s = x[-1::-1]
# if x==s:
#     print(1)
# else:
#     print(0)

'5086'
# while(1):
#     a,b = map(int,input().split())
#     if a==0 and b==0:
#         break
#     if a%b==0:
#         print('multiple')  
#     elif b%a==0:
#         print('factor')
#     else:
#         print('neither')

'5717'
# while(1):
#     M,F = map(int,input().split())
#     if M+F==0:
#         break
#     print(M+F)

'9610'
# n = int(input())
# x = [0]*5
# for i in range(n):
#     a, b= map(int,input().split())
#     if a>0 and b>0:
#         x[0]+=1
#     elif a<0 and b>0:
#         x[1]+=1
#     elif a<0 and b<0:
#         x[2]+=1
#     elif a>0 and b<0:
#         x[3]+=1
#     else:
#         x[4]+=1
# for i in range(5):
#     if i<4:
#         print("Q%d: %d"%(i+1,x[i]))
#     else:
#         print("AXIS: %d"%x[i])

'9506'
# while(1):
    
#     n = int(input())
#     if n==-1:
#         break
#     x=[1]
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             x.append(i)
#             x.append(int(n/i))
#     x.sort()
#     if sum(x)!=n:
#         print("%d is NOT perfect."%n)
#     else:
#         s = str('%d = '%sum(x))
#         for i in range(len(x)-1):
#             s+='%d + '%x[i]
#         s+='%d'%x[-1]
#         print(s)
    
'10162'

# T = int(input())
# if T%10!=0:
#     print(-1)
# else:
#     T=int(T/10)
#     A=T//30
#     T=T%30
#     B=T//6
#     C=T%6
#     print(A,B,C)

'10214'
# T= int(input())
# for i in range(T):
#     y=0
#     k=0
#     for i in range(9):
#         a, b= map(int,input().split())
#         y+=a
#         k+=b
#     if y==k:
#         print('Draw')
#     if y>k:
#         print('Yonsei')
#     else:
#         print('Korea')

'11557'
'dictionary'
'get key with maximum values'
'min(d, key=d.get) or max(d, key=d.get)' 
# T = int(input())
# for i in range(T):
#     N = int(input())
#     d = {}
#     for i in range(N):
#         S,L = map(str,input().split())
#         d[S]=int(L)
#     print(max(d, key=d.get))


'10103'

# n = int(input())
# x = 100
# y = 100
# for i in range(n):
#     a,b = map(int,input().split())
#     if a>b:
#         y-=a
#     if a<b:
#         x-=b
# print('%d\n%d'%(x,y))

'1463'
'다이나믹 프로그래밍?'
'적은 수부터 각 경우를 다 구하고 점화식으로 조건을 찾음'
'x[i]= min(x[i-1]+1, x[i//3]+1, x[i//2]+1)'
# n = int(input())
# x = [0 for i in range(n+1)]
# for i in range(2, n+1):
#     x[i]=x[i-1]+1
#     if i%3==0 and x[i]>x[i//3]:
#         x[i]=x[i//3]+1
#     if i%2==0 and x[i]>x[i//2]:
#         x[i]=x[i//2]+1
# print(x[n])

'6588'
# def getPrimaryNum_Eratos(N):
#     nums = [True] * (N + 1)
#     for i in range(2, len(nums) // 2 + 1):
#         if nums[i] == True:
#             for j in range(i+i, N, i):
#                 nums[j] = False
#     return [[i for i in range(2, N) if nums[i] == True], nums]
# primary_nums = getPrimaryNum_Eratos(1000000)[0]
# primary_bools = getPrimaryNum_Eratos(1000000)[1]
# while(True):
#     N = int(input())
#     if N == 0:
#         break
    
#     for i in range(N // 2):
#         if primary_bools[N-primary_nums[i]] == True:
#             print("{} = {} + {}".format(N, primary_nums[i], N-primary_nums[i]))
#             break

'16637'
# N=int(input())
# x = str(input())
# oper = [str(x[i]) for i in range(1,N,2)]
# num = [str(x[i]) for i in range(0,N+1,2)]
# i=1
# r=num[0]
# while(1):
#     if i==len(num)-1:
#         r = eval(str(r) + oper[i-1] + num[i])
#         break
#     elif len(num)-1<i:
#         break
#     elif i==len(num)-2:
#         x = eval(str(r) + oper[i-1] + num[i])
#         x = eval(str(x) + oper[i] + num[i+1])
        
#         y = eval(num[i] + oper[i] + num[i+1])
#         y = eval(str(r) + oper[i-1] + str(y))
#         if x>y:
#             r = eval(str(r) + oper[i-1] + num[i])
#             i+=1
#         if x<=y:
#             r = y
#             i+=2
#     else:
#         x = eval(str(r) + oper[i-1] + num[i])
#         x = eval(str(x) + oper[i] + num[i+1])
#         x = eval(str(x) + oper[i+1] + num[i+2])
        
#         y = eval(num[i] + oper[i] + num[i+1])
#         y = eval(str(r) + oper[i-1] + str(y))
#         y = eval(str(y) + oper[i+1] + num[i+2])
        
#         z = eval(str(r) + oper[i-1] + num[i])
#         z1 = eval(num[i+1] + oper[i+1] + num[i+2])
#         z = eval(str(z) + oper[i] + str(z1))
#         if z>=y and z>=x:
#             r = eval(str(r) + oper[i-1] + num[i])
#             i+=1
#         elif y>=x and y>z:
#             yy = eval(num[i] + oper[i] + num[i+1])
#             r = eval(str(r) + oper[i-1] + str(yy))
#             i+=2
#         elif x>y and x>z:
#             r = eval(str(r) + oper[i-1] + num[i])
#             i+=1
# if -2**31<r<2**31:print(r)

'15596'

# def solve(a):return sum(a)

'4673'
# def d(n):
#     x=n
#     for i in str(n):
#         x+=int(i)
#     return x
# n=1
# while(1):
#     n = d(n)
    
#     if n>=10000:
#         break
#     print(n)
#     if n>100:
#         break

'16600'
# n = int(input())
# print(4*(n**0.5))

'9501'
# T = int(input())

# for i in range(T):
#     N, D = map(int,input().split())
#     cc=0
#     for i in range(N):
#         v, f, c = map(int,input().split()) # m/s, L, L/s
#         if D<=v/c*f: # 연비(거리(m)/연료량(L))*연료량(L) = 거리
#             cc+=1
#     print(cc)
    
'10809'

# N = int(input())
# if N<100:
#     print(N)
# else:
#     x = list(range(1, 100))
#     for i in range(100, N+1):
#         # print(i)
#         s = str(i)
#         if int(s[0])-int(s[1]) == int(s[1])-int(s[2]):
#             x.append(int(s))
#     print(len(x))

'10872'
# def fucktorial(n):
    
#     if n == 0 or n == 1:
#         return 1
#     return n * fucktorial(n - 1)
# x = int(input())
# print(fucktorial(x))

'10870'
# def fuckbonichi(n):
#     if n==0:
#         return 0    
#     elif n==1:
#         return 1
#     else:
#         return fuckbonichi(n-2)+fuckbonichi(n-1)
# n = int(input())
# print(fuckbonichi(n))


'2447번'

# n = int(input())
# star = [list(range(n)) for i in range(n)]

# def draw_star(n) :
#     global star
    
#     if n==3:
#         star[0][:3] = star[2][:3] = ['*'] *3
#         star[1][:3] = ['*', ' ', '*']
#         return
#     x = n//3
#     draw_star(n//3)
#     for i in range(3):
#         for j in range(3):
#             for k in range(x):
#                 if (i == 0 and j == 0):
#                     continue
#                 elif i == 1 and j == 1:
#                     star[x*i+k][x*j:x*j+x] = [' ']*x
#                 else:
#                     star[x*i+k][x*j:x*j+x] = star[k][:x]
                
        
# draw_star(n)
    
# for i in range(n):
#     for j in range(n):
#         print(star[i][j],end='')
#     print()
    
    



'11729번'


# def hanoi(n):
#     global x
#     if n==1:
#         x = [1,3]
#         return
#     hanoi(n-1)
#     d = x[:]
#     e = x[:]
#     for i in range(len(d)):
#         if d[i]==2:
#             d[i]=3
#         elif d[i]==3:
#             d[i]=2
#     for j in range(len(e)):
#         if e[j]==1:
#             e[j] = 2
#         elif e[j]==2:
#             e[j]=1
#     x=d[:]
#     x.append(1)
#     x.append(3)
#     for i in range(len(e)):
#         x.append(e[i])  
# n = int(input())
# hanoi(n)
# length = int(len(x)/2)
# print(length)

# for i in range(len(x)):
#     print(x[i], end=' ')
#     if i%2==1:
#         print()


# n, m = map(int,input().split())

# x = list(map(int,input().split()))

'11720'


# N = input().upper()
# x = list(set(N))
# cnt_list = []
# for i in x:
#     cnt = N.count(i)
#     cnt_list.append(cnt)

# if cnt_list.count(max(cnt_list))>1:
#     print('?')
# else:
#     print(x[cnt_list.index(max(cnt_list))])

'1920'

# N = int(input())
# A = set((map(int, input().split())))
# M = int(input())
# x = list(map(int, input().split()))

# for i in x:
#     if i in A:print(1)
#     else:print(0)


# print(ord(input()))

# import sys
# N = int(sys.stdin.readline())
# x = []
# for i in range(N):
#     x.append(int(sys.stdin.readline()))
# x.sort()

# for i in range(N):
#     print(x[i])


# import sys
# n=int(sys.stdin.readline())
# num=[]
# for _ in range(n):
#     x = int(sys.stdin.readline())
#     num.append(x)
# for i in sorted(num):
#     print(i)
    


# N = int(input())
# x = []
# for i in range(N):
#     x.append(int(input()))
# x.sort()

# for i in range(N):
#     print(x[i])
'1003'
# t = int(input())
# for i in range(t):
#     n = int(input())
#     count = [[1,0],[0,1]]    
#     if n>1:
#         for i in range(n-1):
#             count[0].append(count[0][i]+count[0][i+1])
#             count[1].append(count[1][i]+count[1][i+1])
#         print(count[0][n], count[1][n])
#     else:
#         print(count[0][n], count[1][n])
'1004'
# t = int(input())
# for i in range(t):
#     x1,y1,x2,y2=map(int, input().split())
#     n = int(input())
#     s =0
#     for i in range(n):
#         x,y,r = map(int,input().split())
#         d1 = (x-x1)**2+(y-y1)**2
#         d2 = (x-x2)**2+(y-y2)**2
#         if (d1>(r**2))^(d2>(r**2)):
#             s+=1
#     print(s)

'nC3 combination'
# for i in range(int(n*(n-1)*(n-2)/6)):
#     y.append([x[a],x[b],x[c]])
#     c=c+1
#     if c==n:
#         b+=1
#         if b==n-1:
#             a+=1
#             b=a+1
#             c=b+1
#         else:
#             c=b+1

'2798'

# n, m = map(int,input().split())
# x = list(map(int,input().split()))

# y = []
# a=0
# b=1
# c=2
# t = int(n*(n-1)*(n-2)/6)
# for i in range(t):
#     if x[a]+x[b]+x[c]-m<=0:
#         y.append(x[a]+x[b]+x[c]-m)
#     c=c+1
#     if c==n:
#         b+=1
#         if b==n-1:
#             a+=1
#             b=a+1
#             c=b+1
#         else:
#             c=b+1
# print(y[y.index(max(y))]+m)






'공통문제'
# N = list(map(int,list(str(input()))))
# num = int(len(N)/2)
# if sum(N[:num]) == sum(N[num:]): print("LUCKY")
# else : print("READY")


'15686'
# def combinations(iterable, r):
#     pool = tuple(iterable)
#     n = len(pool)
#     if r > n:
#         return
#     indices = list(range(r))
#     yield tuple(pool[i] for i in indices)
#     while True:
#         for i in reversed(range(r)):
#             if indices[i] != i + n - r:
#                 break
#         else:
#             return
#         indices[i] += 1
#         for j in range(i+1, r):
#             indices[j] = indices[j-1] + 1
#         yield tuple(pool[i] for i in indices)
        
# N, M = map(int,input().split())
# mapp = []
# home = []
# chic = []
# dist = []
# a=[]
# vil_dist = []
# for i in range(N):
#     mapp.append(list(map(int,input().split())))
#     home.extend([[i, x] for x, value in enumerate(mapp[i]) if value == 1])
#     chic.extend([[i, x] for x, value in enumerate(mapp[i]) if value == 2])
# for i in range(len(home)):
#     dist.append([abs(home[i][0]-chic[j][0])+abs(home[i][1]-chic[j][1]) for j in range(len(chic))])
# for i in range(len(dist)):
#     a.append(list(combinations(dist[:][i],M)))
# for i in range(len(a[0])):
#     x=0
#     for j in range(len(a)):
#         x+=min(a[j][i])
#     vil_dist.append(x)
# print(min(vil_dist))

'1094 막대기'

# x = int(input())
# if x==64:print(1)
# else:
#     s=64
#     i=0
#     n=1
#     while(s>x):
#        i+=1
#        new=2**(6-i)
#        if s-new>=x:s-=new
#        else:n+=1
#     print(n)
  
'10809 알파벳 찾기'         
# x = str(input())
# xset =set(x)
# alp = [['a', 'b', 'c', 'd', 'e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']]
# alp.append([-1]*26)

# for _,j in enumerate(xset):

#     alp[1][alp[0].index(j)]=min([x for x, value in enumerate(x) if value==j])
# for i in range(len(alp[1])):
#     print(alp[1][i],end=' ')
'2743 단어 길이 재기'
# print(len(str(input())))

'1152 단어의 개수'

# x = str(input())
# y = 1
# if x[0]==' ':
#     y-=1
# if x[-1]==' ':
#     y-=1
# for i in range(len(x)):
#     if x[i]==' ':
#         y += 1
# print(y)

'2440 별찍기-3'
# n = int(input())
# for i in range(n) : print('*'*(n-i))
    
'2441 별찍기-4'
# n = int(input())
# for i in range(n) :
#     print(' '*i,end='')
#     print('*'*(n-i))

'2908'
# n,m = map(str,input().split())
# if int(n[::-1])> int(m[::-1]):print(int(n[::-1]))
# else:print(int(m[::-1]))

'1924'
# a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# x, y = map(int, input().split())
# day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
# print(day[(sum(a[:x-1])+y-1)%7])
'11718 EOF error를 해결하려면 ctrl+d를 했을 때 종료될 수 있또록 except 사용'
# while True:
#     try:
#         s = input()
#         print(s)
#     except:
#         break
'5622'
# alp = [['A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']]
# alp.append([3]*3+[4]*3+[5]*3+[6]*3+[7]*3+[8]*4+[9]*3+[10]*4)

# x = str(input())
# s = 0
# for i in range(len(x)):
#     s+=alp[1][alp[0].index(x[i])]
# print(s)
'1316'
# s=0
# for i in range(int(input())):
#     x= str(input())
#     x_set = set(x)
#     a=0
#     for _, i in enumerate(x_set):
#         k = [a for a, value in enumerate(x) if value==i]
#         if len(k)!=(max(k)-min(k)+1):
#             a=1
#             break
#     if a==0:s+=1
# print(s)
'2941'
# x = str(input())
# a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# for i in a:
#     x = x.replace(i,"A")
# print(len(x))
'2920'

# x=str(input())
# if x=='1 2 3 4 5 6 7 8':
#     print('ascending')
# elif x=='8 7 6 5 4 3 2 1':
#     print('descending')
# else:
#     print('mixed')
'11721'
# x =  str(input())
# for i in range(len(x)//10+1):print(x[10*i:10*(i+1)])

'11719'

# while True:
#     try:
#         s = input()
#         print(s)
#     except:
#         break

'2446'

# N=int(input())
# for i in range(N):
#     print(' '*i,end='')
#     print('*'*(2*N-1-2*i))
# for i in range(N-2,-1,-1):
#     print(' '*i,end='')
#     print('*'*(2*N-1-2*i))

'2442'

# N=int(input())
# for i in range(N-1,-1,-1):
#     print(' '*i,end='')
#     print('*'*(2*N-1-2*i))
    
'10773 제로'
# import sys
# input = sys.stdin.readline



# K = int(input())
# s = []
# for i in range(K):
#     x = int(input())
#     if x==0:
#         del s[-1]
#     else:
#         s.append(x)
# print(sum(s))


    
'2475'
# import sys
# input = sys.stdin.readline
# # x=[0, 4, 2, 5, 6]
# x= list(map(int,input().split()))
# s = 0
# for i in range(len(x)):
#     s+=x[i]**2
# print(s%10)

'2523  별 찍기-13'
# import sys
# input = sys.stdin.readline
# x=int(input())
# for i in range(1,x+1):
#     print('*'*i)
# for i in range(x-1,0,-1):
#     print('*'*i)

'2445 별 찍기-8'
# import sys
# input = sys.stdin.readline
# x=int(input())
# for i in range(1,x+1):
#     print('*'*i+' '*2*(x-i)+'*'*i)
# for i in range(x-1,0,-1):
#     print('*'*i+' '*2*(x-i)+'*'*i)
'2443 별 찍기-6'
# import sys
# input = sys.stdin.readline
# x=int(input())
# for i in range(x):
#     print(' '*i+'*'*(2*(x-i)-1))
'2444 별 찍기-7'
# import sys
# input = sys.stdin.readline
# x=int(input())
# for i in range(1,x+1):
#     print(' '*(x-i)+'*'*(2*i-1))
# for i in range(x-1,0,-1):
#     print(' '*(x-i)+'*'*(2*i-1))

'2448 별 찍기-11'
# import math

# N=int(input())
# x=[' '*2+'*'+' '*2,' '+'*'+' '+'*'+' ', '*'*5]
# def new_x(x,k):
#     for i in range(len(x)):
#         x.append(x[i]+' '+x[i])
#         x[i]=' '*(3*2**k)+x[i]+' '*(3*2**k)
#     return x

# for k in range(int(math.log2(N//3))):
#     x=new_x(x,k)
# for i in range(len(x)):
#     print(x[i])

'2522 별 찍기-12'
# N=int(input())
# for i in range(N):
#     print(' '*(N-i-1)+'*'*(i+1))
# for i in range(N-2,-1,-1):
#     print(' '*(N-i-1)+'*'*(i+1))
'10990 별 찍기-15'
# N=int(input())
# print(' '*(N-1)+'*')
# for i in range(1,N):
#     print(' '*(N-i-1)+'*'+' '*(2*i-1)+'*')
'10991 별 찍기-16'
# N=int(input())
# print(' '*(N-1)+'*')
# for i in range(1,N):
#     print(' '*(N-i-1)+'*'+' *'*i)

'10992 별 찍기-17'
# N=int(input())
# print(' '*(N-1)+'*')
# for i in range(1,N-1):
#     print(' '*(N-i-1)+'*'+' '*(2*i-1)+'*')
# if N!=1:
#     print('*'*(2*N-1))

'10993 별 찍기-18'

# N=int(input())
# # N=4
# # x=['*****',' *** ','  *  ']
# x=['*']
# for i in range(N-1):

#     if i%2==1:
#         l=len(x)
#         x.insert(0,(' '*l*2+'*'))
#         for i in range(1, l):
#             x.insert(i,' '*(2*l-i)+'*'+' '*(2*i-1)+'*')
#         for i in range(l,2*l):
#             x[i]=' '*(2*l-i)+'*'+' '*(i-l)+x[i]+' '*2*(i-l)+'*'
#         x.append('*'*(4*l+1))

#     else:
#         l=len(x)
#         x.insert(0,'*'*(4*l+1))
#         for i in range(1,l+1):
#             x[i]=' '*(i)+'*'+' '*(l-i)+x[i]+' '*2*(l-i)+'*'
#         for i in range(l, 2*l-1):
#             x.append(' '*(i+1)+'*'+' '*(4*l-2*i-3)+'*')
#         x.append(' '*l*2+'*')


# for i in range(len(x)):
#     print(x[i])

'10994 별찍기 -19'
# N=int(input())
# x=['*']
# for i in range(N-1):
#     leng= len(x)
#     for j in range(leng):
#         x[j]= '* '+x[j]+' *'
#     x.insert(0,'*'+' '*(4*(i+1)-1)+'*')
#     x.insert(0,'*'*(4*(i+1)+1))
#     x.append('*'+' '*(4*(i+1)-1)+'*')
#     x.append('*'*(4*(i+1)+1))
# for i in range(len(x)):
#     print(x[i])
    
'10995 별 찍기-20'
# N = int(input())
# for i in range(N):
#     if i%2==1:
#         print(' ',end='')
#     print('*'+' *'*(N-1))

'10996 별 찍기-21'
# N= int(input())
# for i in range(N):
#     print('*'+' *'*((N-1)//2)+'\n'*(N!=1)+' *'*(N//2))

'13015 별 찍기-23'
# N=int(input())
# print('*'*N+' '*(2*N-3)+'*'*N)
# for i in range(1,N-1):
#     print(' '*(i-1),'*'+' '*(N-2)+'*'+' '*(2*N-3-2*i)+'*'+' '*(N-2)+'*')
# print(' '*(N-1)+'*'+' '*(N-2)+'*'+' '*(N-2)+'*')
# for i in range(N-2,0,-1):
#     print(' '*(i-1),'*'+' '*(N-2)+'*'+' '*(2*N-3-2*i)+'*'+' '*(N-2)+'*')
# print('*'*N+' '*(2*N-3)+'*'*N)

'10997 별찍기-22'

# N=int(input())
# x= ['*****','*','* ***']
# y= ['*   *','*****']
# if N==1:
#     print('*')
# else:

#     for i in range(1,N-1):
#         x[0]='* '+x[0]+'**'
#         x[1]='* *'+' '*(4*i+1)+'*'
#         for j in range(2,len(x)):
#             x[j]='* '+x[j]+' *'
#         x.insert(0,'*')
#         x.insert(0,'*'*(4*i+5))
#     x.append('*'+' *'*2*(N-1))
#     x.append('*'+' *'*2*(N-1))
#     for i in range(1, N-1):
#         for j in range(len(y)):
#             y[j]='* '+y[j]+' *'
#         y.append('*'+' '*(4*i+3)+'*')
#         y.append('*'*(4*i+5))
#         # print(y)
    
    
    
    
#     for i in range(len(x)):
#         print(x[i])
#     for i in range(len(y)):
#         print(y[i])
'2490 윷놀이'
# answer1
# for i in range(3):
#     N = sum(list(map(int,input().split())))
    
#     if N==0:
#         print('D')
#     elif N==1:
#         print('C')
#     elif N==2:
#         print('B')
#     elif N==3:
#         print('A')
#     else:
#         print('E')        
# answer2
# x = []
# for i in range(3):
#     x.append(sum(list(map(int,input().split()))))
# for i in range(3):
#     if x[i]==0:
#         print('D')
#     elif x[i]==1:
#         print('C')
#     elif x[i]==2:
#         print('B')
#     elif x[i]==3:
#         print('A')
#     else:
#         print('E')  



'2108 통계학'
# import collections
# import sys
# input = sys.stdin.readline
# N=int(input())
# x=[]
# for i in range(N):
#     x.append(int(input()))
# x=sorted(x)
# print(round(sum(x)/N))
# print(x[N//2])
# com = collections.Counter(x).most_common(2)
# if len(com)==1:
#     print(com[0][0])
# else:
#     if com[0][1]==com[1][1]:
#         if com[0][1]==com[1][1]:
#             print(com[1][0])
#         else:
#             print([0][0])
#     else:
#         print(com[0][0])
# print(max(x)-min(x))

'1100'
# import sys
# input = sys.stdin.readline
# from collections import Counter
# x=[]
# s=0
# for i in range(8):
#     x.append(list(input()))
# for i in range(0,8,2):
#     for j in range(0,8,2):
#         s+=Counter(x[i][j])['F']
# for i in range(1,8,2):
#     for j in range(1,8,2):
#         s+=Counter(x[i][j])['F']
# print(s)

'2576'
# x = []
# for i in range(7):
#     N = int(input())
#     if N%2==1:
#         x.append(N)
# s = sum(x)
# if s==0:
#     print(-1)
# else:
#     print(s)
#     print(min(x))


'5338'
# print("       _.-;;-._"+"\n"+"'-..-'|   ||   |"+"\n"+"'-..-'|_.-;;-._|"+"\n"+"'-..-'|   ||   |"+"\n"+"'-..-'|_.-''-._|")

'1476'
# x= list(map(int,input().split()))
# for i in range(3):
#     x[i]-=1
# y=[0,0,0]
# cnt=1
# while(x!=y):
    
#     y[0]=(y[0]+1)%15
#     y[1]=(y[1]+1)%28
#     y[2]=(y[2]+1)%19
#     cnt+=1
# print(cnt)
'11050'
# n,k=map(int,input().split())
# s=1
# if k==0 or n==k:
#     print(1)
# else:
#     for i in range(k):
#         s*=(n-i)/(i+1)
#     print(int(s))
'10808'
# from collections import Counter
# x = list(input())
# cnt = Counter(x)
# alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# for i in range(len(alp)):
#     print(cnt[alp[i]],end=' ')

'2167'
# import sys
# input = sys.stdin.readline
# num=[]
# N,M = map(int,input().split())
# for i in range(N):
#     num.append(list(map(int,input().split())))
# K = int(input())
# for i in range(K):
#     s=0
#     a,b,x,y = map(int,input().split())
#     for i in range(a-1,x):
#         s+=sum(num[i][b-1:y])
#     print(s)
        
'1475 방번호'
# from collections import Counter
# N=input()
# x = Counter(N)
# a = (x['6']+x['9']+1)//2
# if '6'in x:
    
#     del(x['6'])
# if '9' in x:
#     del(x['9'])
# if len(x)==0 or (a>max(x.values())) :
#     print(a)
# else:
#     print(max(x.values()))

'1009 분산처리'
# import sys
# input = sys.stdin.readline
# for i in range(int(input())):
#     a, b=map(int,input().split())
#     x= a%10
#     if x==1 or x==5 or x==6:
#         print(x)
#     elif x==2 or x==3 or x==7 or x==8:
#         print(int(((x)**(b%4+4))%10))
        
#     elif x==4 or x==9:
#         print(int(((x)**(b%2+2))%10))
#     elif x==0:
#         print(10)
'10797'

# N = int(input())%10

# x = list(map(int,input().split()))

# s=0
# for i in range(len(x)):
#     if x[i]==N:
#         s+=1
# print(s)
'2902'
# x = input()
# k = 1
# c = ''
# for i in range(len(x)):
#     if k==1:
#         c+=x[i]
#         k=0
#         continue
#     if x[i]=='-':
#         k=1
# print(c)

'11942'
# print('고려대학교')
'10989'
# import sys
# input = sys.stdin.readline
# x=[0]*10001
# for i in range(int(input())):
#     x[int(input())]+=1
# for i in range(10001):
#     if x[i]!=0:
#         for j in range(x[i]):
#             print(i)

'1032'
# N=int(input())
# x=list(input())

# for i in range(N-1):
#     y=input()
#     for j in range(len(y)):
#         if x[j]!=y[j]:
#             x[j]='?'
# for i in range(len(x)):
#     print(x[i],end='')
            

'2455'

# max_s=0
# s=0
# for i in range(4):
#     op,ip = map(int,input().split())
#     s=s-op+ip
#     if s>max_s:
#         max_s=s
# print(max_s)


'7568'

# A=[]
# for i in range(int(input())):
#     x=list(map(int,input().split()))
#     A.append(x)

# for B in A:
#     rank=1
#     for C in A:
#         if B[0]<C[0] and B[1]<C[1]:
#             rank+=1
#     print(rank)
            

'11723'

        
# import sys
# input = sys.stdin.readline

# s=[0]*21
# for i in range(int(input())):
#     inp= input().strip().split()
#     if len(inp)==1:
#         if inp[0]=='all':
#             s=[1]*21
#         else:
#             s=[0]*21
#     else:
#         op,x= inp[0],inp[1]
#         x=int(x)
#         if (op=='add') and s[x]==0:
#             s[x]+=1
#         elif (op=='remove') and s[x]==1:
#             s[x]-=1
#         elif (op=='check'):
#             if s[x]==1:
#                 print(1)
#             else:
#                 print(0)
#         elif (op=='toggle'):
#             if s[x]==1:
#                 s[x]-=1
#             else:
#                 s[x]+=1

'2231'
# inp=int(input())
# num=0
# while(True):
#     num+=1
#     new_num=num
#     x=list(str(num))
#     for i in x:
#         new_num+=int(i)
#     if new_num==inp:
#         print(num)
#         break
#     if num>inp:
#         print(0)
#         break

'1018 체스판 다시 칠하기'

# import sys
# input = sys.stdin.readline
# x,y = map(int,input().split())
# m=[]
# for i in range(x):
#     m.append(list(input()))
# min_s=32
# for a in range(x-7):
#     for b in range(y-7):
#         s=0
#         for i in range(0,8,2):
        
#             for j in range(0,8,2):
#                 if m[a+i][b+j]=='W':
#                     s+=1
#             for j in range(1,8,2):
#                 if m[a+i][b+j]=='B':
#                     s+=1
#         for i in range(1,8,2):
        
#             for j in range(0,8,2):
#                 if m[a+i][b+j]=='B':
#                     s+=1
#             for j in range(1,8,2):
#                 if m[a+i][b+j]=='W':
#                     s+=1
#         if s>32:
#             s=64-s
#         if min_s>s:
#             min_s=s
# print(min_s)
'4673'

# def d(x):
#     x=str(x)
#     s=int(x)
#     for i in range(len(x)):
#         s+=int(x[i])
#     return s

# x= set(range(1,10001))
# ad = set()

# for i in range(1,10001):
#     for j in str(i):
#         i+=int(j)
#     ad.add(i)
# x= sorted(x-ad)
# for i in range(len(x)):
#     print(x[i])


'5565'
# N=int(input())
# for i in range(9):
#     N-=int(input())
# print(N)

'2953'
# import sys
# input= sys.stdin.readline
# M=0
# for i in range(5):
#     x = list(map(int,input().split()))
#     s = sum(x)
#     if M<s:
#         M=s
#         winner=i+1
# print(winner, end=' ')
# print(M)

'3003'

# ans=[1,1,2,2,2,8]
# x=list(map(int,input().split()))
# for i in range(6):
#     print(ans[i]-x[i],end=' ')

'1550'
# x= input()
# s=0
# for i in range(len(x)):
#     if x[i]=='A':
#         s+=10*16**(len(x)-1-i)
#     elif x[i]=='B':
#         s+=11*16**(len(x)-1-i)
#     elif x[i]=='C':
#         s+=12*16**(len(x)-1-i)
#     elif x[i]=='D':
#         s+=13*16**(len(x)-1-i)
#     elif x[i]=='E':
#         s+=14*16**(len(x)-1-i)
#     elif x[i]=='F':
#         s+=15*16**(len(x)-1-i)
#     else:
#         s+=int(x[i])*16**(len(x)-1-i)
# print(s)
    
'5339'
# print('     /~\\'+'\n'+'    ( oo|'+'\n'+'    _\=/_'+'\n'+'   /  _  \\'+'\n'+'  //|/.\|\\\\'+'\n'+' ||  \ /  ||'+'\n'+'============'+'\n'+'|          |'+'\n'+'|          |'+'\n'+'|          |')

'3003'
# L,P=map(int,input().split())
# num=L*P
# x = list(map(int,input().split()))
# for i in range(5):
#     print(x[i]-num,end= ' ')

'11655'
# alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# ALP = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


# x = input()
# for i in range(len(x)):
#     if x[i] in alp:
#         print(alp[(alp.index(x[i])+13)%26],end='')
#     elif x[i] in ALP:
#         print(ALP[(ALP.index(x[i])+13)%26], end='')
#     else:
#         print(x[i], end='')

'3190 뱀'

# d_x=[1, 0, -1, 0]
# d_y=[0, 1, 0, -1]
# N=int(input())
# ind=0
# maap  = [[0 for i in range(N)] for j in range(N)]
# K=int(input())
# for i in range(K):
#     m,n=map(int,input().split())
#     maap[m-1][n-1]=1
# L=int(input())
# x=0
# y=0
# snake=[[0,0]]
# maap[x][y]=2
# time=0
# k=0
# di = []
# for i in range(L):
#     di.append(list(map(str,input().split())))
# while(True):
#     if k<L:
#         if time==int(di[k][0]):
#             if di[k][1]=='L':
#                 ind= (ind-1)%4
#             else:
#                 ind= (ind+1)%4
#             k+=1
#     x+=d_x[ind]
#     y+=d_y[ind]    
#     time+=1
#     if 0<=x<N and 0<=y<N and maap[y][x]!=2:
#         snake.append([x,y])
#         if maap[y][x]==0:
#             maap[snake[0][1]][snake[0][0]]=0
#             del snake[0]
#         maap[y][x]=2
#     else:
#         break    
# print(time)
        
'20057 마법사 상어와 토네이도'
# import sys
# input= sys.stdin.readline
# d_x=[-1,0,1,0]
# d_y=[0,1,0,-1]
# ind=-1
# N=int(input())
# x=N//2+2
# y=N//2+2
# A = [[0 for i in range(N+4)] for i in range(2)]
# for i in range(N):
#     A.append([0,0]+list(map(int,input().split()))+[0,0])
# for i in range(2):
#     A.append([0 for i in range(N+4)])

# Nu=1
# s=0
# ke=1
# while(ke):
#     Nu+=1
#     ind=(ind+1)%4
#     for i in range(Nu//2):
#         x+=d_x[ind]
#         y+=d_y[ind]
#         if x<2:
#             ke=0
#             break
#         if A[y][x]==0:
#             continue
#         else:
#             A[y+2*d_x[ind]][x+2*d_y[ind]]+=int(0.02*A[y][x])
#             A[y-2*d_x[ind]][x-2*d_y[ind]]+=int(0.02*A[y][x])
#             A[y+d_x[ind]][x+d_y[ind]]+=int(0.07*A[y][x])
#             A[y-d_x[ind]][x-d_y[ind]]+=int(0.07*A[y][x])
#             A[y+d_x[ind]+d_y[ind]][x+d_y[ind]+d_x[ind]]+=int(0.1*A[y][x])
#             A[y-d_x[ind]+d_y[ind]][x-d_y[ind]+d_x[ind]]+=int(0.1*A[y][x])
#             A[y+d_x[ind]-d_y[ind]][x+d_y[ind]-d_x[ind]]+=int(0.01*A[y][x])
#             A[y-d_x[ind]-d_y[ind]][x-d_y[ind]-d_x[ind]]+=int(0.01*A[y][x])
#             A[y+2*d_y[ind]][x+2*d_x[ind]]+=int(0.05*A[y][x])
#             A[y+d_y[ind]][x+d_x[ind]]=A[y+d_y[ind]][x+d_x[ind]]+A[y][x]-2*int(0.01*A[y][x])-2*int(0.1*A[y][x])-2*int(0.07*A[y][x])-2*int(0.02*A[y][x])-int(0.05*A[y][x])
#             A[y][x]=0

# s= sum(A[0])+sum(A[1])+sum(A[-1])+sum(A[-2])

# for i in range(2,N+2):
#     s+=A[i][0]+A[i][1]+A[i][-1]+A[i][-2]
# print(s)
