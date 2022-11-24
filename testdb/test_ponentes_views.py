from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



class PonentesViews(StaticLiveServerTestCase):

    def setup(self):
        

        options = webdriver.ChromeOptions()
        options.headless = False
        self.driver = webdriver.Chrome(options=options)
        super().setup()

    def teardown(self):
        self.driver.quit()
        super().teardown()

    def test_ponentes(self):
        self.driver.get(f'{self.live_server_url}/ponentes/')
        self.assertTrue(len(self.driver.find_elements(By.ID,'ponentes'))==1)

    def test_ponentes_detail(self):
        self.driver.get(f'{self.live_server_url}/ponentes/1/')
        self.assertTrue(len(self.driver.find_elements(By.ID,'ponente'))==1)
    
    '''
    def test_ponentes_detail_not_found(self):
        self.driver.get(f'{self.live_server_url}/ponentes/100/')
        self.assertTrue(len(self.driver.find_elements(By.ID,'ponente'))==0)
    '''
    '''
    def test_simpleCorrectLogin(self):                    
        self.driver.get(f'{self.live_server_url}/admin/')
        self.driver.find_element(By.ID,'id_username').send_keys("admin")
        self.driver.find_element(By.ID,'id_password').send_keys("qwerty",Keys.ENTER)
        
        print(self.driver.current_url)
        #In case of a correct loging, a element with id 'user-tools' is shown in the upper right part
        self.assertTrue(len(self.driver.find_elements(By.ID,'user-tools'))==1)
    '''