import pyautogui as pg
x1,y1 = pg.position()#現在のカーソルの場所
print(x1,y1)

x2, y2 = pg.size()#ディスプレイサイズ
print(x2,y2)#1920 1080

tf = pg.onScreen(x1, y1) #ディスプレイにカーソルがあるか
print(tf)

"""
def sysexit1():
    print("マウスカーソルがメインディスプレイ内にないです")
    exit()

if pg.onScreen(x,y) is False:
    sysexit1()
"""

