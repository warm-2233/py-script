# coding:utf-8
import os
import random
import time
import json
from pykeyboard import PyKeyboard
import pyperclip
import requests

 

k = PyKeyboard()

def msg(m):
    pyperclip.copy(f'{m}')
    time.sleep(0.1)
    k.press_key(k.control_key)
    k.tap_key('v')
    k.release_key(k.control_key)
    time.sleep(0.1)
    k.tap_key(k.enter_key)


def get_con():
    r = requests.get('https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn')
    with open('a.txt','a') as f:
        f.write(r.content.decode('utf-8')+'\n')

def read_file():
    if not os.path.isfile(os.getcwd()+'/a.txt'):
        print('你需要一个 a.txt 的文件')
        time.sleep(2)
        exit()
    with open('a.txt','r') as f:
        return f.readlines()

def main():
    a = read_file()
    while True:
        msg(random.choice(a))
        # get_con()
        time.sleep(0.1)



if __name__ == '__main__':
    input('回车开始')
    for i in range(5,0,-1):
        print(i)
        time.sleep(1)
    main()
    
