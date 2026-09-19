from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Quote:
    def __init__(self):
        self.url= "https://quozio.com/"

    def goto_site(self):
        self.options= Options()
        self.service= Service(ChromeDriverManager().install())
        self.options.add_experimental_option("detach", True)
        self.driver= webdriver.Chrome(service=self.service, options=self.options)
        self.driver.get(self.url)