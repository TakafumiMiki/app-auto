import pyautogui as pg
print('中断するにはCtrl-Cを押してください。')

try:
    while True:
        x, y = pg.position()
        position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(position_str,end='')
        print("\r", end='', flush=True) 

except KeyboardInterrupt:
    print('\n終わり')