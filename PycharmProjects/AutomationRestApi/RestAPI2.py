import unittest
import requests
import xmltodict
from yaml import load


class PostItemIssue(unittest.TestCase):

    def setUp(self):
        self.settings = load(open('settings.yaml').read())

        self.base_url = self.settings['base_url']

        self.params = {
            'login': self.settings ['credentils']['login'],
            'password': self.settings ['credentils']['psswrd']
        }





        url = self.base_url + '/user/login'
        r = requests.post(url, data=self.params)

        self.cookies = r.cookies


    def test_new_issue(self):
        url = self.base_url + '/issue/'

        params = {
            'project':'API',
            'summery': 'Test summery from robots',
            'description': 'Hail the robots by Denys'
        }

        rec = requests.put(url, data=params, cookies=self.cookies)
        self.assertEqual(rec.status_code, 201)

        issue_id = rec.headers['location'].split('/')[-1]

        self.assertEqual(rec.status_code, 200)







if __name__ == '__main__' :
    unittest.main()


