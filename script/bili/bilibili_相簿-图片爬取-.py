#! usr/bin/python
# coding: utf-8

import os
import re
import json
import sys
import time
import threading
import requests as req

headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45"
}

# https://search.bilibili.com/photo?keyword=初音&order=totalrank&category_id=0
def search(keyword, order='totalrank', category_id=0,from_=1, to_=1):
    id_list = []
    if from_ > to_:from_ = to_
    for i in range(from_, to_):
        url = f"https://search.bilibili.com/photo?keyword={keyword}&order={order}&category_id={category_id}&page={i}"
        res = req.get(url, headers=headers)
        con = res.content.decode()
        r = r'<li class="photo-item"><a href="//h.bilibili.com/(\d+)'
        i = re.findall(r, con)
        id_list.extend(i)
        global flag
        flag += 1
        print(flag)
    if not id_list:
        print('没有你想要的结果')
        # global flag
        flag -= 1
        sys.exit()
    return id_list

def get_img_api_url(id_list):
    api_list = []
    for api in id_list:
        api_list.append('https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id='+api)
    img_url_list = []
    for url in api_list:
        res = req.get(url, headers=headers)
        con = json.loads(res.content.decode())
        if con.get('code') == -412:
            print('请求被拦截')
            continue
        
        for i in range(len(con['data']['item']['pictures'])):
            img_url_list.append(con['data']['item']['pictures'][i]['img_src'])
    return img_url_list

def write_img(url_imgs,k=''):
    if not os.path.isdir(path):os.mkdir(path)
    path_img = path + k +'/'
    if not os.path.isdir(path_img):
        os.mkdir(path_img)
    for img in url_imgs:
        time.sleep(0.1)
        file = path_img+img.split('/')[-1]
        if os.path.isfile(file):
            print("文件"+file+"以存在")
            continue
        res = req.get(img, headers=headers)
        with open(file, 'wb') as f:
            f.write(res.content)
            print('文件', file.split('/')[-1], '保存成功')
        images_url(path_img, img)
    global flag
    flag -= 1
    print('+++++++++++一项任务完成++++++++++++++')
    if not flag:
        print('='*40,'\n',)
        print('*'*10,'所有任务全部完成','*'*10)
        print('='*40,'\n\n',)

def images_url(p, t):
    with open(p + 'urls.txt', 'a') as f:
        f.write(t+'\n')
def run(i, order, category_id, f ,t):
    print('任务开始：',i)
    ids = search(i, order, category_id,f ,t)
    imgs = get_img_api_url(ids)
    write_img(imgs,i)

if __name__ == '__main__':
    flag = 0
    # path = "/storage/emulated/0/01biliuuuas/a"
    path = os.getcwd() + '/bili-相簿-images/'
    print('搜索关键字')
    keyword = input("keyword:")
    print("排序方式《1=最新，2=收藏最多，输入错误/不输入=默认排序》")
    order = input("order:")
    if order == "" or order == "0":
        order = "totalrank"
    elif order == "1":
        order = "stow"
    elif order == "2":
        order = "pubdate"
    else:
        order = "totalrank"

    print("选择类型《1=画友，2=摄影，空/输入错误=默认》")
    category_id = input("category_id:")
    if category_id == "": category_id = "0"
    if not category_id in ['0','1','2']: category_id = "0"
    print("页数，默认第一页")
    from_ = input("from:")
    if from_ == "": from_ = 1
    to_ = input("to:")
    if to_ == "": to_ = 1
    try: 
        from_ = int(from_)
        to_ = int(to_)
    except:
        from_ = 1
        to_ = 1
    if from_ > to_:from_ = to_

    for i in range(from_, to_ + 1):
        t = threading.Thread(target=run,
                                args=[keyword, order, category_id, i, i + 1],
                                name='get')
        t.start()
        
    
    
    
    
    
