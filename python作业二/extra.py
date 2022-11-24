# tuple1=(1,2,3,4,5,6,7,8,9,10)
# l=list()
# for i in range(len(tuple1)):
#     if tuple1[i] % 2 == 0:
#         l.append(tuple1[i])
#
# tuple2=tuple(l)
# print(tuple2)

# x=eval(input("请输入X,Y的值："))
# print(type(x))
#****************************************#
# x,y=eval(input("请输入X,Y的值："))
# print(x,y)
# a=[]
# for i in range(x):
#     b=[]
#     for j in range(y):
#         b.append(j*i)
#     a.append(b)
# print(a)

# output_string = "输出项1=%s 输出项2=%s 输出项3=%s 输出项4=%s" % (1,2,3,4)
# print(type("%s" % 1))
# # print(output_string)

# output_string = "输出项1={} 输出项2={} 输出项3={} 输出项4={}".format("a",2,3,4)
# print(type("{}".format(1)))




'''
ABb1234@1,a F1#,2w3E*,2We3345
'''
def lenth(A):
    LenthNum = len(A)
    return LenthNum

def StrOrd(A):
    StrNum = ord(A)
    return StrNum
if __name__ == '__main__':
    up_count, low_count, single_count= 0, 0, 0
    print('请输入多个密码用逗号隔开：')
    PassWords = input().split(',')
    for i in range(len(PassWords)):
        print(i)
        if (len(PassWords[i])<=6 or 12<= len(PassWords[i])):
            PassWords.remove(PassWords[i])
            i-=1
        else:
            continue
    print(PassWords)
    for i in PassWords:
        for a in i:
            if a.islower():
                low_count += 1
            elif a.isupper():
                up_count += 1
        if low_count == 0 or up_count == 0:
            PassWords.remove(i)
    print(PassWords)
    for i in PassWords:
        for a in i:
            if a=='@' or a=='#' or a=='$':
                single_count += 1
        if single_count == 0:
            PassWords.remove(i)
    print(PassWords)