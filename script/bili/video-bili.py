import os
import re
import json
import time
import threading
import subprocess
import requests
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}
params = {
    'from': 'search',
    'seid': '9698329271136034665'
}

def get_url(aid=''):
    if aid == '': exit()
    print('----------')
    if aid.isdecimal():
        video_url = 'https://www.bilibili.com/video/av' + aid
        av_bv = 'AV'+aid
    else:
        video_url = 'https://www.bilibili.com/video/bv' + aid
        av_bv = 'BV'+aid
    print(video_url)
    res = requests.get(video_url, headers=headers)
    html = res.content.decode()
    title = re.findall(r'<title data-vue-meta="true">(.+)_哔哩哔哩.*</title>', html)[0]
    dict_info = json.loads(re.findall(r'<script>window\.__playinfo__=(.*?)</script>', html)[0])
    video = dict_info['data']['dash']['video'][0]['baseUrl']
    audio = dict_info['data']['dash']['audio'][0]['baseUrl']
    # headers.update({"Referer": video_url})
    # headers['Range'] = 'bytes=' + str(0) + '-'
    headers['Referer'] = video_url
    headers['Range'] = 'bytes=0-'
    return aid, title, video, audio, av_bv

def get_video(video, aid):
    v_res = requests.get(video, headers=headers)
    print('video', v_res.url)
    with open(aid+'.mp4','wb') as f:
        f.write(v_res.content)
        print('video 下载完成')

def get_audio(audio, aid):
    a_res = requests.get(audio, headers=headers)
    print('audio', a_res.url)
    with open(aid+'.mp3','wb') as f:
        f.write(a_res.content)
        print('audio 下载完成')

def write_va(aid, av_bv, title):
    command = f'ffmpeg -i "{aid}.mp4" -i "{aid}.mp3" -c copy "{title}_{av_bv}.mp4" -y -loglevel quiet'
    print('合并音视频')
    subprocess.Popen(command, shell=True)
    time.sleep(4)
    print('删除临时文件')
    os.remove(aid+'.mp4')
    os.remove(aid+'.mp3')
    
def main():
    av = input('输入bv/av (不要带av/bv前缀) :')
    aid, title, video, audio, av_bv = get_url(av)
    v = threading.Thread(target=get_video, args=[video, aid])
    v.start()
    a = threading.Thread(target=get_audio, args=[audio, aid])
    a.start()
    v.join()
    a.join()
    write_va(aid, av_bv, title)
    time.sleep(1)
    print('视频下载完成')
if __name__ == '__main__':
    '''调用主函数'''
    main()
    time.sleep(3)
    
    
    
    
    
    
    
    
    
    
    