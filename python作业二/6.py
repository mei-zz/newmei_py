#22+A=第二十二题
#New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
list = input().split(" ")
initDict={}
for i in list:
    if (i not in initDict):
        initDict[i]=1
    else:
        initDict[i]+=1
Dict=sorted(initDict)
for i in range(len(Dict)):
    print(Dict[i]+":"+str(initDict[Dict[i]]))
