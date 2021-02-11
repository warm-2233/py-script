# pywebio

```shell script
pip3 install -U pywebio
```

[github](https://github.com/ryuutanyou/PyWebIO)

[文档](https://pywebio.readthedocs.io/zh_CN/latest/)

## hello world
```python
from pywebio.input import input
from pywebio.output import put_text

def main():
    h = input("输入：", value="hello world")
    print(h)
    put_text(h)

if __name__ == '__main__':
    main()
```

## 输入

```python
# 密码输入
password = input("Input password", type=PASSWORD)

# 下拉选择框
gift = select('Which gift you want?', ['keyboard', 'ipad'])

# 勾选选项
agree = checkbox("用户协议", options=['I agree to terms and conditions'])

# 单选选项
answer = radio("Choose one", options=['A', 'B', 'C', 'D'])

# 多行文本输入
text = textarea('Text Area', rows=3, placeholder='Some text')

# 文件上传
img = file_upload("Select a image:", accept="image/*")
```


