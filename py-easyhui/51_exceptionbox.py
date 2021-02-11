import easygui
# easygui.egdemo()      # 显示模块示例


'''

'''
try:
    int('w')
except:
    but = easygui.exceptionbox('内容','标题')
    print(but)
but = easygui.exceptionbox('内容')
print(but)
easygui.msgbox('返回None')
