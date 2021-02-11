#! ../py385/Scripts/python

import os
import sys
# 第三方包 xlsxwriter image
import xlsxwriter
from PIL import Image


def RGB_to_Hex(tp):
    rgb = list(tp)
    strs = '#'
    for i in rgb:
        num = int(i)
        strs += str(hex(num))[-2:].replace('x','0').upper()
    return strs

def img_size(img):
    while True:
        if (img.size[0]*img.size[1] > 500000):
            w, h = img.size
            w, h = int(w/1.1), int(h/1.1)
            img = img.resize((w, h),Image.ANTIALIAS)
        else:
            print("文件太大了, 宽高修改为:", *img.size)
            return img


def xlsx_img(path):
    path = os.path.join(path)
    img = Image.open(path)
    img = img_size(img)
    
    imgL = img.convert("P").convert("RGB")
    pix = imgL.load()
    w, h = imgL.size
    
    print('图片读取成功...')
    name = os.path.splitext(os.path.basename(path))[0]
    wb = xlsxwriter.Workbook(name+'.xlsx')
    ws = wb.add_worksheet(name[:31])
    print("xlsx 生成中...")
    for i in range(w):
        for j in range(h):
            rgb = pix[i,j]
            color = RGB_to_Hex(rgb)
            style = wb.add_format({'bg_color': '{}'.format(color)})
            ws.write(j,i,'',style)
            ws.set_row(j,1)
    ws.set_column(0,w-1,0.1)
    wb.close()
    print("完成")


def main():
    if len(sys.argv) == 1:
        path = input("输入图片路径:")
        if not path:
            print("\n不听话的孩子！！")
            sys.exit()
    else:
        path = sys.argv[1]
    print("请等待...")
    
    xlsx_img(path)



if __name__ == "__main__":
    main()

