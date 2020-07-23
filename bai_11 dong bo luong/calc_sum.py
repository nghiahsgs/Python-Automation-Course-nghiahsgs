#tinh tong tat ca cac phan tu trong 1 list
# lam 1 list ghi da tinh hay chua de update
## tinh tong cac so tu 1 den 1000
# dung 10 luong de update vao bien global sum
# 1 luong check khi nao thi nen stop
import threading
import time

global sum, list_input, list_is_count, isStop
sum=0
isStop=False


list_input=list(range(1,1001)) # tinh tong tat ca cac phan tu cua list_input
list_is_count= [False]*1000# da tinh chua

class My_thread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name
        
    def run(self):
        global sum, list_input, list_is_count, isStop
        
        while not isStop:
            try:
                index=list_is_count.index(False)
                sum+=list_input[index]
                list_is_count[index]=True
            except:
                print('pass')
        
        
class My_thread_stop(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name
        
    def run(self):
        global isStop
        while(True):
            try:
                index=list_is_count.index(False)
            except:
                isStop=True
                return

            


# lock=threading.Lock()

sum_ref=(1+1000)*1000/2


list_threads=[]
nb_theads=10
#init
my_thread_stop=My_thread_stop('my_thread_stop')
for i in range(nb_theads):
    new_thread=My_thread('thread%s'%i)
    list_threads.append(new_thread)

#start
my_thread_stop.start()
for i in range(nb_theads):
    list_threads[i].start()

#join
my_thread_stop.join()
for i in range(nb_theads):
    list_threads[i].join()

# thread1=My_thread('thread1')
# thread2=My_thread('thread2')

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

print('sum',sum)
print('sum_ref',sum_ref)