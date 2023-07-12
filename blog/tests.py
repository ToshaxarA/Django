from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpRequest
from django.shortcuts import render
from blog.models import Post
request = HttpRequest

class BlogTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(title="test",content="test")

    
        
    def test_index(self):
        response = self.client.get(reverse("index-page"))
        
        self.assertTemplateUsed("blog/index.html")
        
        self.assertIn('Главная страница', response.content.decode())

    
    def test_contacts(self):
        response = self.client.get(reverse("contacts-page"))
        self.assertTemplateUsed("blog/contacts.html")
        self.assertIn('Контакты', response.content.decode())

    def test_about(self):
        response = self.client.get(reverse("about-page"))
        self.assertTemplateUsed("blog/about.html")
        self.assertIn('Страница о нас', response.content.decode())

    def test_post_udate(self):
        response = self.client.get(reverse("post-update", args=(1,)))
        self.assertTemplateUsed("blog/post_update.html")
        self.assertEqual(response.status_code, 200)
    
    def test_post_delete(self):
        response = self.client.get(reverse("post-delete", args=(1,)))
        self.assertTemplateUsed("blog/post_delete.html")
        self.assertEqual(response.status_code, 200)

    
