from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post


# Create your tests here.
# ... blog/tests.py
...
def test_post_createview(self): # new
  response = self.client.post(
    reverse("post_new"),
    {
      "title": "New title",
      "body": "New text",
      "author": self.user.id,
    },
  )
  self.assertEqual(response.status_code, 302)
  self.assertEqual(Post.objects.last().title, "New title")
  self.assertEqual(Post.objects.last().body, "New text")

def test_post_updateview(self): # new
  response = self.client.post(
    reverse("post_edit", args="1"),
    {
      "title": "Updated title",
      "body": "Updated text",
    },
  )
  self.assertEqual(response.status_code, 302)
  self.assertEqual(Post.objects.last().title, "Updated title")
  self.assertEqual(Post.objects.last().body, "Updated text")

def test_post_deleteview(self): # new
  response = self.client.post(reverse("post_delete", args="1"))
  self.assertEqual(response.status_code, 302)