#1题
X=int(input("请输入学号："))
def mod(a,X):
    X=X%a
    print(X)

if __name__ == '__main__':
    for i in [13,3,5,7,50]:
        mod(i,X)    #A:0 B:1 C:3 D:6 E:13