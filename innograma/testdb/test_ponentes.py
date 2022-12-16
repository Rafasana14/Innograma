from django.test import TestCase
from api.models import Ponente

''' constantes para atributos en las pruebas de tipo caso negativo '''
CORREO = "ivamorgra@alum.us.es"
APELLIDOS = "mor gra"
EMPRESA = "Django"
ESPECIALIDADES = "Python"
TELEFONO = "123456789"

class PonenteTestCase(TestCase):
    def setUp(self):
        Ponente.objects.create(nombre="ivamorgra",apellidos="mor gra",especialidades="python",empresa="Django",correo="ivamorgra@python.com",telefono="123456789",otras_formas_de_contacto="LinkedIn: Iván Moreno Granado")
        Ponente.objects.create(nombre="ivamorgraToUpdate",apellidos="morup gradate",especialidades="python",empresa="Django",correo="ivamorgratoupdate@python.com",telefono="223456789",otras_formas_de_contacto="LinkedIn: Iván Moreno Granado")
        
    def test_ponente_create(self):
        ponente = Ponente.objects.get(nombre = "ivamorgra")
        self.assertIsNotNone(ponente)
        self.assertEqual(ponente.nombre,"ivamorgra")
        self.assertEqual(ponente.apellidos,"mor gra")
        self.assertEqual(ponente.especialidades,"python")
        self.assertEqual(ponente.empresa,"Django")
        self.assertEqual(ponente.correo,"ivamorgra@python.com")
        self.assertEqual(ponente.telefono,"123456789")
        self.assertEqual(ponente.otras_formas_de_contacto,"LinkedIn: Iván Moreno Granado")
       
       
    def test_ponente_delete(self):
        ponente = Ponente.objects.get(nombre = "ivamorgra")
        ponente.delete()
        self.assertEqual(1,Ponente.objects.count())

    
    def test_ponente_update(self):
        ponente = Ponente.objects.get(nombre = "ivamorgraToUpdate")
        ponente.nombre="Actualiza"
        ponente.apellidos="Actualiza Prueba"
        ponente.especialidades="Prueba"
        ponente.correo="Prueba@gmail.com"
        ponente.empresa="Empresa Prueba"
        ponente.telefono="223456789"
        ponente.otras_formas_de_contacto="https://www.google.es/github/ivamorgra"
        ponente.save()
        ponente_prueba = Ponente.objects.get(nombre = "Actualiza")
        self.assertIsNotNone(ponente_prueba)
        self.assertEqual(ponente_prueba.nombre,"Actualiza")
        self.assertEqual(ponente_prueba.apellidos,"Actualiza Prueba")
        self.assertEqual(ponente_prueba.especialidades,"Prueba")
        self.assertEqual(ponente_prueba.correo,"Prueba@gmail.com")
        self.assertEqual(ponente_prueba.telefono,"223456789")
        self.assertEqual(ponente_prueba.empresa,"Empresa Prueba")
        self.assertEqual(ponente_prueba.otras_formas_de_contacto,"https://www.google.es/github/ivamorgra")

    
    
    def test_ponente_create_error_email(self):
        with self.assertRaises(Exception):
            Ponente.objects.create(nombre="Prueba email",apellidos=APELLIDOS,especialidades=ESPECIALIDADES,conferencias_impartidas="python",empresa="Django",correo="ivamorgra",telefono="123456789",otras_formas_de_contacto="LinkedIn: Iván Moreno Granado")
    

    def test_ponente_create_duplicated_email(self):
        with self.assertRaises(Exception):
            Ponente.objects.create(nombre="Prueba email",apellidos=APELLIDOS,especialidades=ESPECIALIDADES,conferencias_impartidas="python",empresa="Django",correo="ivamorgra@python.com",telefono="323456789",otras_formas_de_contacto="LinkedIn: Iván Moreno Granado")
    
    def test_ponente_create_duplicate_phone(self):
        with self.assertRaises(Exception):
            Ponente.objects.create(nombre="Prueba email",apellidos=APELLIDOS,especialidades=ESPECIALIDADES,conferencias_impartidas="python",empresa=EMPRESA,correo="ivamorgra@outlook.es",telefono=TELEFONO,otras_formas_de_contacto="LinkedIn: Iván Moreno Granado")

    def test_ponente_create_blank_nombre(self):
        with self.assertRaises(Exception):
            Ponente.objects.create(nombre=" ",apellidos=APELLIDOS,especialidades=ESPECIALIDADES,conferencias_impartidas="python",empresa=EMPRESA,correo="ivamorgra@outlook.es",telefono=TELEFONO,otras_formas_de_contacto="LinkedIn: Iván Moreno Granado")

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
    