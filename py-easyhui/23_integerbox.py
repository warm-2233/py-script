import easygui
# easygui.egdemo()      # 显示模块示例


'''     只要一个参数， 标题和按钮可以省略，第三个参数默认内容 返回内容 '''
but = easygui.integerbox('数字输入框','标题',lowerbound=0, upperbound=11111111111111)
print(but)
but = easygui.integerbox('只有一个参数的情况')
print(but)
easygui.msgbox('只要一个参数， 标题和按钮可以省略，lowerbound 最小值, upperbound=最大值')
