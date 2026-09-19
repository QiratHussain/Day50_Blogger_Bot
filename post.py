from seleniumbase import Driver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import dotenv
dotenv.load_dotenv()

class PostManager:
    def __init__(self):
        self.url="https://www.blogger.com/about/?bpli=1"
        self.email= os.getenv("EMAIL")
        self.password= os.getenv("PASSWORD")

    def goto_site(self):
        self.options= Options()
        self.service= Service(ChromeDriverManager().install())
        self.options.add_experimental_option("detach", True)
        self.driver= Driver(uc=True, headed=True)
        self.driver.get(self.url)

    def login(self):
        time.sleep(10)
        login_button= self.driver.find_element(By.CSS_SELECTOR,"body > header > div.header--content > div.header--buttons > a.sign-in.ga-header-sign-in > span")
        login_button.click()
        time.sleep(10)
        email_input= self.driver.find_element(By.CSS_SELECTOR,"#identifierId")
        email_input.click()
        email_input.send_keys(self.email, Keys.ENTER)
        time.sleep(5)
        self.wait= WebDriverWait(self.driver, 3)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")))
        password_input= self.driver.find_element(By.CSS_SELECTOR,"#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
        password_input.send_keys(self.password,Keys.ENTER)
        time.sleep(10)