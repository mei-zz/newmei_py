# 八皇后问题【宽度优先】
"""
在8×8格的国际象棋上摆放8个皇后，使其不能互相攻击，
即任意两个皇后都不能处于同一行、同一列或同一斜线上，问有多少种摆法
"""
"""
import numpy as np
init_array=np.zeros(shape=(8,8))
def decide(x,y):
    for i in range(8):
        init_array[x][i]=5
        init_array[i][y]=5
    # 正45°斜线：  (x+-1,y-+1)

    # 负45°斜线：  (x+-1,y+-1)
    init_array[x][y]=1

if __name__ == '__main__':
    decide(1,1)
    print(init_array)
"""
# import sys
# sys.setrecursionlimit(5000)
# 将8*8的空间压缩成1维，用长度为7的一维数组表示每一行存放的位置
def judge_next(i):
    list = [1, 2, 3, 4, 5, 6, 7, 8]
    line = [0] * 8
    # 第一个queen放在第一行的某个位置
    line[i-1]=1
    # 判下一行能放的位置
    if (i==1):
        list.remove(i)
        list.remove(i+1)
    elif (i==8):
        list.remove(i)
        list.remove(i-1)
    else:
        list.remove(i)
        list.remove(i-1)
        list.remove(i+1)
    return list

final_set=[]
def add_children(list,count=1):
    """
    添加下一层的子节点
    :param list:表示第一层输入的元素
    :param count:表示当前所在的层数，初始化是第一层
    :return:
    """
    line_list=[]
    final_set.append(list[0])
    for i in range(len(list)):
        temp_list=judge_next(list[i])  #[3,4,5,6,7,8]
        if(list[0] in temp_list):
            temp_list.remove(list[0])
            line_list.extend(temp_list[:])
        else:
            line_list.extend(temp_list[:])
        count += 1
    while(1):
        add_children(line_list, count)
        if(count==8):
            break
    return len(line_list)
# TODO:
#   想法（1）：把每一个子节点的children都用不同的列表保存下来
#      （2）：保存下来了之后如何判断
if __name__ == '__main__':
    res = add_children([1])
    print(res)















