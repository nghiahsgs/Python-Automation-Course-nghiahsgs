#ref : https://sebastianraschka.com/Articles/2014_multiprocessing.html#the-pool-class
from multiprocessing import Pool
import time
#work = (["A", 5], ["B", 2], ["C", 1], ["D", 3])

def cube(x):
	#print(x)
	#time.sleep(random.randint(0,3))
	time.sleep(3)
	#time.sleep(6-x)
	return x**3

def sum(list_para):
	x=list_para[0]
	y=list_para[1]
	#print(x)
	#time.sleep(random.randint(0,3))
	#time.sleep(3)
	#time.sleep(6-x)
	return x+y

def pool_handler():
	p = Pool(2)
	#kq=p.map(cube, range(1,7))
	#kq=p.map(cube, ([1,3],2))
	#kq=p.map_async(cube, (1,2,3)) #=> ko block main
	#kq2=p.map_async(cube, (4,5,6))
	

	
	# <=> kq2=p.map_async(cube, (1,2,3,4,5,6))
	
	#vd 2: pass multi para (tricky)
	kq=p.map_async(sum, ([1,2],[3,4],[4,5]))
	print('nghiahsgs')

	print(kq.get()) #khi chay ham nay => block
	#The Pool.map and Pool.apply will lock the main program until all processes are finished, which is quite useful if we want to obtain results in a particular order for certain applications.
	p.close()
	p.join()
	print('Task ended. Pool join.')


if __name__ == '__main__':
    pool_handler()
