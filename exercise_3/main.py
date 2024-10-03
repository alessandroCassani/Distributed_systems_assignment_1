import threading
import time
import random

def main():
    
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
    sleeping_time = random.randint(1,10)
    time.sleep(sleeping_time)
    print('thread {} is saying you goodbye after sleeping for {} seconds!'.format(id, sleeping_time))
         
         
if __name__ == "__main__":
    main()