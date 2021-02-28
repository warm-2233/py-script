# ../py385/scripts/python
import markdown
from mdx_math import MathExtension


html_body_file = open("some_file.md","r",encoding='utf-8')
html_body_txt = html_body_file.read()
html_body_file.close()







# 所支持的复杂元素
exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc',MathExtension(enable_dollar_delimiter=True)]

md = markdown.Markdown(extensions = exts)
html_body = md.convert(html_body_txt)

html = html_body
html_file = open("file.html","w",encoding='utf-8')
html_file.write(html)
html_file.close()











"""
import markdown

import codecs


input_file = codecs.open("some_file.md", mode="r", encoding="utf-8")
text = input_file.read()

# 转为 html 文本
html = markdown.markdown(text)

# 保存为文件
output_file = codecs.open("some_file.html", mode="w", encoding="utf-8")
output_file.write(html)


"""