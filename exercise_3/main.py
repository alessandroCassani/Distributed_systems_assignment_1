import threading
import time
import random

def main():
    threads = []
    
    for i in range(3):
        thread = threading.Thread(target=greet_sleep_farewell,args=(i,))
        threads.append(thread)

    for thread in threads:
        thread.start()
        
    for thread in threads:
        thread.join()
        
    
def greet_sleep_farewell(id):
    print(f'Hi!, Im thread {id}')
    
    sleeping_time = random.randint(1,10)
    time.sleep(sleeping_time)
    
    print('thread {} is saying you goodbye after sleeping for {} seconds!'.format(id, sleeping_time))
         
         
if __name__ == "__main__":
    main()