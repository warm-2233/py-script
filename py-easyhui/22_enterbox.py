import easygui
# easygui.egdemo()      # 显示模块示例


'''     只要一个参数， 标题和按钮可以省略，第三个参数默认内容 返回内容 '''
but = easygui.enterbox('内容,与choicebox一样, 多了全选和不选项','标题','默认内容')
print(but)
but = easygui.enterbox('只有一个参数的情况')
print(but)
easygui.msgbox('只要一个参数， 标题和按钮可以省略，第三个参数默认内容 返回内容')
