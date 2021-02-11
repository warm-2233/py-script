import easygui
# easygui.egdemo()      # 显示模块示例


'''     只要一个参数， 标题和按钮可以省略，第三个参数传入[元祖或列表(可迭代对象)]（可以传入N多值）返回内容'''
but = easygui.buttonbox('内容,与ynbox/ccbox类似','标题',['1','2','3','4','5','6','7'])
print(but)
but = easygui.buttonbox('只有一个参数的情况')
print(but)
easygui.msgbox('只要一个参数， 标题和按钮可以省略，第三个参数传入[元祖或列表(可迭代对象)]（可以传入N多值）返回内容')

