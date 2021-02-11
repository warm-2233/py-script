# coding: utf-8

import os
import re
import json
import time
import requests as req

def get_req(url):
    res = req.get(url, headers=headers)
    return res 

headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45"
}

# https://api.bilibili.com/x/space/article?mid=166559060&pn=1
def up_id(mid):
    article_list = []
    pn = 1
    if type(mid) == str:
        if not mid.isdecimal():
            EXIT('id 必须是数字')
    while True:
        url = "https://api.bilibili.com/x/space/article?mid={}&pn={}".format(mid, pn)
        
        res = get_req(url)
        j = json.loads(res.text)
        if not j.get('data').get('articles'):
            if not article_list:
                EXIT('ID {} UP 的专栏为 none'.format(mid))
            print('获取完毕')
            print('UP {} 共有专栏 {} 篇'.format(upName, len(article_list)))
            return article_list, upName
        upName = j.get('data').get('articles')[0].get('author').get('name')
        for art in j['data']['articles']:
            article_id = art['id']
            article_list.append(article_id)
        pn += 1
        
# https://www.bilibili.com/read/cv6426773
def set_article_url(art_id_list, to='1', rotate=None):
    article_url_list = []
    if rotate in ['y','Y']:
        art_id_list = art_id_list[::-1]
    
    if type(to) == str:
        if to.isdecimal():
            to = int(to)
            art_id_list = art_id_list[:to]
        else:
            to = 1
            art_id_list = art_id_list[:to] 
    elif type(to) == int:
        art_id_list = art_id_list[:to]
    else:
        to = 1
        art_id_list = art_id_list[:to] 
    for art_id in art_id_list:
        url = f"https://www.bilibili.com/read/cv{art_id}"
        article_url_list.append(url)
    return article_url_list


def get_img_url(art_url_list):
    img_url_dict ={}
    for art in art_url_list:
        print('--',art)
        img_url_list = []
        res = get_req(art)
        con = res.text
        title = re.findall(r'<h1 class="title">(.*?)</h1>', con)[0]
        t = re.findall(r'url.*?"https:(//i0.hdslb.com/bfs/article/.*?[j|p][p|n][g])', con)
        url = re.findall(r'<img data-src="(//i0.hdslb.com/bfs/article/.*?[j|p][p|n][g])"', con)
        url.extend(t)
        img_url_list.extend(url)
        img_url_dict[title] = img_url_list
    return img_url_dict

def preserve_img(urls,upName=''):
    root_path = os.getcwd() + "/bilibili_up专栏_图片/"
    if not os.path.isdir(root_path):os.mkdir(root_path)
    
    path = root_path + upName +'/'
    if not os.path.isdir(path):os.mkdir(path)
    
    for title in urls:
        t = re.sub(r"[\/\\\:\*\?\"\<\>\|]", '', title)
        art_path = path + t +'/'
        if not os.path.isdir(art_path):os.mkdir(art_path)
        for img in urls[title]:
            if img[:4] != 'http':
                img = 'http:'+img
            img_file = art_path + img.split('/')[-1]
            if os.path.isfile(img_file):
                print('文件 {} 以存在'.format(img_file))
                continue
            
            res = get_req(img)
            with open(img_file, 'wb') as f:
                f.write(res.content)
                print('文件 '+ img.split('/')[-1] +' 保存成功')
    print('全部图片保存完毕')

def EXIT(a='', n=0.5):
    print(a)
    time.sleep(n)
    exit()

def main():
    id_ = input('''......................................
---- 输入Up 的ID
---- 或输入 url=专栏链接
---- 例：url=https://www.bilibili.com/read/cv5210011
**********************:''')
    if id_[:2] == 'cv':
        id_ = 'url=https://www.bilibili.com/read/' + id_

    if id_[:4] == "url=":
        # url=https://www.bilibili.com/read/cv6525566
        url = [id_[4:]]
        imgUrl = get_img_url(url)
        cv = re.findall(r'http.*(cv\d*)',url[0])[0]
        preserve_img(imgUrl)
        EXIT('保存完毕', 2)
    art , name = up_id(id_)

    rotate = input('是否从UP的第一篇开始爬取(默认爬取最新篇)[ y / n ]')
    to = input('输入爬取的篇数(默认只爬取一篇)')
    url = set_article_url(art, to, rotate)
    img = get_img_url(url)
    preserve_img(img, name)
    EXIT('程序退出',2)
    
if __name__ =="__main__":
    main()
    # print(get_req("https://pan.baidu.com/s/1EQtVkQshgDK3mr6p3xwMAw"))

