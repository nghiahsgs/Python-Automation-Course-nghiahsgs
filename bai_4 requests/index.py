#ref https://realpython.com/python-requests/
import requests
import io
#luu file
def writeHTMLfile(data):
	file=io.open('code.html','w',encoding='utf-8')
	file.write(data)
	file.close()
	
res=requests.get('https://www.youtube.com/results?search_query=nghiahsgs')
writeHTMLfile(res.text)

#demo 1 => get requests
'''
response=requests.get('https://api.github.com')
print('response.status_code',response.status_code)
print(response.json()['current_user_url'])

print('headers',response.headers['Content-Type'])
'''
#demo 2 => add params (query string)
'''
#response=requests.get('https://api.github.com/search/repositories?q=requests+language:python')

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

print('total_count',response.json()['total_count'])
#https://api.github.com/search/repositories

'''
#demo 3: thay doi request header
'''
import requests

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json',
	
	},
)

# View the new `text-matches` array which provides information
# about your search term within the results
json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')
'''

#demo 4: POST data form
'''
response=requests.post('https://httpbin.org/post', data={'name':'nghia','age':20})
print(response.text)
'''

#demo 5: POST data json
'''response = requests.post('https://httpbin.org/post', json={'name':'nghia','age':20})
print(response.text)
'''
#proxy
#fake ip => fake ip ca may
#fake ip qua proxy

proxies = {
	"http": 'http://operator:operator@113.161.210.88:1080/', 
    "https": 'http://operator:operator@113.161.210.88:1080/'
 }


response=requests.get('https://api.myip.com',proxies=proxies)
print(response.json())
myip=response.json()['ip']
print(myip)


