from selenium import webdrive
driver=webdriver.Chrome(executable_path="F:\\python\\chromedriver\\chromedriver.exe")
driver.get("https://www.flipkart.com")
driver.maximize_window()
#print(driver.title)
#driver.close()
