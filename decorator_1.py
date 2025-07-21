import threading
import time

def pass_to_thread(func):
    def wrapper(*args,**kwargs):
        thread=threading.Thread(target=func,args=args,kwargs=kwargs)
        thread.start()
    return wrapper

@pass_to_thread
def print_numbers(limit):
    time.sleep(5)
    for i in range(limit):
        print(i)

print_numbers(20)
print("hello from main stack")
