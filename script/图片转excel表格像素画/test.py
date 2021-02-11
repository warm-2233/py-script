'''
import xlsxwriter

wb = xlsxwriter.Workbook('test.xlsx')
ws = wb.add_worksheet('test')

ws.set_row(0,10)
ws.set_column(0,1,1)



wb.close()

from PIL import Image


img = Image.open("warma.jpg")
print(img)
print(img.size)
print("===========================")
imgL = img.convert("P").convert("RGB")
pix = imgL.load()
w, h = imgL.size

print(imgL)
print(pix)
print(w, h)
'''


def RGB_to_Hex(tmp):
    rgb = list(tmp)
    strs = '#'
    for i in rgb:
        num = int(i)
        strs += str(hex(num))[-2:].replace('x','0').upper()
    return strs


print(RGB_to_Hex((255, 255, 255)))





