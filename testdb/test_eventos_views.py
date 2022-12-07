from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from api.models import Evento


class EventosViewsTests(StaticLiveServerTestCase):

    def setUp(self):
        #Load base test functionality for decide
        Evento.objects.create(titulo="Panpizzas gratis",descripcion="Reparto de 200 tickets para panpizzas gratuitos en Ñam Ñam válidos durante la semana de Innosoft Days",fecha="2022-11-08 8:30",lugar="Punto verde ETSII, a la derecha de conserjería",aforo_max="200",premio="Unidad de ticket intercambiable por un panpizza gratis en ÑamÑam", coste="0.0")
        Evento.objects.create(titulo="Gymkhana",descripcion="Gymkhana con 9 distintos retos a realizar en el mínimo tiempo posible",fecha="2022-11-10 15:00",lugar="Aula A3.10 ETSII",premio="Caja de 5KG de La Estepeña",n_asistentes = "63",coste="0.0")
        
        options = webdriver.ChromeOptions()
        options.headless = False
        self.driver = webdriver.Chrome(options=options)

        super(EventosViewsTests, self).setUp()           
            
    def tearDown(self):           
        self.driver.quit()
        super(EventosViewsTests, self).tearDown()
  
    def test_count_eventos_list_view(self):
        driver = self.driver
        driver.get(f'{self.live_server_url}')
        driver.set_window_size(1152, 824)
        driver.find_element(By.LINK_TEXT, "Eventos").click()
        eventos = self.driver.find_elements(By.TAG_NAME, "tr")
        self.assert_(len(eventos)==3)
        #We check if they are 3 rows, counting the header (2 events)
        
    def test_details_view_event_1(self):
        
        driver = self.driver
        driver.get(f'{self.live_server_url}')
        driver.set_window_size(1152, 824)
        driver.find_element(By.LINK_TEXT, "Eventos").click()
        driver.find_element(By.XPATH, "//table/tbody/tr[1]").click()
        
        atributos = self.driver.find_elements(By.TAG_NAME, "tr")
        self.assert_(len(atributos)==8)
        
        titulo = atributos[0].find_element(By.TAG_NAME, "td")
        self.assert_("Panpizzas gratis" in titulo.text)
        
        descripcion = atributos[1].find_element(By.TAG_NAME, "td")
        self.assert_("Reparto de 200 tickets para panpizzas gratuitos en Ñam Ñam válidos durante la semana de Innosoft Days" in descripcion.text)
        
        fecha = atributos[2].find_element(By.TAG_NAME, "td")
        self.assert_("Nov. 8, 2022, 8:30 a.m." in fecha.text)
        
        lugar = atributos[3].find_element(By.TAG_NAME, "td")
        self.assert_("Punto verde ETSII, a la derecha de conserjería" in lugar.text)
        
        aforo_max = atributos[4].find_element(By.TAG_NAME, "td")
        self.assert_(aforo_max.text=="200")
        
        n_asistentes = atributos[5].find_element(By.TAG_NAME, "td")
        self.assert_(n_asistentes.text=="No especificado")
        
        premio = atributos[6].find_element(By.TAG_NAME, "td")
        self.assert_(premio.text=="Unidad de ticket intercambiable por un panpizza gratis en ÑamÑam")
        
        coste = atributos[7].find_element(By.TAG_NAME, "td")
        self.assert_(coste.text=="0.0 €")

    def test_details_view_event_2(self):
        
        driver = self.driver
        driver.get(f'{self.live_server_url}')
        driver.set_window_size(1152, 824)
        driver.find_element(By.LINK_TEXT, "Eventos").click()
        driver.find_element(By.XPATH, "//table/tbody/tr[2]").click()
        
        atributos = self.driver.find_elements(By.TAG_NAME, "tr")
        self.assert_(len(atributos)==8)
        
        titulo = atributos[0].find_element(By.TAG_NAME, "td")
        self.assert_("Gymkhana" in titulo.text)
        
        
        descripcion = atributos[1].find_element(By.TAG_NAME, "td")
        self.assert_("Gymkhana con 9 distintos retos a realizar en el mínimo tiempo posible" in descripcion.text)
        
        fecha = atributos[2].find_element(By.TAG_NAME, "td")
        self.assert_("Nov. 10, 2022, 3 p.m." in fecha.text)
        
        lugar = atributos[3].find_element(By.TAG_NAME, "td")
        self.assert_("Aula A3.10 ETSII" in lugar.text)
        
        aforo_max = atributos[4].find_element(By.TAG_NAME, "td")
        self.assert_(aforo_max.text=="No especificado")
        
        n_asistentes = atributos[5].find_element(By.TAG_NAME, "td")
        self.assert_(n_asistentes.text=="63")
        
        premio = atributos[6].find_element(By.TAG_NAME, "td")
        self.assert_(premio.text=="Caja de 5KG de La Estepeña")
        
        coste = atributos[7].find_element(By.TAG_NAME, "td")
        self.assert_(coste.text=="0.0 €")