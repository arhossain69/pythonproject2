from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class webelements():
    def locator(self):
        driver = webdriver.Firefox(executable_path= "/Users/mdismailhossain/PycharmProjects/pythonProject2/Drivers/geckodriver2")


        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        username = driver.find_element(By.NAME,"username")
        username.send_keys("admin")

        password = driver.find_element(By.NAME,"password")
        password.send_keys("admin123")

        logging_button = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        logging_button.click()
        time.sleep(3)

        account = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p')
        account.click()

        myinfo = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a')
        myinfo.click()

        blood_type = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[1]')
        sel = Select(blood_type)
        sel.select_by_visible_text('A+')



obj_test = webelements()
obj_test.locator()