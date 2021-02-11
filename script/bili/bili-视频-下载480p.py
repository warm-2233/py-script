# -*- coding: utf-8 -*-

import os
import re
import sys
import time
import requests

# https://m.bilibili.com/video/BV1PV411k7yh
# https://www.bilibili.com/video/BV1PV411k7yh

def get_video_url(bv_av):
    try:
        url = 'https://m.bilibili.com/video/{}'.format(bv_av)
        print(url)
        res = requests.get(url, headers=headers)
        con = res.content.decode()
        t = re.findall(r'<title data-vue-meta="true">(.*)_哔哩哔哩.*</title>', con)[0]
        r = r"video_url: '(.*000000)"
        html = re.findall(r,con)
        html = 'http:' + html[0]
        return html, t
    except:
        print('获取失败')
        sys.exit()

def downloader(url, path):
    try:
        if not os.path.isdir(path):
            print('*-**********')
            os.mkdir(path)
        v_file = path + t + bv + '.mp4'
        if os.path.isfile(path):
            print('文件存在')
            return
        v = requests.get(url, headers=headers)
        with open(v_file, 'wb') as f:
            f.write(v.content)
            print('保存成功')
    except:
        print('获取失败')
        sys.exit()
# 入口函数
if __name__ == "__main__":
    bv = input('输入视频BV：')
    #bv = 'BV1vp4y1Q7UF'
    if bv[:4] == 'http':
        bv = re.findall('video/(.*)\??',bv)[0]
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36'
    }
    url, t = get_video_url(bv)
    path = os.getcwd() + '\\Videos\\'
    downloader(url,path)
    time.sleep(2)









    
