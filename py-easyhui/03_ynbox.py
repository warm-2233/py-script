import easygui
# easygui.egdemo()      # 显示模块示例


'''     只要一个参数， 标题和按钮可以省略，第三个参数传入[元祖或列表(可迭代对象)](只能有两个参数)返回True False '''
but = easygui.ynbox('内容,ynbox与ccbox一样','标题',['定','不',])
print(but)
but = easygui.ynbox('只有一个参数的情况')
print(but)
easygui.msgbox('只要一个参数， 标题和按钮可以省略，第三个参数传入[元祖或列表(可迭代对象)]返回True False')
