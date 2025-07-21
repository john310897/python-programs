import threading
import time

def print_numbers(rangeLim):
    time.sleep(5)
    for i in range(rangeLim):
        print(i)

thread=threading.Thread(target=print_numbers,kwargs={'rangeLim':20})
thread.start()
# thread.join()

print("hello from the main call stack")
