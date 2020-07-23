import threading
import time

class myThread(threading.Thread):
    def __init__(self, name, counter, delay):
        threading.Thread.__init__(self)
        self.name=name
        self.counter=counter
        self.delay=delay
    def run(self):
        print('ready to run', self.name)

        while(self.counter):
            time.sleep(self.delay)
            print('%s : %s'%(self.name, time.ctime(time.time())))
            self.counter-=1

try:
    threads=[]
    thread1 = myThread('thread1',5,2)
    thread2 = myThread('thread2',5,3)
    
    threads.append(thread1)
    threads.append(thread2)
    
    thread1.start()
    thread2.start()

    for t in threads:
        t.join()
    print('end all threads')


except:
    pass