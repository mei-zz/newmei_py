# 30+A=第三十二题
Dict={}
def generateDict(X):    #传入实参为字符串
    Dict[X]=int(X)*int(X)

if __name__ == '__main__':
    for i in range(1,21):
        generateDict(str(i))
    print(Dict.keys())

