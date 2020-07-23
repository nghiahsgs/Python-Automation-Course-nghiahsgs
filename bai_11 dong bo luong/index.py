# 2 luong cung vao rut tien 1 tai khoan
# dung lock de khoa luong lai, luong 2 cho luong 1 rut xong moi cho vao
import threading
import time

class My_Thread(threading.Thread):
    def __init__(self, name,account, amount):
        threading.Thread.__init__(self)
        self.name=name
        self.account=account
        self.amount=amount
    def run(self):
        lock.acquire()

        print('running %s'%self.name)
        withDraw(self.account, self.amount)    

        lock.release()

class Account():
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance

# moi lan goi ham nay
# account se dc rut 10 lan
def withDraw(account, amount):
    
    for i in range(10):
        if account.balance>= amount:
            account.balance-=amount
            print('so du tai khoan %s'% account.balance)
        else:
            print('tai khoan %s da het tien'% account.name)
        
        time.sleep(0.2)
    

account1=Account('test account 1',1000)
lock=threading.Lock()

# t1=threading.Thread(target=withDraw, args=(account1,100))
# t2=threading.Thread(target=withDraw, args=(account1,100))

t1=My_Thread(name='t1',account=account1, amount=200)
t2=My_Thread(name='t2',account=account1, amount=200)


t1.start()
t2.start()

t1.join()
t2.join()

print('end program')