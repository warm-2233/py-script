# coding: utf-8

import os
import re
import json
import time

import requests

path = os.getcwd() + "\\bilibili_up专栏_图片\\"

headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45"
}
#==========================================================


# https://api.bilibili.com/x/space/article?mid=166559060&pn=1
def up_id(mid):
    article_list = []
    pn = 1
    if mid[:4] == "url=":
        url = [mid[4:]]
        a = get_img_url(url)
        cv = re.findall(r'http.*(cv\d*)',url[0])[0]
        print(cv)
        preserve_img(a)
        EXIT('保存完毕', 2)
        
    if not mid.isdecimal():
        EXIT('id 必须是数字')

    while True:
        url = f"https://api.bilibili.com/x/space/article?mid={mid}&pn={pn}"
        res = requests.get(url, headers=headers)
        con = res.content.decode()
        j = json.loads(con)
        if not j.get('data').get('articles'):
            if not article_list:
                EXIT(f'UP {mid} 的专栏为 none')
            print('获取完毕')
            return article_list
        for art in j['data']['articles']:
            article_id = art['id']
            article_list.append(article_id)
        pn += 1


# https://www.bilibili.com/read/cv6426773
def set_article_url(art_id_list, to='1', rotate=None, mid=None):
    article_url_list = []
    if mid:
        up = f'https://space.bilibili.com/{mid}/article'
        r_up = requests.get(up, headers=headers)
        text = r_up.content.decode()
        up_name = re.findall(r'<title>(.*)的个人空间', text)[0]
    
    if rotate in ['y','Y']:
        art_id_list = art_id_list[::-1]
    if type(to) == int or to.isalnum():
        to = int(to)
        if to >len(art_id_list):
            to = len(art_id_list)
        art_id_list = art_id_list[:to]
    else:
        to = 1
        art_id_list = art_id_list[:to]
        
    for art_id in art_id_list:
        url = f"https://www.bilibili.com/read/cv{art_id}"
        article_url_list.append(url)
    return article_url_list, up_name


def get_img_url(art_url_list):
    img_url_dict ={}
    for art in art_url_list:
        img_url_list = []
        res = requests.get(art, headers=headers)
        con = res.content.decode()
        title = re.findall(r'<h1 class="title">(.*?)</h1>', con)[0]
        t = re.findall(r'url.*?"https:(//i0.hdslb.com/bfs/article/.*?[j|p][p|n][g])', con)
        url = re.findall(r'<img data-src="(//i0.hdslb.com/bfs/article/.*?[j|p][p|n][g])"', con)
        url.extend(t)
        img_url_list.extend(url)
        img_url_dict[title] = img_url_list
        print(img_url_dict)
    print(img_url_dict)
    return img_url_dict


def preserve_img(urls,up_name='', title=''):
    if not os.path.isdir(path):os.mkdir(path)
    p = path + up_name +'\\'
    print(path,p)
    if not os.path.isdir(p):os.mkdir(p)
    
    for title in urls:
        art_path = p + title +'\\'
        if not os.path.isdir(art_path):os.mkdir(art_path)
        for img in urls[title]:
            if img[:4] != 'http':
                img = 'http:'+img
            img_file = art_path + img.split('/')[-1]
            if os.path.isfile(img_file):
                print(f'文件 {img_file} 以存在')
                continue
            res = requests.get(img, headers=headers)
            with open(img_file, 'wb') as f:
                f.write(res.content)
                print('文件 '+ img.split('/')[-1] +' 保存成功')
    print('全部图片保存完毕')

def EXIT(a='', n=1):
    print(a)
    time.sleep(n)
    exit()
if __name__ =="__main__":
    id_ = input('输入Up 的ID\n或输入 url=专栏链接\nurl=https://www.bilibili.com/read/cv5210011\n----------------------:')
    art = up_id(id_)
    print(f'Up --{id_}-- 共有专栏 {len(art)} 篇')
    n = input('输入爬取的篇数(默认只爬取一篇)：')
    rot  = input('是否重UP的第一篇开始爬取(默认爬取最新篇)[ y / n ]:')
    art_urls, up_name = set_article_url(art,n,rot,id_)
    imgs = get_img_url(art_urls)
    preserve_img(imgs, up_name)
    # input()
    EXIT('程序退出',2)

