from rest_framework.views import APIView
from rest_framework.response import Response

import json
from typing import TypedDict

# Реалізовуємо ось такі EndPoints:
#
# GET http://localhost:8000/users           //витягнути всіх юзерів з файлу
# POST http://localhost:8000/users        // записати нового юзера в файл (не забудьте про id, він має бути унікальним)
#
# GET http://localhost:8000/users/<ID>           // витягти юзера по ID
# PUT http://localhost:8000/users/<ID>          // змінити юзера по ID
# DELETE  http://localhost:8000/users/<ID>          // видалити юзера по ID
#
# список юзерів зберігаємо в файлі users.json


UserType = TypedDict('UserType', {'id': int, 'name': str, 'age': int})


class PersistenceManager:
    __file_name = 'users.json'

    @classmethod
    def read_from_file(cls) -> list[UserType]:
        try:
            with open(cls.__file_name) as file:

                return json.load(file)
        except Exception as err:
            print(err)

            return []

    @classmethod
    def write_to_file(cls, data: list[UserType]) -> None:
        try:
            with open(cls.__file_name, mode='w') as file:

                json.dump(data, file)
        except Exception as err:
            print(err)


class UserCreateView(APIView):
    def get(self, *args, **kwargs):
        try:
            users_list = PersistenceManager.read_from_file()

            return Response(users_list)
        except Exception as err:

            return Response({'error': str(err)})

    def post(self, *args, **kwargs):
        try:
            users_list = PersistenceManager.read_from_file()
            new_id: int = users_list[-1]['id'] + 1 if users_list else 1
            data: UserType = self.request.data
            data.update(id=new_id)
            users_list.append(data)
            PersistenceManager.write_to_file(users_list)

            return Response(data)

        except Exception as err:

            return Response({'error': str(err)})


class UserRetrieveDeleteDestroyView(APIView):
    def get(self, *args, **kwargs):
        try:
            users_list: list[UserType] = PersistenceManager.read_from_file()
            user_id: int = kwargs.get('pk')
            user = next(filter(lambda item: item['id'] == user_id, users_list), None)

            if not user:
                return Response('Not Found')

            return Response(user)

        except Exception as err:
            return Response({'error': str(err)})

    def put(self, *args, **kwargs):
        try:
            users_list: list[UserType] = PersistenceManager.read_from_file()
            user_id: int = kwargs.get('pk')
            data: UserType = self.request.data

            index = next((index for index, value in enumerate(users_list) if value['id'] == user_id), None)

            if not index:
                return Response('Not Found')

            user: UserType = {'id': user_id, **data}
            users_list[index] = user
            PersistenceManager.write_to_file(users_list)

            return Response(user)
        except Exception as err:
            return Response({'error': str(err)})

    def delete(self, *args, **kwargs):
        try:
            users_list: list[UserType] = PersistenceManager.read_from_file()
            user_id: int = kwargs.get('pk')

            index = next((index for index, value in enumerate(users_list) if value['id'] == user_id), None)

            if not index:
                return Response('Not Found')

            del users_list[index]
            PersistenceManager.write_to_file(users_list)

        except Exception as err:
            return Response({'error': str(err)})
