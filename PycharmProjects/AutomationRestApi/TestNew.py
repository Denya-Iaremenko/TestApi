import unittest
import requests
import xmltodict
from yaml import load
from base_test import BaseApiTest

class TestDeleteIssue(BaseApiTest):

    def setUp(self):
        super(TestDeleteIssue, self).setUp()
        self.url = self.base_url +'/issue/'





    def tes_delete_issue(self):
        issue_id = self.create_issue()
        r = requests.delete(self.url+ issue_id, cookies=self.cookies )
        self.assertEqual()




if __name__ == '__main__' :
    unittest.main()