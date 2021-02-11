import easygui
# easygui.egdemo()      # 显示模块示例


'''   
        只要一个参数，
        第三个参数默认路径和文件类型
        第四个参数 可迭代对象 限定文件类型
        第五个参数 True False 表示是否可以选择多个文件
        返回文件完整路径
        

'''
but = easygui.fileopenbox('内容','标题','c:\\*.py',('*.jpg','*.png'),True)
print(but)
but = easygui.fileopenbox('内容')
print(but)
easygui.msgbox('返回文件完整路径')
