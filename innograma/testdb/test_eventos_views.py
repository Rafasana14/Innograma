from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from api.models import Evento


class EventosViewsTests(StaticLiveServerTestCase):

    def setUp(self):
        Evento.objects.create(titulo="Panpizzas gratis",
                              descripcion="Reparto de 200 tickets para panpizzas gratuitos en Ñam Ñam válidos durante la semana de Innosoft Days",
                              fecha="2022-11-08 8:30",
                              lugar="Punto verde ETSII, a la derecha de conserjería",
                              aforo_max="200",
                              premio="Unidad de ticket intercambiable por un panpizza gratis en ÑamÑam", 
                              coste="0.0")
        Evento.objects.create(titulo="Gymkhana",
                              descripcion="Gymkhana con 9 distintos retos a realizar en el mínimo tiempo posible",
                              fecha="2022-11-10 15:00",
                              lugar="Aula A3.10 ETSII",
                              premio="Caja de 5KG de La Estepeña",
                              n_asistentes = "63",
                              coste="0.0")
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
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
        count = Evento.objects.all().count()
        self.assert_(len(eventos)-1 == count) #Le restamos uno a len(eventos) para no contar la cabecera de la tabla
        
    def test_details_view_event(self):
        driver = self.driver
        driver.get(f'{self.live_server_url}')
        driver.set_window_size(1152, 824)
        driver.find_element(By.LINK_TEXT, "Eventos").click()
        driver.find_element(By.XPATH, "//table/tbody/tr[contains(.,'Panpizzas gratis')]").click()
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

    def test_details_view_event_1(self):
        driver = self.driver
        driver.get(f'{self.live_server_url}')
        driver.set_window_size(1152, 824)
        driver.find_element(By.LINK_TEXT, "Eventos").click()
        driver.find_element(By.XPATH, "//table/tbody/tr[contains(.,'Gymkhana')]").click()
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

    def test_view_create_event(self):
        old_count= Evento.objects.all().count()
        driver = self.driver
        driver.get(f'{self.live_server_url}')
        driver.set_window_size(1152, 824)
        self.driver.find_element(By.LINK_TEXT, "Acceso Administrador").click()
        self.driver.find_element(By.ID, "id_username").send_keys("admin")
        self.driver.find_element(By.ID, "id_password").send_keys("admin",Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT, "Eventos").click()
        self.driver.find_element(By.XPATH, '//button[text()="Crear"]').click()
        self.driver.find_element(By.ID, "id_titulo").send_keys("Título de evento creado")
        self.driver.find_element(By.ID, "id_descripcion").send_keys("Descripción de evento creado")
        self.driver.find_element(By.ID, "id_fecha").send_keys("2022-11-08 11:00:00")
        self.driver.find_element(By.ID, "id_lugar").send_keys("Lugar de evento creado")
        self.driver.find_element(By.ID, "id_aforo_max").send_keys("240")
        self.driver.find_element(By.ID, "id_n_asistentes").send_keys("194")
        self.driver.find_element(By.ID, "id_premio").send_keys("Premio del evento creado")
        self.driver.find_element(By.ID, "id_coste").send_keys("35")
        self.driver.find_element(By.XPATH, '//button[@name="Submit"]').submit()
        count= Evento.objects.all().count()
        self.assertTrue(count == (old_count+1))
        
    def test_view_update_event(self):
        evento = Evento.objects.get(titulo="Panpizzas gratis")
        aforo_max_antiguo=evento.aforo_max
        self.driver.get(f'{self.live_server_url}')
        self.driver.find_element(By.LINK_TEXT, "Acceso Administrador").click()
        self.driver.find_element(By.ID, "id_username").send_keys("admin")
        self.driver.find_element(By.ID, "id_password").send_keys("admin",Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT, "Eventos").click()
        self.driver.find_element(By.XPATH, "//table/tbody/tr[contains(.,'Panpizzas gratis')]").click()
        self.driver.find_element(By.XPATH,  "//button[contains(.,'Editar')]").click()
        self.driver.find_element(By.ID, "id_aforo_max").clear()
        self.driver.find_element(By.ID, "id_aforo_max").send_keys("300")
        self.driver.find_element(By.XPATH, '//button[@name="Submit"]').submit()
        evento_nuevo = Evento.objects.get(titulo="Panpizzas gratis")
        aforo_max_nuevo = evento_nuevo.aforo_max
        self.assertTrue(evento.id == evento_nuevo.id)
        self.assertTrue(aforo_max_antiguo != aforo_max_nuevo)
        self.assertTrue(evento_nuevo.aforo_max == 300)
        self.driver.find_element(By.LINK_TEXT, "Cerrar Sesión").click()

    def test_view_delete_event(self):
        
        Evento.objects.create(titulo="Titulo de evento a eliminar",
                        descripcion="Descripcion de evento a eliminar",
                        fecha="2022-11-10 15:00",
                        lugar="Lugar de evento a eliminar",
                        premio="Premio de evento a eliminar",
                        n_asistentes = "34",
                        coste="20.0")
        old_count= Evento.objects.all().count()
        driver = self.driver
        driver.get(f'{self.live_server_url}')
        driver.set_window_size(1152, 824)
        self.driver.find_element(By.LINK_TEXT, "Acceso Administrador").click()
        self.driver.find_element(By.ID, "id_username").send_keys("admin")
        self.driver.find_element(By.ID, "id_password").send_keys("admin",Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT, "Eventos").click()
        self.driver.find_element(By.XPATH, "//table/tbody/tr[contains(.,'Titulo de evento a eliminar')]").click()
        self.driver.find_element(By.XPATH, '//button[text()="Eliminar"]').click()
        self.driver.find_element(By.XPATH, '//button[text()="Confirmar"]').click() #Confirmamos la eliminacion
        count= Evento.objects.all().count()
        self.assert_(count==old_count-1) #Sería 1 evento (el otro es la cabecera de la tabla)
        self.driver.find_element(By.LINK_TEXT, "Cerrar Sesión").click()    
        