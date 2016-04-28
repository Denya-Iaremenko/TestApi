import unittest
import requests
import xmltodict
from yaml import load

class BaseAPITest(unittest.TestCase):

    def setUp(self):
        self.settings = load(open('settings.yaml').read())
        self.base_url = self.settings ['base_url']

        self.params = {
            'login': self.settings ['credentils']['login'],
            'password': self.settings ['credentils']['psswrd']
        }

        url = self.base_url + '/user/login/'

        r = requests.put(url, data=self.params)

        self.cookies = r.cookies

        def create_issue(self):

            params = {
                'project':'API',
                'summery': 'sum',
                'description': 'new'
            }

            r = requests.put(self.base_url, data=params, cookies=self.cookeis)
            self.assertEquals(r.status_code, 201)

            issue_id = r.headers['location'].split('/')[-1]
            r = requests.get(self.base_url + issue_id, cookies=self.cookies)
            self.assertEquals(r.status_code, 200)

            return issue_id