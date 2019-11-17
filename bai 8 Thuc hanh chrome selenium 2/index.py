
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

def initDriver(filePath):
	chrome_options = webdriver.ChromeOptions()
	#config open chrome theo specific path
	chrome_options.add_argument(
		"user-data-dir="+filePath) #chrome profile
	#config ko load anh
	'''
	prefs = {
	"profile.managed_default_content_settings.images": 2
	}
	chrome_options.add_experimental_option("prefs", prefs)
	'''
	driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
	return driver

def ham_surf_face(filePath):
	
	driver=initDriver(filePath)
	driver.get('https://www.facebook.com/') #da co nick fb login san roi
	#wait khi story xuat hien <=> load success
	WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#stories_tray")))
	time.sleep(2)
	count_eles_btn_like=0

	while(True):
		#scroll down
		driver.execute_script("window.scrollBy(0,0.7*window.innerHeight)")
		time.sleep(2)

		eles_btn_like=driver.find_elements_by_css_selector('div[data-testid="UFI2ReactionLink/actionLink"] a') #selector cua nut like
		count_eles_btn_like=len(eles_btn_like)
		#eles_btn_like[0].click()
		print(count_eles_btn_like)

filePath='chrome2'
ham_surf_face(filePath)	
