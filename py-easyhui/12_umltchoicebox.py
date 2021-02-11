import easygui
# easygui.egdemo()      # 显示模块示例


'''     只要一个参数， 标题和按钮可以省略，第三个参数传入[元祖或列表(可迭代对象)]返回内容列表 '''
but = easygui.multchoicebox('内容,与choicebox一样, 多了全选和不选项','标题',('aaaaaaaa','bbbbb','cc'))
print(but)
but = easygui.multchoicebox('只有一个参数的情况')
print(but)
easygui.msgbox('只要一个参数， 标题和按钮可以省略，第三个参数传入[元祖或列表(可迭代对象)]返回内容列表 ')
