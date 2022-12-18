from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from api.models import Ponente

class PonentesViews(StaticLiveServerTestCase):
    def setUp(self):
        Ponente.objects.create(nombre="ponente1",apellidos="apellidos",
                               especialidades="Ninguna",empresa="Empresa1",correo="ponente1@gmail.com",
                               telefono="666666666",otras_formas_de_contacto="Ninguna")
        Ponente.objects.create(nombre="ponente2",apellidos="apellidos",especialidades="Ninguna",
                               empresa="Empresa2",correo="ponente2@gmail.com",telefono="666666665",
                               otras_formas_de_contacto="Ninguna")
        Ponente.objects.create(nombre="ponente3",apellidos="apellidos",especialidades="Ninguna",
                               empresa="Empresa3",correo="ponente3@gmail.com",telefono="666666664",
                               otras_formas_de_contacto="LinkedIn: https:/www.linkedin.com/ponente3")
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')      
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        super(PonentesViews, self).setUp()

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
        
        # En nuestro caso hay 7 atributos 
        self.assert_(len(atributos)==7)

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
        self.assert_(len(atributos)==7)

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
        
    def test_create_ponente(self):
        old_count= Ponente.objects.all().count()
        self.driver.get(f'{self.live_server_url}')
        self.driver.find_element(By.LINK_TEXT, "Acceso Administrador").click()
        self.driver.find_element(By.ID, "id_username").send_keys("admin")
        self.driver.find_element(By.ID, "id_password").send_keys("admin",Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT, "Ponentes").click()
        self.driver.find_element(By.XPATH, '//button[text()="Crear"]').click()
        self.driver.find_element(By.ID, "id_nombre").send_keys("Rafael")
        self.driver.find_element(By.ID, "id_apellidos").send_keys("Sanabria Espárrago")
        self.driver.find_element(By.ID, "id_especialidades").send_keys("Ciencia")
        self.driver.find_element(By.XPATH, '//button[@name="Submit"]').submit()
        count= Ponente.objects.all().count()
        self.assertTrue(count == (old_count+1))
        self.driver.find_element(By.LINK_TEXT, "Cerrar Sesión").click()
        
    def test_editar_ponente(self):
        ponente=Ponente.objects.get(nombre="ponente1")
        nombre_old=ponente.nombre
        self.driver.get(f'{self.live_server_url}')
        self.driver.find_element(By.LINK_TEXT, "Acceso Administrador").click()
        self.driver.find_element(By.ID, "id_username").send_keys("admin")
        self.driver.find_element(By.ID, "id_password").send_keys("admin",Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT, "Ponentes").click()
        self.driver.find_element(By.XPATH, "//td[contains(.,\'666666666\')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,\'Editar\')]").click()
        self.driver.find_element(By.ID, "id_nombre").clear()
        self.driver.find_element(By.ID, "id_nombre").send_keys("cambiado")
        self.driver.find_element(By.XPATH, '//button[@name="Submit"]').submit()
        ponente_new = Ponente.objects.get(nombre="cambiado")
        nombre_new = ponente_new.nombre
        self.assertTrue(ponente.id == ponente_new.id and nombre_old != nombre_new)
        self.driver.find_element(By.LINK_TEXT, "Cerrar Sesión").click()
    
    def test_view_delete_ponente(self):
        Ponente.objects.create(nombre="Juan", apellidos="palomo",
                               especialidades="Tema",empresa="Empresa1",correo="juan@gmail.com",
                               telefono="623748592",otras_formas_de_contacto="Ninguna")
        driver = self.driver
        driver.get(f'{self.live_server_url}')
        old_count = Ponente.objects.count()
        self.driver.find_element(By.LINK_TEXT, "Acceso Administrador").click()
        self.driver.find_element(By.ID, "id_username").send_keys("admin")
        self.driver.find_element(By.ID, "id_password").send_keys("admin",Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT, "Ponentes").click()
        self.driver.find_element(By.XPATH, "//td[contains(.,\'623748592\')]").click() #Cojo por teléfono porque es único
        self.driver.find_element(By.XPATH, '//button[text()="Eliminar"]').click()
        self.driver.find_element(By.XPATH, '//button[text()="Confirmar"]').click() #Confirmamos la eliminacion
        count = Ponente.objects.count()
        self.assertTrue(count == (old_count-1))
        self.driver.find_element(By.LINK_TEXT, "Cerrar Sesión").click()  