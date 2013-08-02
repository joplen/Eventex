#coding: utf-8

from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'João Guedes',
            cpf = '12345678901',
            email = 'joao@guedes.eu',
            phone = '15-12121212'
            )

    def test_creat(self):
        'Subscription must have name, cpf, email, phone'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def tes_unicode(self):
        self.assertEqual(u'João Guedes', unicode(self.obj))


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        Subscription.objects.create(name='João Guedes', cpf='12345678901',
                                     email='joao@guedes.eu', phone='15-12121212')
    def test_cpf_unique(self):
        'CPF must be unique'
        s = Subscription(name='João Guedes', cpf='12345678901',
                         email='outro@email.com',phone='15-12121212')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        'Email must be unique'
        s = Subscription(name='João Guedes', cpf='00000000011',
                         email='joao@guedes.eu',phone='15-12121212')
        self.assertRaises(IntegrityError, s.save)


        
