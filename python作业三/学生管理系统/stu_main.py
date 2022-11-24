import stu_tools
while True:
    #TODO(梅) 显示功能菜单
    stu_tools.show_menu()
    action_str = input("请选择希望执行的操作:")
    print("您选择的操作是P【%s】"%action_str)
    #1,2,3针对学生的操作
    if action_str in ["1","2","3"]:
        #新增
        if action_str == "1":
            stu_tools.new_card()
        #显示全部
        elif action_str == "2":
            stu_tools.show_all()
        #查询
        elif action_str == "3":
            stu_tools.search_card()
    # 0 退出系统
    elif action_str == "0":
        print("欢迎使用【学生管理系统】")
        break
    else:
        print("您输入的不正确，请重新输入：")