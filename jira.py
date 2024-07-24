import os

import requests
import json
from base64 import b64encode


class Jira:
    def __init__(self, login: str, password: str, base_url: str):
        self._login = login
        self._password = password
        self._base_url = base_url
        self._token = b64encode(f'{self._login}:{self._password}'.encode('utf-8')).decode('ascii')


    def create(self, project: str, issuetype: str):
        payload = json.dumps({
            "fields": {
                "project": {
                    "key": project
                },
                "summary": "REST ye merry gentlemen.",
                "description": "Creating of an issue using project keys and issue type names using the REST API",
                "issuetype": {
                    "name": issuetype
                }
            }
        })



        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Basic {self._token}',
            'X-Atlassian-Token' : 'no-check'
        }

        response = requests.request("POST", self._base_url + '/rest/api/2/issue/',
                                    headers=headers, data=payload)
        print(response.status_code)
        print(response.json())
        return response.json()['key']


    def add_attach(self):
        payload = {}
        file_name = input('Введите названия файл, который нужно прикрепить с расширением(test.txt): ')
        files = [
            ('file',(file_name, open(file_name, 'rb'), 'text/plain'))
        ]

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Basic {self._token}',
            'X-Atlassian-Token': 'no-check'
        }

        key_issue = input('Введите ключ задачи к которой нужно добавить файл: ')

        response = requests.request("POST", self._base_url + '/rest/api/2/issue/' + key_issue + '/attachments',
                                    headers=headers, data=payload, files=files)
        print(response.status_code)
        print(response.json())
        return  response.json()

