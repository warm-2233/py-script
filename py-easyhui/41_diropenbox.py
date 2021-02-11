import easygui
# easygui.egdemo()      # 显示模块示例


'''   
        只要一个参数，
        第三个设置大开默认目录
        返回目录路径

'''
but = easygui.diropenbox('内容','标题','C:\Windows')
print(but)
but = easygui.diropenbox('内容')
print(but)
easygui.msgbox('返回目录路径')
