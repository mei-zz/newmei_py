import numpy as np
def eight_queen(n):
    """
    八皇后【宽度优先】
    :param n:棋盘的大小：n*n
    :return:无返回，直接打印棋盘结果
    """
    n = int(n)
    board = initBoard(n)    #board为初始化棋盘【全零的二维数组】
    print("打印初始化棋盘")
    print(board)
    print("---------------------------------------")

    for i in range(n):  # 遍历第一行能够走的位置，从0【第一个位置开始】
        board[0][i] = 1   # 把第一行第一个元素赋值1：表示走的位置
        put_next(n, 1, board)   # 放置下一行的位置
        board[0][i] = 0     # 把走过的i列，重新初始化为0
    print("当输入为", n, "时，共计", cnt, "种方式")
    return

def put_next(n, row, board):
    """
    添加棋子
    :param n:棋盘大小【边长】 --->8
    :param row:下一行【需要放置】的行数
    :param board:棋盘
    :return:
    """
    if(row == n):   # 当 当前的行数已经是最后一行则能够输出一种结果
        global cnt
        cnt += 1
        print("第", cnt, "种结果如下：")
        print(board)
        print("-----------------------------------")
        return
    for j in range(n):  # 对每一行能放置的位置从第一个开始判断【j表示列】
        if(check(board, row, j, n)):    # 判断放置的位置是否符合规则，如果不符合则返回，符合才修改棋盘
            # 修改棋盘
            board[row][j] = 1   # 确定放置位置
            row += 1    # 下一行的放置位置确定了，继续对下一行进行判断
            put_next(n, row, board)   # 递归，找下一行的解
            row -= 1    # 当找到最后一行，发现无法放置 则返回上一行
            board[row][j] = 0   # 将上一行放置的位置变为0，重新选择位置
    return

def initBoard(n):
    """
    初始化棋盘 --->棋盘中 1代表选择，0代表未被选
    :param n: 棋盘大小【边长】
    :return: 棋盘
    """
    board = np.zeros((n,n),dtype=int)
    return board

def check(board, row, col, n):
    """
    检测新添加的棋子是否合法：
        依次判断每一行 为1的元素，下一行的位置是否合规。如果合规则再向上一行移动继续判断，直到第一行也判断完毕
    :param board: 当前棋盘
    :param row: 当前行
    :param col: 当前列
    :param n: 棋盘大小【边长】
    :return:
    """
    temp_x = row
    temp_x -= 1     # 得到上一行的index
    while( temp_x >= 0 ):   # 如果是第一行 则不用判断
        for j in range(n):  # 依次判断上一行放置的位置
            # 依次判断需放置元素行的 上一行的所放置的位置；通过上一行放置的位置判断下一行中的不能放置的位置是否已经有元素了
            if(board[temp_x][j] == 1):  # 找到每一行所放置的位置【上一行】
                if(j == col or abs(j - col) == abs(temp_x - row)):
                    """
                    j == col:列相等
                    abs(j - col) == abs(temp_x - row):判断上一行元素的两个斜对角位置
                    """
                    return False
        temp_x -= 1     # 当前行的判断已经符合规则后，继续返回当前行的上一行进行判断，直到第一行；
    return True

if __name__ == '__main__':
    cnt = 0     # 表示第几种结果，用于输出
    n = input("请输入棋盘大小：")
    eight_queen(n)

"""
Things:
    （1）将二维数组通过一维数组表示：
            二维数组的每一行使用一个数代替
            [[0,0,0,0,0,0,0,0],                     [0,
             [0,0,0,0,0,0,0,0],                      0,
             [0,0,0,0,0,0,0,0],                      0,
             [0,0,0,0,0,0,0,0],           ==>        0,
             [0,0,0,0,0,0,0,0],                      0,
             [0,0,0,0,0,0,0,0],                      0,
             [0,0,0,0,0,0,0,0],                      0,
             [0,0,0,0,0,0,0,0],]                     0,]
            一维数组的每一个元素，范围为0-7，即为表示在每一行所放置的位置
    （2）通过递归把树给列出来【宽度优先】：
            每一次给上一层的结点添加子节点列表时，排除解中以重复的元素
            把最后一层的结果存起来
            列表长度即为解的个数
"""