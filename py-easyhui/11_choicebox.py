import easygui
# easygui.egdemo()      # 显示模块示例


'''     只要一个参数， 标题和按钮可以省略，第三个参数传入[元祖或列表(可迭代对象)]返回内容 '''
but = easygui.choicebox('内容,','标题',('aaaaaaaa','bbbbb','cc'))
print(but)
but = easygui.choicebox('只有一个参数的情况')
print(but)
easygui.msgbox('只要一个参数， 标题和按钮可以省略，第三个参数传入[元祖或列表(可迭代对象)]返回内容 ')
