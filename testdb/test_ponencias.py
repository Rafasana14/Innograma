from django.test import TestCase
from datetime import date
from datetime import datetime
from api.models import Conferencia

''' constantes para atributos en las pruebas de tipo caso negativo '''
PONETE = "Pedro"
TEMA = "IA"
FECHA = "2022-08-19"
ESPACIO = "Facultad"
AFORO = "400"
ASISTENTES = "200"

class PonenciaTestCase(TestCase):
    def setUp(self):
        Conferencia.objects.create(ponente="Daniel Ruiz",tema="Redes",fecha="2022-10-05 12:00",espacio="ETSII",aforo_max="200",n_asistentes="75")
        Conferencia.objects.create(ponente="Daniel Ruiz To Update",tema="Redes",fecha="2022-10-05 12:00",espacio="ETSII",aforo_max="200",n_asistentes="75")
        
    def test_ponente_create(self):
        ponencia = Conferencia.objects.get(ponente = "Daniel Ruiz")
        self.assertIsNotNone(ponencia)
        self.assertEqual(ponencia.ponente,"Daniel Ruiz")
        self.assertEqual(ponencia.tema,"Redes")
        #self.assertEqual(ponencia.fecha, datetime.date(2022,10,5,12,0))
        self.assertEqual(ponencia.espacio,"ETSII")
        self.assertEqual(ponencia.aforo_max,200)
        self.assertEqual(ponencia.n_asistentes,75)
       
       
    def test_ponente_delete(self):
        ponencia = Conferencia.objects.get(ponente = "Daniel Ruiz")
        ponencia.delete()
        self.assertEqual(1,Conferencia.objects.count())

    
    def test_ponente_update(self):
        ponencia = Conferencia.objects.get(ponente = "Daniel Ruiz To Update")
        ponencia.ponente="Daniel Actualizado"
        ponencia.tema="Actualiza Tema"
        ponencia.fecha="2021-07-14 12:00"
        ponencia.espacio="A1.30"
        ponencia.aforo_max= "300"
        ponencia.n_asistentes= "100"
        ponencia.save()
        ponencia_prueba = Conferencia.objects.get(ponente = "Daniel Actualizado")
        self.assertIsNotNone(ponencia_prueba)
        self.assertEqual(ponencia_prueba.ponente,"Daniel Actualizado")
        self.assertEqual(ponencia_prueba.tema,"Actualiza Tema")
        #self.assertEqual(ponencia_prueba.fecha, datetime.date(2021,7,14,12,0))
        self.assertEqual(ponencia_prueba.espacio,"A1.30")
        self.assertEqual(ponencia_prueba.aforo_max,300)
        self.assertEqual(ponencia_prueba.n_asistentes,100)


    '''
    def test_ponencia_create_blank_ponente(self):
        with self.assertRaises(Exception):
            Conferencia.objects.create(ponente=" ",tema="Redes",fecha="2022-10-05 12:00",espacio="ETSII",aforo_max="200",n_asistentes="75")
    
    def test_ponente_create_blank_apellidos(self):
        with self.assertRaises(Exception):
            Ponente.objects.create(nombre="Prueba",apellidos=" ",especialidades=ESPECIALIDADES,conferencias_impartidas="python",empresa=EMPRESA,correo=CORREO,telefono=TELEFONO,otras_formas_de_contacto="LinkedIn: Iván Moreno Granado")

    def test_ponente_create_blank_especialidades(self):
        with self.assertRaises(Exception):
            Ponente.objects.create(nombre="Prueba",apellidos="moreno granado",especialidades=" ",conferencias_impartidas="python",empresa=EMPRESA,correo=CORREO,telefono=TELEFONO,otras_formas_de_contacto="LinkedIn: Iván Moreno Granado")
    
    def test_ponente_create_blank_conferencias_impartidas(self):
        with self.assertRaises(Exception):
            Ponente.objects.create(nombre="Prueba",apellidos="moreno granado",especialidades=ESPECIALIDADES,conferencias_impartidas=" ",empresa=EMPRESA,correo=CORREO,telefono=TELEFONO,otras_formas_de_contacto="LinkedIn: Iván Moreno Granado")
    
    def test_ponente_update_email_duplicated(self):
        with self.assertRaises(Exception):
            Ponente.objects.update(nombre="ivamorgraToUpdate",apellidos="moreno granado",especialidades=ESPECIALIDADES,conferencias_impartidas="python",empresa=EMPRESA,correo="ivamorgra@python.com",telefono=TELEFONO,otras_formas_de_contacto="LinkedIn: Iván Moreno Granado")
        
    def test_ponente_update_telefono_duplicated(self):
        with self.assertRaises(Exception):
            Ponente.objects.update(nombre="ivamorgra",apellidos="moreno granado",especialidades=ESPECIALIDADES,conferencias_impartidas="python",empresa=EMPRESA,correo=CORREO,telefono="223456789",otras_formas_de_contacto="LinkedIn: Iván Moreno Granado")
    
    def test_ponente_update_blank_nombre(self):
        with self.assertRaises(Exception):
            Ponente.objects.update(nombre=" ",apellidos="moreno granado",especialidades=ESPECIALIDADES,conferencias_impartidas="python",empresa=EMPRESA,correo=CORREO,telefono="223456789",otras_formas_de_contacto="LinkedIn: Iván Moreno Granado")
    
    def test_ponente_update_blank_apellidos(self):
        with self.assertRaises(Exception):
            Ponente.objects.update(nombre="ivamorgra",apellidos=" ",especialidades=ESPECIALIDADES,conferencias_impartidas="python",empresa=EMPRESA,correo=CORREO,telefono="223456789",otras_formas_de_contacto="LinkedIn: Iván Moreno Granado")
    
    def test_ponente_update_blank_especialidades(self):
        with self.assertRaises(Exception):
            Ponente.objects.update(nombre="ivamorgra",apellidos="moreno granado",especialidades=" ",conferencias_impartidas="python",empresa=EMPRESA,correo=CORREO,telefono="223456789",otras_formas_de_contacto="LinkedIn: Iván Moreno Granado")
    
    def test_ponente_update_blank_conferencias_impartidas(self):
        with self.assertRaises(Exception):
            Ponente.objects.update(nombre="ivamorgra",apellidos="moreno granado",especialidades=ESPECIALIDADES,conferencias_impartidas=" ",empresa=EMPRESA,correo=CORREO,telefono="223456789",otras_formas_de_contacto="LinkedIn: Iván Moreno Granado")
    '''