from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from api.models import Conferencia, Ponente, Ponente_Conferencia


class PonenciasViewsTests(StaticLiveServerTestCase):

    def setUp(self):
        #Load base test functionality for decide
        ponente1=Ponente.objects.create(nombre="ponente1",apellidos="apellidos",especialidades="Ninguna",telefono="666666666")
        conferencia1=Conferencia.objects.create(tema="tema1",fecha="2022-12-24 12:00",espacio="espacio1",aforo_max="10",n_asistentes="5")
        conferencia2=Conferencia.objects.create(tema="tema2",fecha="2022-12-24 12:00",espacio="espacio2",aforo_max="10",n_asistentes="5")
        Ponente_Conferencia.objects.create(ponente=ponente1,conferencia=conferencia1)
        Ponente_Conferencia.objects.create(ponente=ponente1,conferencia=conferencia2)
        
        options = webdriver.ChromeOptions()
        options.headless = False
        self.driver = webdriver.Chrome(options=options)

        super(PonenciasViewsTests, self).setUp()           
            
    def tearDown(self):           
        self.driver.quit()
        super(PonenciasViewsTests, self).tearDown()
  
    def test_ponenciasviews(self):
        driver = self.driver
        driver.get(f'{self.live_server_url}')
        #self.driver.get(f'{self.live_server_url}/')
        driver.set_window_size(1152, 824)
        driver.find_element(By.LINK_TEXT, "Ponencias").click()
        ponencias = self.driver.find_elements(By.TAG_NAME, "tr")
        for ponencia in ponencias:
            atributos = ponencia.find_elements(By.TAG_NAME, "td")
            #self.assert_(len(atributos)==6)
        driver.find_element(By.CSS_SELECTOR, "td:nth-child(2)").click()
        atributos = self.driver.find_elements(By.TAG_NAME, "tr")
        self.assert_(len(atributos)==6)
        tema = atributos[0].find_element(By.TAG_NAME, "td")
        self.assert_("tema1" in tema.text)
        ponente = atributos[1].find_element(By.TAG_NAME, "td")
        self.assert_("ponente1" in ponente.text)
        fecha = atributos[2].find_element(By.TAG_NAME, "td")
        self.assert_("Dec. 24, 2022, noon" in fecha.text)
        espacio = atributos[3].find_element(By.TAG_NAME, "td")
        self.assert_("espacio1" in espacio.text)
        aforo_max = atributos[4].find_element(By.TAG_NAME, "td")
        self.assert_(aforo_max.text=="10")
        n_asistentes = atributos[5].find_element(By.TAG_NAME, "td")
        self.assert_(n_asistentes.text=="5")
