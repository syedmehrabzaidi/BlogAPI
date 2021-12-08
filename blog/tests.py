from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from .models import Post, Comments


class HomepageTests(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_homepage_contains_correct_html(self):
        response = self.client.get('/')

        self.assertNotContains(response, 'Homepage', html=True)

    def test_homepage_does_not_contain_incorrect_html(self):  # new
        response = self.client.get('/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')


class PostTests(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(

            email='will@email.com',
            password='testpass123'

        )
        user.set_password('testpass123')
        user.save()
        c = Client()
        logged_in = c.login(email='testuser', password='testpass123')
        self.post = Post.objects.create(
            title='Harry Potter',
            author=get_user_model().objects.get(email='will@email.com'),
            body='25.00',
        )
        self.comments = Comments.objects.create(
            post=self.post,
            author=get_user_model().objects.get(email='will@email.com'),
            comments='An excellent review',
        )

    def test_post_listing(self):
        self.assertEqual(f'{self.post.title}', 'Harry Potter')

        self.assertEqual(f'{self.post.author}', 'will@email.com')
        self.assertEqual(f'{self.post.body}', '25.00')
        self.assertEqual(f'{self.comments}', 'An excellent review')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_list_view_for_logged_in_user(self):  # new
        self.client.login(email='reviewuser@email.com', password='testpass123')

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'home.html')


