from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.auto_parks.models import AutoParksModel
from apps.cars.models import CarModel
from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class AutoParkTestCase(APITestCase):
    def _authenticate(self):
        email = 'ivankonanezs4@gmail.com'
        password = 'pawe24gwgwe4g'
        self.client.post(reverse('user_create'), {
            'email': email,
            "password": password,
            'profile': {
                'name': 'ivan',
                'surname': 'konanets',
                'age': 35,
                'phone': "095325235123"
            }
        }, format='json')
        user = UserModel.objects.get(email=email)
        user.is_active = True
        user.save()

        response = self.client.post(reverse('auth_login'), {'email': email, 'password': password})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {response.data["access"]}')

    def test_create_auto_park_without_auth(self):
        prev_count = AutoParksModel.objects.count()
        auto_park = {
            "name": "Recop",
        }

        response = self.client.post(reverse('auto_park_list_create'), auto_park)
        self.assertEqual(AutoParksModel.objects.count(), prev_count)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_auto_park(self):
        self._authenticate()
        prev_count = AutoParksModel.objects.count()
        auto_park = {
            "name": "Recop",
        }

        response = self.client.post(reverse('auto_park_list_create'), auto_park)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Recop')
        self.assertEqual(response.data['cars'], list)
        self.assertEqual(AutoParksModel.objects.count(), prev_count + 1)

    def test_create_car(self):
        prev_count = CarModel.objects.count()
        self._authenticate()
        auto_park = {
            "name": "Recop",
        }
        pk = self.client.post(reverse('auto_park_list_create'), auto_park).data['id']
        car_object = {
            'price': '125425',
            'mark': 'Audi',
            'year': 2022,
            'seats': 5,
            'body_type': 'Large',
            'engine_capacity': 6.5
        }
        length = len(self.client.get(reverse('create_car_in_auto_park', args=(pk,))).data)
        response = self.client.post(reverse('create_car_in_auto_park', args=(pk,)), car_object)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CarModel.objects.count(), prev_count)
        self.assertEqual(len(response.data['cars']), length)
