from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpRequest
from django.shortcuts import render
request = HttpRequest

class BlogTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_index(self):
        response = self.client.get(reverse("index-page"))
        
        self.assertIn('Главная страница', response.content.decode())

    
    def test_contacts(self):
        response = self.client.get(reverse("contacts-page"))
        
        self.assertIn('Контакты', response.content.decode())

    def test_about(self):
        response = self.client.get(reverse("about-page"))
        
        self.assertIn('Страница о нас', response.content.decode())
    

    
