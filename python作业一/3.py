#第七题
from numpy import *
i,j=input().split(",")
i=int(i)    #3
j=int(j)    #5
res=[[0 for j in range(1,j+1)]for i in range(1,i+1)]
# print(res)
for row in range(0,i):    #0,1,2
    for column in range(0,j): #0,1,2,3,4
        res[row][column]=row*column
print(res)

# m1 = array([arange(1,4),arange(4,7),arange(7,10),arange(10,13),arange(13,16),arange(16,19)])