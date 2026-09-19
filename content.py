from seleniumbase import Driver
from selenium.webdriver.common.by import By
import time


class ai_manager:
    def __init__(self):
        self.url= "https://chatgpt.com/"

    def goto_site(self):
        try:
            self.driver=Driver(uc=True )
            self.driver.get(self.url)
            time.sleep(20)
        except Exception as e:
            print(e)

    def content_prompt(self,quote, author):
        promp_input= self.driver.find_element(By.CSS_SELECTOR,"#mobile-composer-prompt")
        promp_input.click()
        promp_input.send_keys(f'''
        write 3 human written paragraphed text article in which you add {quote}, make sure you do mention that quote is by {author} inside the article that, and don't write other stuff inside the message so that i can just copy your message and paste on my blog, just send me pastable, and please dont write stuff like here's the paragraph,or in end that you say do you also want or something blah blah that you do, just article to the point that i can copy, i mean it
        ''')
        time.sleep(60)