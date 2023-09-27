from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.cathaybk.com.tw/cathaybk/personal/product/credit-card/cards/")

time.sleep(1)

elelist= driver.find_elements(By.CLASS_NAME, "cubre-m-anchor__btn")

print(elelist)
count = 0
for ele in elelist:
    count+=1

print(count)


driver.get_screenshot_as_file("Official_website2.png")



# driver.close()