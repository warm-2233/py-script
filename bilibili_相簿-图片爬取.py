# coding: utf-8

import os
import re
import json
import requests as req

path = os.getcwd() + "\\bilibili_img\\"

headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45"
}

# https://search.bilibili.com/photo?keyword=初音&order=totalrank&category_id=0

def search(keyword, order='totalrank', category_id=1, page=1):
    ''' 获取文章链接中的 id 值 '''
    url = f"https://search.bilibili.com/photo?keyword={keyword}&order={order}&category_id={category_id}&page={page}"
    res = req.get(url, headers=headers)
    con = res.content.decode()
    # <li class="photo-item"><a href="//h.bilibili.com/56871096?from=search" title="初音未来" target="_blank"><div class="img">
    r = r'<li class="photo-item"><a href="//h.bilibili.com/(\d+)'
    id_list = re.findall(r, con)

    return id_list
    

def get_img_api_url(id_list):
    api_list = []
    # https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id=1162771
    for api in id_list:
        api_list.append('https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id='+api)

    img_url_list = []
    for url in api_list:
        res = req.get(url, headers=headers)
        con = json.loads(res.content.decode())

        for i in range(len(con['data']['item']['pictures'])):
            img_url_list.append(con['data']['item']['pictures'][i]['img_src'])

    return img_url_list

def write_img(url_imgs):
    if not os.path.isdir(path):
        os.mkdir(path)
    for img in url_imgs:
        res = req.get(img, headers=headers)
        with open(path+img.split('/')[-1], 'wb') as f:
            f.write(res.content)

    
id_list = search("初音")
# id_list=['56871096']

img_urls = get_img_api_url(id_list)
write_img(img_urls)
