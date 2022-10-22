from django.core.management.base import BaseCommand
from urllib.parse import urljoin
from django.conf import settings
import requests


class Command(BaseCommand):
    help = 'Пример загрузки данных через REST API'

    def add_arguments(self, parser):
        parser.add_argument('--username', '-u', dest='username', help='Имя пользователя')
        parser.add_argument('--password', '-p', dest='password')
        # python3 manage.py load_tags -u user_example -p 12345678

    def handle(self, *args, **options):    # команда для вызова: python3 manage.py load_tags
        login_url = urljoin(settings.MY_EXTERNAL_SERVICE, '/user/login/')
        response = requests.post(login_url, data={
            'username': options['username'],
            'password': options['password'],
        })
        response.raise_for_status()

        token = response.json()['token']
        tags_url = urljoin(settings.MY_EXTERNAL_SERVICE, '/tags/')
        response = requests.get(tags_url, headers={'Authorization': f'Token {token}'})
        response.raise_for_status()

        for t in response.json():
            print(t['name'])

