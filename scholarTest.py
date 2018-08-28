from selenium import webdriver
import time

if __name__ == "__main__":
	driver = webdriver.Chrome()
	url  = "https://scholar.google.com/scholar?q=%22Anne+M.+Brown%22&hl=en&as_sdt=0%2C47&as_ylo=2010&as_yhi="
	driver.get(url)
	buttons = driver.find_elements_by_class_name('gs_or_cit')
	
	for button in buttons:
		button.click()
		time.sleep(.5)
		print(driver.find_elements_by_class_name("gs_citr")[2].text)
		time.sleep(.5)
		driver.find_elements_by_class_name("gs_ico")[0].click()
		time.sleep(.5)
		print("********************************")
