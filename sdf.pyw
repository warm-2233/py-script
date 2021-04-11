import time
import easygui as gui


def t_to_m(t=0.001):
    t = t*60*60
    # gui.msgbox(t)
    print(t)
    return int(t)

while 1:
    time.sleep(t_to_m(1))
    gui.msgbox("休息一下吧",)