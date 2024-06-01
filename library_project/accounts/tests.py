from django.test import TestCase
from django.urls import reverse

class SignUpViewTests(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_form_errors(self):
        response = self.client.post(reverse('signup'), {})
        form = response.context_data.get('form')
        self.assertTrue(form.is_bound, "The form should be bound")
        self.assertFormError(response, 'form', 'username', 'This field is required.')