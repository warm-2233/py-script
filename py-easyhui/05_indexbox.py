import easygui
# easygui.egdemo()      # 显示模块示例


'''     只要一个参数， 标题和按钮可以省略，第三个参数传入[元祖或列表(可迭代对象)]（可以传入N多值）返回索引值 0-N'''
but = easygui.indexbox('内容,与buttonbox类似','标题','aaabbbccc')
print(but)
but = easygui.indexbox('只有一个参数的情况')
print(but)
easygui.msgbox('只要一个参数， 标题和按钮可以省略，第三个参数传入[元祖或列表(可迭代对象)]（可以传入N多值）返回索引值 0-N')
