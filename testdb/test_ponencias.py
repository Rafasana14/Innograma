from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import datetime
from api.models import Conferencia

''' constantes para atributos en las pruebas de tipo caso negativo '''
TEMA = "IA"
FECHA = "2022-08-19"
ESPACIO = "Facultad"
AFORO = "400"
ASISTENTES = "200"

class PonenciaTestCase(TestCase):
    def setUp(self):
        Conferencia.objects.create(tema="Redes",fecha="2022-10-05 12:00",espacio="ETSII",aforo_max="200",n_asistentes="75")
        Conferencia.objects.create(tema="Redes To Update",fecha="2022-10-05 12:00",espacio="ETSII",aforo_max="200",n_asistentes="75")

    def test_ponencia_create(self):
        ponencia = Conferencia.objects.get(tema = "Redes")
        self.assertIsNotNone(ponencia)
        self.assertEqual(ponencia.tema,"Redes")
        self.assertEqual(ponencia.fecha, datetime.fromisoformat('2022-10-05 12:00:00+00:00'))
        self.assertEqual(ponencia.espacio,"ETSII")
        self.assertEqual(ponencia.aforo_max,200)
        self.assertEqual(ponencia.n_asistentes,75)
       
       
    def test_ponencia_delete(self):
        ponencia = Conferencia.objects.get(tema = "Redes")
        ponencia.delete()
        self.assertEqual(1,Conferencia.objects.count())

    
    def test_ponencia_update(self):
        ponencia = Conferencia.objects.get(tema = "Redes To Update")
        ponencia.tema="Actualiza Tema"
        ponencia.fecha="2021-07-14 12:00"
        ponencia.espacio="A1.30"
        ponencia.aforo_max= "300"
        ponencia.n_asistentes= "100"
        ponencia.save()
        ponencia_prueba = Conferencia.objects.get(tema = "Actualiza Tema")
        self.assertIsNotNone(ponencia_prueba)
        self.assertEqual(ponencia_prueba.tema,"Actualiza Tema")
        self.assertEqual(ponencia_prueba.fecha, datetime.fromisoformat('2021-07-14 12:00:00+00:00'))
        self.assertEqual(ponencia_prueba.espacio,"A1.30")
        self.assertEqual(ponencia_prueba.aforo_max,300)
        self.assertEqual(ponencia_prueba.n_asistentes,100)
    


    # CASOS NEGATIVOS
   
    def test_ponencia_create_null_tema(self):
        with self.assertRaises(Exception):
            Conferencia.objects.create(tema=None,fecha=FECHA,espacio=ESPACIO,aforo_max=AFORO,n_asistentes=ASISTENTES)
    
    def test_ponencia_create_blank_tema(self):
            conferencia = Conferencia(tema="",fecha=FECHA,espacio=ESPACIO,aforo_max=AFORO,n_asistentes=ASISTENTES)
            with self.assertRaises(ValidationError):
                conferencia.full_clean()

    def test_ponencia_create_null_fecha(self):
        with self.assertRaises(Exception):
            Conferencia.objects.create(tema=TEMA,fecha=None,espacio=ESPACIO,aforo_max=AFORO,n_asistentes=ASISTENTES)

    def test_ponencia_create_blank_fecha(self):
            conferencia = Conferencia(tema=TEMA,fecha="",espacio=ESPACIO,aforo_max=AFORO,n_asistentes=ASISTENTES)
            with self.assertRaises(ValidationError):
                conferencia.full_clean()

    def test_ponencia_create_null_espacio(self):
        with self.assertRaises(Exception):
            Conferencia.objects.create(tema=TEMA,fecha=FECHA,espacio=None,aforo_max=AFORO,n_asistentes=ASISTENTES)
    
    def test_ponencia_create_blank_espacio(self):
            conferencia = Conferencia(tema=TEMA,fecha=FECHA,espacio="",aforo_max=AFORO,n_asistentes=ASISTENTES)
            with self.assertRaises(ValidationError):
                conferencia.full_clean()
    
    def test_ponencia_create_error_format_fecha(self):
        with self.assertRaises(Exception):
            Conferencia.objects.create(tema=TEMA,fecha="10-02-2021 00:00",espacio=ESPACIO,aforo_max=AFORO,n_asistentes=ASISTENTES)
    
    def test_ponencia_update_null_tema(self):
        with self.assertRaises(Exception):
            Conferencia.objects.update(tema=None,fecha=FECHA,espacio=ESPACIO,aforo_max=AFORO,n_asistentes=ASISTENTES)
    
    def test_ponencia_update_null_fecha(self):
        with self.assertRaises(Exception):
            Conferencia.objects.update(tema=TEMA,fecha=None,espacio=ESPACIO,aforo_max=AFORO,n_asistentes=ASISTENTES)
    
    def test_ponencia_update_null_espacioi(self):
        with self.assertRaises(Exception):
            Conferencia.objects.update(tema=TEMA,fecha=FECHA,espacio=None,aforo_max=AFORO,n_asistentes=ASISTENTES)

    def test_ponencia_update_error_format_fecha(self):
        with self.assertRaises(Exception):
            Conferencia.objects.update(tema=TEMA,fecha="10-02-2021 00:00",espacio=ESPACIO,aforo_max=AFORO,n_asistentes=ASISTENTES)
  
