"""
1.容器的遍历联系
申明一个List Lst；
寻找出0-99999之间的水仙花数、四叶玫瑰数、五角星数，并将结果存入Lst中；
使用for 对 Lst进行遍历，并将其中的偶数打印出来；
"""
# 三位自幂数：水仙花数 153 = 1^3 + 5^3 + 3^3
# 四位自幂数：四叶玫瑰数
# 五位自幂数：五角星数
lst = []
for temp_x in range(99, 100000):
    x = str(temp_x)
    if len(x) == 3:
        if int(x) == (int(x[0]) ** 3) + (int(x[1]) ** 3) + (int(x[2]) ** 3):
            lst.append(int(x))
    if len(x) == 4:
        if int(x) == (int(x[0]) ** 4) + (int(x[1]) ** 4) + (int(x[2]) ** 4):
            lst.append(int(x))
    if len(x) == 5:
        if int(x) == (int(x[0]) ** 5) + (int(x[1]) ** 5) + (int(x[2]) ** 5):
            lst.append(int(x))
if __name__ == '__main__':
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            print(lst[i])
