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
        ponente1=Ponente.objects.create(nombre="ponente1",apellidos="apellidos",especialidades="Ninguna",empresa="Empresa1",correo="ponente1@gmail.com",telefono="666666666",otras_formas_de_contacto="Ninguna")
        ponente2=Ponente.objects.create(nombre="ponente2",apellidos="apellidos",especialidades="Ninguna",empresa="Empresa2",correo="ponente2@gmail.com",telefono="666666665",otras_formas_de_contacto="Ninguna")
        pnente3=Ponente.objects.create(nombre="ponente3",apellidos="apellidos",especialidades="Ninguna",empresa="Empresa3",correo="ponente3@gmail.com",telefono="666666664",otras_formas_de_contacto="LinkedIn: https:/www.linkedin.com/ponente3")
        
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        #super().setup()

    def tearDown(self):           
        self.driver.quit()
        super(PonentesViews, self).tearDown()

    
    def test_ponentes(self):
        driver = self.driver
        driver.get(f'{self.live_server_url}')
        driver.set_window_size(1152, 824)
        driver.find_element(By.LINK_TEXT, "Ponentes").click()
        ponentes = self.driver.find_elements(By.TAG_NAME, "tr")
        self.assert_(len(ponentes)==4)
    
    def test_ponentes_detail(self):
        driver = self.driver
        driver.get(f'{self.live_server_url}')
        driver.set_window_size(1152, 824)
        driver.find_element(By.LINK_TEXT, "Ponentes").click()
        driver.find_element(By.XPATH, "//table/tbody/tr[1]").click()

        atributos = self.driver.find_elements(By.TAG_NAME, "tr")
        
        # En nuestro caso hay 7 atributos pero dos tablas diferentes ( hay un tr más)
        self.assert_(len(atributos)==8)

        nombre = atributos[1].find_element(By.ID, "ponente")
        self.assert_("ponente1" in nombre.text)

        apellidos = atributos[0].find_element(By.TAG_NAME, "td")
        self.assert_("apellidos" in apellidos.text)

        especialidades = atributos[2].find_element(By.TAG_NAME, "td")
        self.assert_("Ninguna" in especialidades.text)

        empresa = atributos[3].find_element(By.TAG_NAME, "td")
        self.assert_("Empresa1" in empresa.text)

        correo = atributos[4].find_element(By.TAG_NAME, "td")
        self.assert_(correo.text=="ponente1@gmail.com")

        telefono = atributos[5].find_element(By.TAG_NAME, "td")
        self.assert_(telefono.text=="666666666")

        otras_formas_de_contacto = atributos[6].find_element(By.TAG_NAME, "td")
        self.assert_(otras_formas_de_contacto.text=="Ninguna")


    def test_ponentes_detail_ponente3(self):
        driver = self.driver
        driver.get(f'{self.live_server_url}')
        driver.set_window_size(1152, 824)
        driver.find_element(By.LINK_TEXT, "Ponentes").click()
        driver.find_element(By.XPATH, "//table/tbody/tr[3]").click()

        atributos = self.driver.find_elements(By.TAG_NAME, "tr")
        self.assert_(len(atributos)==8)

        nombre = atributos[1].find_element(By.TAG_NAME, "td")
        self.assert_("ponente3" in nombre.text)

        apellidos = atributos[0].find_element(By.TAG_NAME, "td")
        self.assert_("apellidos" in apellidos.text)

        especialidades = atributos[2].find_element(By.TAG_NAME, "td")
        self.assert_("Ninguna" in especialidades.text)

        empresa = atributos[3].find_element(By.TAG_NAME, "td")
        self.assert_("Empresa3" in empresa.text)

        correo = atributos[4].find_element(By.TAG_NAME, "td")
        self.assert_(correo.text=="ponente3@gmail.com")

        telefono = atributos[5].find_element(By.TAG_NAME, "td")
        self.assert_(telefono.text=="666666664")

        otras_formas_de_contacto = atributos[6].find_element(By.TAG_NAME, "td")
        self.assert_(otras_formas_de_contacto.text=="LinkedIn: https:/www.linkedin.com/ponente3")