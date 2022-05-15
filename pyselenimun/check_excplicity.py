from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
class checkingdate():
    def checked(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # driver=webdriver.Chrome(executable_path="F:\\python\\chromedriver\\chromedriver.exe")
        # driver.get("https://www.yatra.com/")
        driver.get("https://flight.yatra.com/air-search-ui/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=BOM&destinationCountry=IN&flight_depart_date=10%2F04%2F2022&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home&unqvaldesktop=258193728031")
        # driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']").click()
        driver.maximize_window()
        # wait=WebDriverWait(driver,10)
        # all_date=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")))\
        #     .find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        # for date in all_date:
        #     if date.get_attribute("data-date") == "10/05/2022":
        #         date.click()
        #         break
        # driver.find_element(By.XPATH,"//input[@id='BE_flight_flsearch_btn']").click()
        time.sleep(35)
        pagelength=driver.execute_script("window.scrollTo(0,document.body.scrollHeight);var pagelength=document.body.scrollHeight;return document.body.scrollHeight")
        match=False
        while match==False:
            lastcount=pagelength
            time.sleep(4)
            pagelength=driver.execute_script("window.scrollTo(0,document.body.scrollheight);var pagelength=document.body.scrollheigth;return document.body.scrollHeight")
            if lastcount== pagelength:
                match=True

        time.sleep(10)

csselem=checkingdate()
csselem.checked()
