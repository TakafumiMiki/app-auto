import pyautogui as pg
from time import clock,sleep
print('中断するにはCtrl+Cを押してください。')

try:
    count = 0
    file1 = open("log.txt","w") 
    while True:
        x, y = pg.position()
        position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        sleep(1)
        if(int(clock())%3 == 0):    
            file1.write(position_str + "\n")
            count += 1
        if(count == 20):
            break
except KeyboardInterrupt:
    print("おわり %d回"%count)