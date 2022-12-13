from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import datetime
from api.models import Evento

''' constantes para atributos en las pruebas de tipo caso negativo '''
TITULO = "Evento 1"
FECHA = "2022-08-19"
LUGAR = "Facultad"
AFORO = "400"
ASISTENTES = "200"
PREMIO = "Trofeo"
COSTE = "10"

class EventoTestCase(TestCase):
    def setUp(self):
        Evento.objects.create(titulo="Evento 1", descripcion="Descripción 1", fecha="2022-10-05 12:00",lugar="ETSII",aforo_max="200",n_asistentes="75", premio="Gominola", coste=10)
        Evento.objects.create(titulo="Evento to Update", descripcion="Descripción 2", fecha="2022-11-05 12:00",lugar="ETSII",aforo_max="100",n_asistentes="65", premio="Trofeo", coste=5)
    def test_evento_create(self):
        evento = Evento.objects.get(titulo = "Evento 1")
        self.assertIsNotNone(evento)
        self.assertEqual(evento.titulo,"Evento 1")
        self.assertEqual(evento.descripcion,"Descripción 1")
        self.assertEqual(evento.fecha, datetime.fromisoformat('2022-10-05 12:00:00+00:00'))
        self.assertEqual(evento.lugar,"ETSII")
        self.assertEqual(evento.aforo_max,200)
        self.assertEqual(evento.n_asistentes,75)
        self.assertEqual(evento.premio,"Gominola")
        self.assertEqual(evento.coste,10)
       
       
    def test_evento_delete(self):
        evento = Evento.objects.get(titulo = "Evento 1")
        evento.delete()
        self.assertEqual(1,Evento.objects.count())

    
    def test_evento_update(self):
        evento = Evento.objects.get(titulo = "Evento to Update")
        evento.titulo="Actualiza Titulo"
        evento.descripcion="Actualiza Descripcion"
        evento.fecha="2021-07-14 12:00"
        evento.lugar="A1.30"
        evento.aforo_max= "300"
        evento.n_asistentes= "100"
        evento.premio="Medalla"
        evento.coste="50"
        evento.save()
        evento_prueba = Evento.objects.get(titulo = "Actualiza Titulo")
        self.assertIsNotNone(evento_prueba)
        self.assertEqual(evento_prueba.titulo,"Actualiza Titulo")
        self.assertEqual(evento_prueba.descripcion,"Actualiza Descripcion")
        self.assertEqual(evento_prueba.fecha, datetime.fromisoformat('2021-07-14 12:00:00+00:00'))
        self.assertEqual(evento_prueba.lugar,"A1.30")
        self.assertEqual(evento_prueba.aforo_max,300)
        self.assertEqual(evento_prueba.n_asistentes,100)
        self.assertEqual(evento_prueba.premio,"Medalla")
        self.assertEqual(evento_prueba.coste,50)
    


    # CASOS NEGATIVOS
   
    def test_evento_create_null_titulo(self):
        with self.assertRaises(Exception):
            Evento.objects.create(titulo=None,fecha=FECHA,lugar=LUGAR,aforo_max=AFORO,n_asistentes=ASISTENTES, premio=PREMIO, coste=COSTE)
    
    def test_evento_create_blank_titulo(self):
            evento = Evento(titulo="",fecha=FECHA,lugar=LUGAR,aforo_max=AFORO,n_asistentes=ASISTENTES, premio=PREMIO, coste=COSTE)
            with self.assertRaises(ValidationError):
                evento.full_clean()

    def test_evento_create_null_fecha(self):
        with self.assertRaises(Exception):
            Evento.objects.create(titulo=TITULO,fecha=None,lugar=LUGAR,aforo_max=AFORO,n_asistentes=ASISTENTES, premio=PREMIO, coste=COSTE)

    def test_evento_create_blank_fecha(self):
            evento = Evento(titulo=TITULO,fecha="",lugar=LUGAR,aforo_max=AFORO,n_asistentes=ASISTENTES, premio=PREMIO, coste=COSTE)
            with self.assertRaises(ValidationError):
                evento.full_clean()

    def test_evento_create_null_lugar(self):
        with self.assertRaises(Exception):
            Evento.objects.create(titulo=TITULO,fecha=FECHA,lugar=None,aforo_max=AFORO,n_asistentes=ASISTENTES, premio=PREMIO, coste=COSTE)
    
    def test_evento_create_blank_lugar(self):
            evento = Evento(titulo=TITULO,fecha=FECHA,lugar="",aforo_max=AFORO,n_asistentes=ASISTENTES, premio=PREMIO, coste=COSTE)
            with self.assertRaises(ValidationError):
                evento.full_clean()
    
    def test_evento_create_error_format_fecha(self):
        with self.assertRaises(Exception):
            Evento.objects.create(titulo=TITULO,fecha="10-02-2021 00:00",lugar=LUGAR,aforo_max=AFORO,n_asistentes=ASISTENTES, premio=PREMIO, coste=COSTE)
    
    def test_evento_create_negative_coste(self):
        evento = Evento(titulo=TITULO,fecha=FECHA,lugar=LUGAR,aforo_max=AFORO,n_asistentes=ASISTENTES, premio=PREMIO, coste="-1")
        with self.assertRaises(ValidationError):
            evento.full_clean()

    def test_evento_update_null_titulo(self):
        with self.assertRaises(Exception):
            Evento.objects.update(titulo=None,fecha=FECHA,lugar=LUGAR,aforo_max=AFORO,n_asistentes=ASISTENTES, premio=PREMIO, coste=COSTE)
    
    def test_evento_update_null_fecha(self):
        with self.assertRaises(Exception):
            Evento.objects.update(titulo=TITULO,fecha=None,lugar=LUGAR,aforo_max=AFORO,n_asistentes=ASISTENTES, premio=PREMIO, coste=COSTE)
    
    def test_evento_update_null_lugari(self):
        with self.assertRaises(Exception):
            Evento.objects.update(titulo=TITULO,fecha=FECHA,lugar=None,aforo_max=AFORO,n_asistentes=ASISTENTES, premio=PREMIO, coste=COSTE)

    def test_evento_update_error_format_fecha(self):
        with self.assertRaises(Exception):
            Evento.objects.update(titulo=TITULO,fecha="10-02-2021 00:00",lugar=LUGAR,aforo_max=AFORO,n_asistentes=ASISTENTES, premio=PREMIO, coste=COSTE)

    def test_evento_update_error_negative_coste(self):
        evento = Evento(titulo=TITULO,fecha=FECHA,lugar=LUGAR,aforo_max=AFORO,n_asistentes=ASISTENTES, premio=PREMIO, coste="-1")
        with self.assertRaises(ValidationError):
            evento.full_clean()
            evento.save()
  