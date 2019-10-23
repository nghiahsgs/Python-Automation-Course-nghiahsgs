import requests
# proxies = {
#     "http": 'http://nghiahsgs:679701@p1.vietpn.co:1808/', 
#     "https": 'http://nghiahsgs:679701@p1.vietpn.co:1808/'
#  }
proxies = {
	"http": 'http://operator:operator@113.161.210.88:1080/', 
    "https": 'http://operator:operator@113.161.210.88:1080/'
 }

#response=requests.get('https://httpbin.org/ip',proxies={"http": proxy, "https": proxy})
#response=requests.get('https://httpbin.org/ip',proxies=proxies)


response=requests.get('https://api.myip.com',proxies=proxies)
print(response.json())
myip=response.json()['ip']
print(myip)
#http://ipinfo.io/json
response=requests.get('http://ip-api.com/json/'+myip,proxies=proxies)
print(response.json())


# response=requests.get('http://ipinfo.io/json',proxies=proxies)
# print(response.json())

# import requests
# url = 'https://httpbin.org/ip'
# # proxies = {
# #     "http": 'http://209.50.52.162:9050', 
# #     "https": 'http://209.50.52.162:9050'
# # }
# proxies=""
# response = requests.get(url,proxies=proxies)
# print(response.json())


# import requests
# from lxml.html import fromstring
# from itertools import cycle
# #import traceback

# def get_proxies():
#     url = 'https://free-proxy-list.net/'
#     response = requests.get(url)
#     parser = fromstring(response.text)
#     proxies = set()
#     for i in parser.xpath('//tbody/tr')[:10]:
#         if i.xpath('.//td[7][contains(text(),"yes")]'):
#             #Grabbing IP and corresponding PORT
#             proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
#             proxies.add(proxy)
#     return proxies

# # kq=get_proxies()
# # print(kq)

# for iChay in range(3):
# 	print("lan chay thu",iChay)
# 	#If you are copy pasting proxy ips, put in the list below
# 	#proxies = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']

# 	proxies = get_proxies()
# 	print(proxies)
# 	proxy_pool = cycle(proxies)

# 	url = 'https://httpbin.org/ip'
# 	#for i in range(1,11):
# 	for i in range(len(proxies)):
# 	    #Get a proxy from the pool
# 	    proxy = next(proxy_pool)
# 	    print("Request #%d"%i)
# 	    try:
# 	        response = requests.get(url,proxies={"http": proxy, "https": proxy})
# 	        print(response.json())
# 	    except:
# 	        #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
# 	        #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
# 	        print("Skipping. Connnection error")