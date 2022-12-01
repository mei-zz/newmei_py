"""
编写一个函数，利用“递归方法”对输入的参数分解质因数，
并将结果用append方法加入到一个列表中，分解完毕后，
利用for循环遍历，将列表中元素逐个打印出来；
"""
enter = int(input("请输入："))
print("{} =".format(enter), end=' ')


def recursion_segm_primeFactor(x):
    for i in range(2, x + 1):  # 质数条件：被2和自身整除
        if x % i == 0:
            next_x = int((x / i))
            if i == x:
                print(str(i), end=' ')
            else:
                print(str(i) + " *", end=' ')
            if next_x == 1:
                exit()
            else:
                recursion_segm_primeFactor(next_x)


if __name__ == '__main__':
    recursion_segm_primeFactor(enter)
