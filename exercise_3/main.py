import threading
import time
import random

def main():
    
    for in in range
    t1 = threading.Thread(target=greet_sleep_farewell,args=(1,))
    t2 = threading.Thread(target=greet_sleep_farewell,args=(2,))
    t3 = threading.Thread(target=greet_sleep_farewell,args=(3,))
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    
def greet_sleep_farewell(id):
        
    print('Hi!, Im thread {}'.format(id))
    time.sleep(random.randint(1,10))
    print('thread {} is saying you goodbye!'.format(id))
         
         
if __name__ == "__main__":
    main()