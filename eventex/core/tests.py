#coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
class HomepageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:homepage'))

    def test_get(self):
        'Get / must return status cod 200.'
        self.assertEqual(200, self.resp.status_code)
        
    def test_template(self):
        'Homepage must use template index.html.'
        self.assertTemplateUsed(self.resp, 'index.html')
