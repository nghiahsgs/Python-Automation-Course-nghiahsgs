
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time
import urllib
import requests
import shutil

def initDriver(filePath):
	chrome_options = webdriver.ChromeOptions()
	#config open chrome theo specific path
	chrome_options.add_argument(
		"user-data-dir="+filePath) #chrome profile
	#config ko load anh
	
	prefs = {
	"profile.managed_default_content_settings.images": 2
	}
	chrome_options.add_experimental_option("prefs", prefs)
	
	driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
	return driver

def ham_download_image_gg(filePath,folder_save,keyword,number_scroll):
	
	nameFile = "-".join(keyword.split(" "))
	
	driver=initDriver(filePath)
	
	driver.get('https://www.google.com/')
	driver.get('https://www.google.com/search?tbm=isch&q='+keyword.replace(" ","+")) ## gg anh
	time.sleep(10)

	for i in range(number_scroll):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(10)
	# print('nghiahsgs')

	#get anh base 64
    # list_elements = driver.find_elements_by_css_selector('img')
    # list_href = []
    # for image in list_elements[3:]:
    #     href = image.get_attribute('src')
    #     list_href.append(href)

	#get link truc tiep cua anh
	list_elements =driver.find_elements_by_css_selector('a[jsname="hSRGPd"]')
	list_href = []
	for image in list_elements[3:]:
		href = image.get_attribute('href')
		list_href.append(href)

	print ('len(list_href)', len(list_href))

	list_src = []
    
	#dung cho anh base 64
	# pos = 0
    # for href in list_href:
    #     print(pos,href)
    #     try:
    #         kq=base64.b64decode(href.replace('data:image/jpeg;base64,',''))
    #         f=open(r'%s\%s.jpg'%(result_dir,nameFile+'-'+str(pos)),'wb')
            
    #         f.write(kq)
    #         f.close()
            

    #     except:
    #         try:
    #             downloadImg(href, nameFile+'-'+str(pos), result_dir)
    #         except:
    #             print("error at %s" % pos)


    #     pos += 1

	#tach url ra tu chuoi query string va download (url decode)
	pos = 0
	for href in list_href:
		print(pos,href)
		try:
			href=urllib.parse.parse_qs(href)
			href=href['https://www.google.com/imgres?imgurl'][0]
			print('href',href)
			# input('nghiahsgs')
			downloadImg(href, nameFile+'-'+str(pos), folder_save)
		except:
			print("error at %s" % pos)
		pos += 1

def downloadImg(url, nameFile, result_dir):
	try:
		response = requests.get(url, stream = True,timeout=10)
		with open(r'%s\%s.jpg' % (result_dir,nameFile), 'wb') as out_file:
			shutil.copyfileobj(response.raw, out_file)
		del response
	except:
		print("error downloadImg")

filePath='chrome'
folder_save='image'
keyword='messi'
number_scroll=1
ham_download_image_gg(filePath,folder_save,keyword,number_scroll)	
