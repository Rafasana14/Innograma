from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from api.models import Ponente

class PonentesViews(StaticLiveServerTestCase):

    def setUp(self):
        Ponente.objects.create(id=1,nombre="ivamorgra",apellidos="mor gra",especialidades="python",conferencias_impartidas="python",empresa="Django",correo="ivamorgra@python.com",telefono="123456789",otras_formas_de_contacto="LinkedIn: Iván Moreno Granado")
        Ponente.objects.create(nombre="ivamorgraToUpdate",apellidos="morup gradate",especialidades="python",conferencias_impartidas="python",empresa="Django",correo="ivamorgratoupdate@python.com",telefono="223456789",otras_formas_de_contacto="LinkedIn: Iván Moreno Granado")
        
        options = webdriver.ChromeOptions()
        options.headless = False
        self.driver = webdriver.Chrome(options=options)
        #super().setup()

    def teardown(self):
        self.driver.quit()
        super().teardown()

    
    def test_ponentes(self):
        self.driver.get(f'{self.live_server_url}/ponentes')
        self.assertTrue(len(self.driver.find_elements(By.ID,'ponente'))==14)

    
    def test_ponentes_detail(self):
        self.driver.get(f'{self.live_server_url}/ponentes/1')
        print(len(self.driver.find_elements(By.ID,'ponente')))
        self.assertTrue(len(self.driver.find_elements(By.ID,'ponente'))==8)
    
   