import easygui
# easygui.egdemo()      # 显示模块示例


'''     只要一个参数， 标题和默认值可以省略，第三个参数传入默认值 返回内容 '''
but = easygui.passwordbox('内容','标题','默认值')
print(but)
but = easygui.passwordbox('只有一个参数的情况')
print(but)
easygui.msgbox('只要一个参数，标题和默认值可以省略，第三个参数传入默认值 返回内容')
