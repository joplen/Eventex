# coding: utf-8
from django.contrib.auth import get_user_model
from django.test import TestCase
from eventex.myauth.backends import EmailBackend

class EmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='joao',
                                      email='joao@guedes.eu',
                                      password='abcdef')
        self.backend = EmailBackend()

    def test_authenticate_with_email(self):
        user = self.backend.authenticate(email='joao@guedes.eu',
                                         password='abcdef')
        self.assertIsNotNone(user)

    def test_wrong_password(self):
        user = self.backend.authenticate(email='joao@guedes.eu',
                                         password='wrong')
        self.assertIsNone(user)

    def test_unknown_user(self):
        user = self.backend.authenticate(email='unknown@email.com',
                                         password='abcdef')
        self.assertIsNone(user)

    def test_get_user(self):
        self.assertIsNotNone(self.backend.get_user(1))

class MultipleEmailsTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='user1',
            email='joao@guedes.eu', password='abcdef')
        UserModel.objects.create_user(username='user2',
            email='joao@guedes.eu', password='abcdef')
        self.backend = EmailBackend()

    def test_multiple_email(self):
        user = self.backend.authenticate(email='joao@guedes.eu',
                                         password='abcdef')
        self.assertIsNone(user)

class FunctionalEmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='joao',
                                      email='joao@guedes.eu',
                                      password='abcdef')
        
        def test_login_with_email(self):
            result = self.client.login(email='joao@guedes.eu',
                                       password='abcdef')
            self.assertTrue(result)

        def test_login_with_username(self):
            result = self.client.login(username='joao@guedes.eu',
                                       password='abcdef')
            self.assertTrue(result)
            
