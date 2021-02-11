import easygui
# easygui.egdemo()      # 显示模块示例


'''     只要一个参数， 标题和按钮可以省略，第三个参数传入[元祖或列表(可迭代对象)](只能有两个参数)返回True False '''
but = easygui.ccbox('内容','标题',['确定','不要',])
print(but)
but = easygui.ccbox('只有一个参数的情况')

easygui.msgbox('只要一个参数， 标题和按钮可以省略，第三个参数传入[元祖或列表(可迭代对象)]返回True False')
