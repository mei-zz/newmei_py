"""
用一条语句生成一个 包含0-2000之间所有奇数的列表，
找出列表中可以整除3、6、7、15、35的数，
分别存放在L3,L6,L7,L15, L35这几个列表中，
并找到这几个列表中共有的元素，打印出来。
"""
L3 = []
L6 = []
L15 = []
L35 = []
odd_list = [x for x in range(0, 2001) if x % 2 != 0]
for i in range(len(odd_list)):
    if odd_list[i] % 3 == 0:
        L3.append(odd_list[i])
    if odd_list[i] % 6 == 0:
        L6.append(odd_list[i])
    if odd_list[i] % 15 == 0:
        L15.append(odd_list[i])
    if odd_list[i] % 35 == 0:
        L35.append(odd_list[i])

print(set(L3).intersection(set(L6)).intersection(set(L15)).intersection(set(L35)))

