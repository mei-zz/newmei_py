import numpy as np
# 三个根的大致位置，求具体解
# (1)[0,0.778]
# (2)[2.556,3.444]
# (3)[6.111，7.000]
result=[]
def clacY(x):
    value_y=(np.exp(-x) - np.sin(x))
    return value_y
def solve(first,end):
    middle=(first+end)/2
    temp=clacY(middle)
    if(round(temp,3) == 0):
        result.append(middle)
    elif(temp*clacY(first)<0):
        end=middle
        solve(first,end)
    elif (temp * clacY(end) < 0):
        first=middle
        solve(first, end)
solve(0.000,0.778)
solve(2.556,3.444)
solve(6.111,7.000)
print(result)



# *****************改动*********************
"""
result=[]

def clacY(x):
    value_y=(np.exp(-x) - np.sin(x))
    return value_y
def solve(first,end):
    middle=(first+end)/2
    temp=clacY(middle)
    if(round(clacY(temp),3) == 0):
        result.append(temp)
    elif(temp*clacY(first)<0):
        end=middle
    elif (temp * clacY(end) < 0):
        first=middle
    print(middle)
while 1:
    solve(0.000,0.778)
    if(len(result)!=0):
        break
print(result)   #0.2984709538907072
"""