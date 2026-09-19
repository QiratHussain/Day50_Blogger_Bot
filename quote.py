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

    def get_quote(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.quote")))
        random_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.faux-link")))
        random_link.click()
        time.sleep(1)
        quote = self.driver.find_element(By.CSS_SELECTOR, "textarea.quote").get_attribute("value")
        author = self.driver.find_element(By.CSS_SELECTOR, "input.author").get_attribute("value")
        time.sleep(3)
        self.driver.close()
        return quote, author