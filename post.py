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