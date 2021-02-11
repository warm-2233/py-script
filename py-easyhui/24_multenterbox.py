import easygui
# easygui.egdemo()      # 显示模块示例


'''     只要一个参数内容，第二个参数标题，第三个参数为可迭代对象 返回内容列表 '''
but = easygui.multenterbox('数字输入框','标题',('111111','2222'))
print(but)

easygui.msgbox('''     只要一个参数内容，第二个参数标题，第三个参数为可迭代对象 返回内容列表 ''')
