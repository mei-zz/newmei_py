#记录所有的姓名字典
stu_list = []
def show_menu():
    """显示菜单"""
    print("*"*80)
    print("欢迎使用【学生管理系统】V 1.0")
    print("")   #换行
    print("1.新增学生")
    print("2.显示全部")
    print("3.搜索学生")
    print("")
    print("0.退出系统")
    print("*"*50)


def new_card():
    """新增学生"""
    print("-"*50)
    print("新增学生")
    #1.提示用户输入姓名的详细信息
    id_str = input("请输入学号：")
    name_str = input("请输入姓名：")
    sex_str = input("请输入性别：")
    hMath_str = input("请输高数成绩：")
    LineMath_str = input("请输线代成绩：")
    Probability_str = input("请输概率论成绩：")
    English_str = input("请输英语成绩：")
    #2.使用用户输入的信息建立一个姓名字典
    stu_dict = {"id":id_str,"name":name_str,"sex":sex_str,"hMath":hMath_str
                ,"LineMath":LineMath_str,"Probability":Probability_str,"English":English_str}
    #3.将姓名字典添加到列表中
    stu_list.append(stu_dict)
    print(stu_list)
    #提示用户添加姓名成功
    print("%s的姓名添加成功"%name_str)
def show_all():
    """显示所有姓名"""
    print("-" * 50)
    print("显示所有学生")
    #判断是否存在姓名记录，如果没有，提示用户并且返回
    if len(stu_list) == 0:
        print("当前没有任何的学生记录，请使用新增功能添加")
        #return 可以返回一个函数的执行结果
        #下方的代码不会被执行
        #如果return 后面没有任何的内容，表示会返回到调用函数的位置
        #并且不返回任何的结果
        return
    #打印表头
    for name in ["学号","姓名","性别","高数成绩","线代成绩","概率论成绩","英语成绩"]:
        print(name,end="\t\t")
    print("")
    #打印分割线
    print("="*80)
    #遍历姓名列表依次输出字典信息
    for stu1_dict in stu_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t"%(stu1_dict["id"],stu1_dict["name"],stu1_dict["sex"],stu1_dict["hMath"],
                                                        stu1_dict["LineMath"],stu1_dict["Probability"],stu1_dict["English"]))
    deal_sort()
def search_card():
    """搜索姓名"""
    print("-" * 50)
    print("搜索学生")
    #提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名:")
    #遍历姓名列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for stu1_dict in stu_list:
        if stu1_dict["name"] == find_name:
            print("学号\t\t姓名\t\t性别\t\t高数成绩\t\t线代成绩\t\t概率论成绩\t\t英语成绩\t\t")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s%s\t\t%s\t\t%s\t\t" % (stu1_dict["id"], stu1_dict["name"], stu1_dict["sex"], stu1_dict["hMath"],
                                                                stu1_dict["LineMath"], stu1_dict["Probability"], stu1_dict["English"]))
            # 针对找到的姓名记录执行修改和删除的操作
            deal_stu(stu1_dict)    #再嵌套一个函数
            break
    else:
        print("抱歉，没有找到%s" % find_name)


def deal_stu(find_dict):
    """
    处理查找到的姓名
    :param find_dict:查找到的学生
    :return:
    """
    print(find_dict)
    action_str = input("请选择要执行的操作 【1】 修改 【2】 删除 【0】 返回上一级:")
    if action_str == "1":
        find_dict["id"] = input_card_info(find_dict["id"],"学号:")
        find_dict["name"] = input_card_info(find_dict["name"],"姓名:")
        find_dict["sex"] = input_card_info(find_dict["sex"],"性别:")
        find_dict["hMath"] = input_card_info(find_dict["hMath"],"高数成绩:")
        find_dict["LineMath"] = input_card_info(find_dict["LineMath"],"线代成绩:")
        find_dict["Probability"] = input_card_info(find_dict["Probability"],"概率论成绩:")
        find_dict["English"] = input_card_info(find_dict["English"],"英语成绩:")

        print("修改姓名成功！")
    elif action_str =="2":
        stu_list.remove(find_dict)
        print("删除姓名成功！")
    #不需要对0进行写代码，因为无论输入什么都会自动返回到最初显示的页面

def deal_sort():
    action_str = input("请选择要执行的操作 【1】 按高数成绩排序【2】 按学号成绩排序 【0】 返回上一级")
    if action_str == "1":
        sort_by_hMath(stu_list)
    elif action_str == "2":
        sort_by_id(stu_list)


def input_card_info(dict_value,tip_message):
    """
    输入学生信息
    :param dict_value:字典中原有的值
    :param tip_message:输入的提示文字
    :return:如果未输入修改的文字，就返回字典中原有的值；如果输入了修改的值就返回修改值
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)
    # 2.针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3.如果用户没有输入内容，返回“字典中原有的值“
    else:
        return dict_value
"""
[
    {'id': '1', 'name': '1', 'sex': '1', 'hMath': '1', 'LineMath': '1', 'Probability': '1', 'English': '1'},
    {'id': '2', 'name': '2', 'sex': '2', 'hMath': '2', 'LineMath': '2', 'Probability': '2', 'English': '2'}
]
"""
def sort_by_hMath(stu_list):
    stu_list.sort(key=lambda x: (x['hMath']),reverse=True)
    show_all()
def sort_by_id(stu_list):
    stu_list.sort(key=lambda x: (x['id']))
    show_all()

