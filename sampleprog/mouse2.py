import pyautogui as pg
from time import clock,sleep
print('中断するにはCtrl+Cを押してください。')

try:
    count = 0
    x1 = 0
    y1 = 0
    file1 = open("log.txt","w") 
    while True:
        x, y = pg.position()
        position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        sleep(1)
        if(int(clock())%3 == 0):
            x1 += x
            y1 += y    
            file1.write(position_str + "\n")
            count += 1
        if(count == 20):
            file1.write("平均 x:%d,y:%d"%(x1/count,y1/count))
            break
except KeyboardInterrupt:
    print("x1 = %d :y1 = %d"%(x1,y1))
    print("おわり %d回"%count)