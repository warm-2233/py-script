import easygui
# easygui.egdemo()      # 显示模块示例


'''   保存文件
        只要一个参数，
        第三个参数默认文件名
        第四个参数 可迭代对象 限定文件类型
        返回文件完整路径

'''
but = easygui.filesavebox('内容','标题','默认文件名',('*.jpg','*.png'))
print(but)
but = easygui.filesavebox('内容')
print(but)
easygui.msgbox('返回文件完整路径')
