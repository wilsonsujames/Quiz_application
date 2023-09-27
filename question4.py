from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.cathaybk.com.tw/cathaybk/")

driver.get_screenshot_as_file("Official_website.png")


driver.close()