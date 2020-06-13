from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_succesful(self):
        email='jarifrahman@zoho.com'
        password='chichichi1'
        user = get_user_model().objects.create_user(
            email=email,
            password=password)

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normailized(self):
        email= 'jarifrahman@zoho.com'
        user = get_user_model().objects.create_user(email,'jarif')
        d=self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'jarif')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'jarifrahman@zoho.com',
            'chichichi1',

        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    