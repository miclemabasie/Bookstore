from logging import INFO
from django.test import TestCase
from django.core import mail
from django.urls.base import reverse
from core import forms
from core.views import ContactUsView

class TestForm(TestCase):
    def test_valid_contact_us_form_sends_email(self):
        form = forms.ContactForm({
            'name': "Miclem Abasie",
            'message': 'Hi there!'
        })
        form1 = forms.ContactForm({
            'name': 'Miclem Luke',
            'message': 'This is a message from luke'
        })
   
        self.assertTrue(form.is_valid())
        self.assertTrue(form1.is_valid())
        with self.assertLogs('core.forms', level='INFO') as cm:
            form.send_mail()
            form.send_mail()
            form1.send_mail()
           

        self.assertNotEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Site message')
       

    def test_invalid_contact_us_form(self):
        form = forms.ContactForm({
            'message': 'This is a bad form'
        })

        self.assertFalse(form.is_valid())


    def test_contact_us_page_works(self):
        response = self.client.get(reverse('core:contact'))
        self.assertContains(response, 'BookTime')
        self.assertTemplateUsed(response, 'contact_form.html')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], forms.ContactForm)