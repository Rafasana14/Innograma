from rest_framework.test import APISimpleTestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from faker import Faker

class TestSetUp(APITestCase):
    def setUp(self):

        faker = Faker()
        
        self.login_url = '/admin/login/?next=/admin/'
        self.user  =User.objects.create_superuser(
            username='admin',
            last_name='admin',
            password='admin',
            email = faker.email()
        )


        response = self.client.post(self.login_url,
         {  'username': self.user.username,
            'password': self.user.password
         }, format='json')
        
        self.assertEquals(response.status_code, 200)

        return super().setUp()

    def test_prueba(self):
        pass