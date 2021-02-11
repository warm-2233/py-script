import easygui
# easygui.egdemo()      # 显示模块示例


'''   
            注意：最后一个输入框是密码形式， 其他都是明文
第三个参数传入可迭代对象 返回内容列表 '''
but = easygui.multpasswordbox('内容','标题','默认值')
print(but)
easygui.msgbox('注意：最后一个输入框是密码形式， 其他都是明文第三个参数传入可迭代对象 返回内容列表 ')
