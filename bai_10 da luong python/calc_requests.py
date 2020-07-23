# 1 luong cam dong ho ra bam, du 60s no bao nghi thoi
# 1 luong con lai cu cam dau vao chay, khi nao luong kia bao nghi thi nghi thoai
# luong chay se dem va update so luong request vao bien global
import threading
import time
import requests

global is_stop
is_stop=False

global count_rq
count_rq=0

global count_rq_success
count_rq_success=0



class myThread_request(threading.Thread):
    
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name=name
    def run(self):
        global is_stop
        global count_rq
        global count_rq_success

        while(not is_stop):
            # res=requests.get('http://google.com')
            res=requests.get('https://nha.chotot.com/toan-quoc/mua-ban-bat-dong-san?page=2')
            if res.status_code==200:
                count_rq_success+=1
            count_rq+=1

class myThread_time(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name=name
    def run(self):
        global is_stop

        time.sleep(60)#sleep 60s
        is_stop=True

print('is_stop',is_stop)

thread1=myThread_request('thread1')
thread2=myThread_time('thread2')

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('is_stop',is_stop)
print('count_rq',count_rq)
print('count_rq_success',count_rq_success)
