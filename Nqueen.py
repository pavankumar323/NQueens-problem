N=int(input())
chess=[[0]*N for _ in range(N)]
def attack(i,j):
    for x in range(0,N):
        if chess[i][x]==1 or chess[x][j]==1:
            return True
    for x in range(0,N):
        for y in range(0,N):
            if(x+y==i+j) or (x-y==i-j):
                if chess[x][y]==1:
                    return True;
    return False;
def nqueen(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if(not(attack(i,j))) and (chess[i][j]!=1):
                chess[i][j]=1
                if nqueen(n-1)==True:
                    return True
                chess[i][j]=0
    return False
nqueen(N)
for i in chess:
    print(i)
