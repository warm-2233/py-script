# coding: utf-8

import os
import re
import json
import tkinter as tk
import requests as req

path = os.getcwd() + "\\bili_imgs\\"

headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45"
}

# https://search.bilibili.com/photo?keyword=初音&order=totalrank&category_id=0
def search(keyword, order='totalrank', category_id=0, page=1):
    url = f"https://search.bilibili.com/photo?keyword={keyword}&order={order}&category_id={category_id}&page={page}"
    res = req.get(url, headers=headers)
    con = res.content.decode()
    r = r'<li class="photo-item"><a href="//h.bilibili.com/(\d+)'
    id_list = re.findall(r, con)
    return id_list

def get_img_api_url(id_list):
    api_list = []
    for api in id_list:
        api_list.append('https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id='+api)
    img_url_list = []
    for url in api_list:
        res = req.get(url, headers=headers)
        con = json.loads(res.content.decode())
        for i in range(len(con['data']['item']['pictures'])):
            img_url_list.append(con['data']['item']['pictures'][i]['img_src'])
    return img_url_list

def write_img(url_imgs,k=''):
    os.mkdir(path)
    path_img = path + k +'\\'
    if not os.path.isdir(path_img):
        os.mkdir(path_img)
    for img in url_imgs:
        file = path_img+img.split('/')[-1]
        if os.path.isfile(file):
            print("文件"+file+"以存在")
            continue
        res = req.get(img, headers=headers)
        with open(file, 'wb') as f:
            f.write(res.content)
            print('文件', file, '保存成功')
    t = '文件保存于：'+path_img+"\n 保存失败请检查输入的范围是否合理，\n 不排除是我的程序的问题"
    a = tk.Label(app, text=t)
    a.place(x=50,y=300)
app = tk.Tk()
app.title('哔哩哔哩-图片-下载')
app.resizable(False,False)
app.geometry("450x450")

def run():
    _from_ = v.get()
    _to_ = v2.get()
    if _from_ > _to_:
        _from_ = _to_
    
    key = e.get()
    order = rad.get()
    category_id = c_id.get()
    
    for i in range(_from_, _to_+1):
        id_list = search(key, order, category_id,i)
        img_urls = get_img_api_url(id_list)
        write_img(img_urls,key)

        
but = tk.Button(app,text='确认',font=("微软雅黑", 24), command=run)
but.place(x=350, y=380, width=80, height=50)

l = tk.Label(app, text='搜索内容：')
l.place(x=2,y=2)
e=tk.StringVar()
e.set('初音未来')
input_ = tk.Entry(app, textvariable=e)
input_.place(x=30,y=30)

la = tk.Label(app, text='选择排序方式：')
la.place(x=2,y=60)
rad = tk.StringVar()
rad.set('totalrank')
radio1 = tk.Radiobutton(app, text="默认排序", variable=rad, value='totalrank')
radio2 = tk.Radiobutton(app, text="最多收藏", variable=rad, value='stow')
radio3 = tk.Radiobutton(app, text="最新发布", variable=rad, value='pubdate')
radio1.place(x=30, y=80)
radio2.place(x=30, y=100)
radio3.place(x=30, y=120)

la = tk.Label(app, text='选择分区：')
la.place(x=2,y=140)
c_id = tk.StringVar()
c_id.set('0')
r1 = tk.Radiobutton(app, text="全部分区", variable=c_id, value='0')
r2 = tk.Radiobutton(app, text="画友", variable=c_id, value='1')
r3 = tk.Radiobutton(app, text="摄影", variable=c_id, value='2')
r1.place(x=30, y=160)
r2.place(x=30, y=180)
r3.place(x=30, y=200)

la = tk.Label(app, text='输入爬取的范围(默认只爬取第一页)：')
la.place(x=2,y=240)
v = tk.IntVar()
v.set(1)
range_1 = tk.Spinbox(app,from_=0,to=999,increment=1,textvariable=v)
range_1.place(x=30, y=260, width=50)
la = tk.Label(app, text='to')
la.place(x=82,y=260)
v2 = tk.IntVar()
v2.set(1)
range_2 = tk.Spinbox(app,from_=0,to=999,increment=1,textvariable=v2)
range_2.place(x=110, y=260, width=50)


app.mainloop()



