from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



class SesionTests(StaticLiveServerTestCase):

    def setUp(self):
        
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')

        super(SesionTests, self).setUp()           
            
    def tearDown(self):           
        self.driver.quit()
        super(SesionTests, self).tearDown()
        
    def test_login(self):
        self.driver.get(f'{self.live_server_url}')
        self.driver.find_element(By.LINK_TEXT, "Acceso Administrador").click()
        self.driver.find_element(By.ID, "id_username").send_keys("admin")
        self.driver.find_element(By.ID, "id_password").send_keys("admin",Keys.ENTER)
        self.assertTrue(len(self.driver.find_elements(By.LINK_TEXT,"Cerrar Sesión"))==1)
        
    def test_logout(self):

        self.driver.get(f'{self.live_server_url}')
        self.driver.find_element(By.LINK_TEXT, "Acceso Administrador").click()
        self.driver.find_element(By.ID, "id_username").send_keys("admin")
        self.driver.find_element(By.ID, "id_password").send_keys("admin",Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT, "Cerrar Sesión").click()
        self.assertTrue(len(self.driver.find_elements(By.LINK_TEXT,"Acceso Administrador"))==1)
        