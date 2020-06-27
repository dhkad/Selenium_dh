from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get('https://www.wikipedia.org/')

# find the english lang and click on it
en_box = driver.find_element_by_id('js-link-box-en')
en_box.click()

# we will use implicit wait until the even is finished
wait = W(driver, 5)
search_dh = wait.until(EC.presence_of_element_located((By.NAME, "search")))

# send software to search textbox and get this value and then press enter
search_dh.send_keys("software")
print(search_dh.get_attribute('value'))
search_dh.submit()

driver.quit()
