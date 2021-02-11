import os
import sys
import re
import json
import time
import platform

if platform.system() == "Windows":
    root_path = os.getcwd() + "\\download\\"
else:
    root_path = "/storage/emulated/0/android/data/tv.danmaku.bili/download/"


def read_dir(root):
    path_list = os.listdir(root)

    for path in path_list:
        a = root_path + path + "/"
        if not os.path.isdir(a):continue
        a = os.listdir(a)
        for p in a:
            b = root_path + path + "/" + p + "/"
            if os.path.isfile(b+"entry.json"):
                with open(b+"entry.json",encoding="utf-8") as f:
                    f = f.read()
                j = json.loads(f)
                # title = str(j.get("page_data").get("part")) + "-" + str(j.get("avid"))
                title = str(j.get("title"))+ str(p) + "-av" + str(j.get("avid"))
                title = re.sub('[\/:*?"<>|]','',title)
                # print(title,p)
            b = os.listdir(b)
            for i in b:
                c = root_path + path + "/" + p + "/" +i
                if os.path.isdir(c):
                    os.chdir(c)
                    os.system(f'ffmpeg -i "video.m4s" -i "audio.m4s" -codec copy "{title}.mp4" -y -loglevel quiet')
                    
                    # time.sleep(1)
                    v = os.getcwd()+"/"+title+".mp4"
                    f = open(v,"rb")
                    t = open(root_path+title+".mp4", "wb")
                    t.write(f.read())
                    f.close()
                    t.close()
                    os.remove(v)
                    
                    
            
            # entry.json


read_dir(root_path)
