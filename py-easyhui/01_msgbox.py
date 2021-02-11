import easygui
# easygui.egdemo()      # 显示模块示例


'''     只要一个参数， 标题和按钮可以省略， 点击按钮返回按钮内容，X掉返回None'''
but = easygui.msgbox('内容','标题','按钮')
print(but)


easygui.msgbox('只要一个参数， 标题和按钮可以省略')
