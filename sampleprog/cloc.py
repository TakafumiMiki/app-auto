import time

try:
    while True:
        time.sleep(1)
        print((int(time.clock())))
        #print(time.time())
        #print(int(time.time()))

except KeyboardInterrupt:
    print("終わり")