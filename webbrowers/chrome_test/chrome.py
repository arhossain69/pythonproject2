from selenium import webdriver
import time

class   chrome_config():
        def chrome_test(self):
            driver = webdriver.Chrome(executable_path="/Users/mdismailhossain/PycharmProjects/pythonProject2/Drivers/chromedriver")

            driver.maximize_window()

            driver.get("https://apple.com")
            time.sleep(5)

            title = driver.title
            print(title)

            url = driver.current_url
            print(url)

            driver.back()
            print(title)

            driver.forward()
            print(title)



obj_test = chrome_config()
obj_test.chrome_test()