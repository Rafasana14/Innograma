from django.test import TestCase
from api.models import Ponente, Conferencia, Ponente_Conferencia


class PonentePonenciaTestCase(TestCase):

    def setUp(self):
        ponente_aux = Ponente.objects.create(nombre="migrivros",apellidos="mig riv",especialidades="redes",empresa="Django",correo="migrivros@python.com",telefono="8757396781",otras_formas_de_contacto="LinkedIn: Miguel Ángel Rivas Rosado")
        conferencia_aux = Conferencia.objects.create(tema="Redes",fecha="2022-10-05 12:00",espacio="ETSII",aforo_max="200",n_asistentes="75")
        Ponente_Conferencia.objects.create(ponente=ponente_aux,conferencia=conferencia_aux)

        
    def test_ponente_conferencia_create(self):
        ponente_aux = Ponente.objects.get(correo = "migrivros@python.com")
        conferencia_aux = Conferencia.objects.get(tema="Redes")
        ponente_conferencia = Ponente_Conferencia.objects.get(ponente=ponente_aux,conferencia=conferencia_aux)
        self.assertIsNotNone(ponente_conferencia)
        self.assertEqual(ponente_conferencia.ponente,ponente_aux)
        self.assertEqual(ponente_conferencia.conferencia,conferencia_aux)
       

    #Test para comprobar que se elimina la relacion correctamente
    def test_ponente_conferencia_delete(self):
        ponente_aux = Ponente.objects.get(correo = "migrivros@python.com")
        conferencia_aux = Conferencia.objects.get(tema="Redes")
        ponente_conferencia = Ponente_Conferencia.objects.get(ponente=ponente_aux,conferencia=conferencia_aux)
        ponente_conferencia.delete()
        self.assertEqual(0,Ponente_Conferencia.objects.count())


    #Test para comprobar que se elimina la relacion correctamente al eliminar el ponente
    def test_ponente_conferencia_delete_ponente(self):
        ponente_aux = Ponente.objects.get(correo = "migrivros@python.com")
        ponente_aux.delete()
        self.assertEqual(0,Ponente_Conferencia.objects.count())

    
    #Test para comprobar que se elimina la relacion correctamente al eliminar la conferencia
    def test_ponente_conferencia_delete_conferencia(self):
        conferencia_aux = Conferencia.objects.get(tema="Redes")
        conferencia_aux.delete()
        self.assertEqual(0,Ponente_Conferencia.objects.count())
