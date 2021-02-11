# coding: utf-8

import os
import re
import sys
import json
import time

import requests
import html2text
from bs4 import BeautifulSoup

path = "imgs"
headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45"
}



def EXIT(a='', n=0.5):
    print(a)
    time.sleep(n)
    exit()
    

class UP_Article:
    def __init__(self, id):
        self.id = self.is_id(id)
        self.all_article_url()
        self.url = self.all_srticle_list[0]
        
        
    def exit(self, msg='', t=0.5):
        print(msg)
        time.sleep(t)
        sys.exit()
        
        
    def is_id(self, id):
        if type(id) == str:
            if id.isdecimal():
                return int(id)
            else:
                self.exit("up id 输入 有误")
        elif type(id) == int:
            return id
        else:
            return int(id)
            
            
    def all_article_url(self):
        self.all_article_list = []
        pn = 1
        while True:
            url = f"https://api.bilibili.com/x/space/article?mid={self.id}&pn={pn}"
            res = requests.get(url, headers=headers)
            txt = json.loads(res.text)
            if txt.get('code') == 0:
                articles = txt.get("data").get("articles")
                if articles:
                    for art in articles:
                        self.all_article_list.append(f"https://www.bilibili.com/read/cv{art.get('id')}")
                        # print(art)
                else:
                    if not self.all_article_list:
                        self.exit("这个up好像没有写专栏")
                    print("有", len(self.all_article_list), "条专栏")
                    print(self.all_article_list)
                    break
                
            pn += 1
    

    @staticmethod
    def get_up_article_to_markdown(url):
        # print(url)
        res = requests.get(url, headers=headers)
        html = res.text

        title = re.findall(r'<h1 class="title">(.*)</h1>', html)[0]
        title = re.sub(r"[\/\\\:\*\?\"\<\>\|]", '', title)
        global path
        path = title + '/' + path
        if not os.path.isdir(path):
            os.makedirs(path)

        header_img = re.findall(r'<meta itemprop="image" content="(.*)">', html)
        if header_img:
            length = len(header_img)
            name = []
            for u in range(length):
                r = requests.get(header_img[u], headers=headers).content
                fn = path + "/head_" + str(u) + ".jpg"
                name.append(f"./imgs/head_{u}.jpg")
                with open(fn, "wb") as i:
                    i.write(r)
            header = ""
            for h in name:
                header += f"![{h}]({h})"
                # print(header)

        c = re.findall(r'<div class="article-holder">.*</div>', html)[0]

        img_url_list = []
        url_img = re.findall(r'<img data-src="(//i0.hdslb.com/bfs/article/.*?[j|p|g][p|n|i][g|f])"', c)
        img_url_list.extend(url_img)
        if img_url_list:
            length = len(img_url_list)
            for i in range(length):
                u = img_url_list[i] if img_url_list[i][:4] == "http" else "http:"+img_url_list[i]
                img_path = f"{path}/{i}.jpg"
                if os.path.isfile(img_path):
                    continue
                img = requests.get(u, headers=headers).content
                with open(img_path, "wb") as file:
                    file.write(img)
        # print(img_url_list)

        t = re.findall(r'<img data-src="//i0\.hdslb\.com.*?/>', c)
        # print(t)
        for i in range(len(t)):
            c = c.replace(t[i], f'<img alt="./imgs/{i}.jpg" src="./imgs/{i}.jpg" />')


        md = html2text.html2text(c)
        with open(f"{title}/{title}.md", "w", encoding="utf-8") as f:
            # print(md, type(md))
            markdown = f'{header}\n\n# {title}\n\n{md}\n\n\n{f"[原文链接]({url})"}\n\n'
            f.write(markdown)
        
        
        
        
        
        



def main():
#     id_ = input('''......................................
# ---- 输入Up 的ID
# ---- 或输入 url=专栏链接
# ---- 例：url=https://www.bilibili.com/read/cv5210011
# **********************:''')

    if l:=len(sys.argv) == 1:
        u = input("输入专栏链接，https://www.bilibili.com/read/cv2233")
    elif l == 2:
        u = sys.argv[1]
    else:
        print("参数错误")
        sys.exit()

    UP_Article.get_up_article_to_markdown(u)
    
if __name__ =="__main__":
    main()

