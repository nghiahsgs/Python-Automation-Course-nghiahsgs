from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

chrome_options = webdriver.ChromeOptions()
prefs = {
	"profile.managed_default_content_settings.images": 2
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome('./chromedriver', options = chrome_options)

#===cach click
driver.get('http://nghiahsgs.com')
#cach 1 : thuc thi js 
js_zzz="document.querySelector('.readmore').click()"
driver.execute_script(js_zzz)

#cach 2: tim phan tu bang driver
 driver.find_element_by_css_selector('.readmore').click()
#trong truong hop nhieu phan tu thi dung find_elements_by_css_selector
list_eles=driver.find_elements_by_css_selector('.readmore')
len(list_eles)
list_eles[1].click()

#===cach type
#c1: dung js
driver.get('http://google.com')
js_zzz='document.querySelector(\'input[name="q"]\').value=\'nghiahsgs\'' #dien vao input tim kiem
driver.execute_script(js_zzz)

#c2: driver
input_search=driver.find_element_by_css_selector('input[name="q"')
input_search.send_keys('anh nghia dez')
input_search.send_keys('anh nghia dep trai vcl')


#==== doi phan tu xuat hien
driver.get(url)  # http://taoanhonline.com/wp-admin/post-new.php
title_input = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#title")));
time.sleep(0.5)

