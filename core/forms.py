from django import forms
import logging
from django.core.mail import send_mail

from Bookshop.settings import DEBUG

logging.basicConfig(level=DEBUG)
logger = logging.getLogger(__name__)

class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    message = forms.CharField(max_length=600, widget=forms.Textarea)


    def send_mail(self):
        logger.info("Sending email to customer service")
        message = f"From: {self.cleaned_data.get('name')}, {self.cleaned_data.get('message')}"

        send_mail(
            "Site message",
            message,
            "site@booktime.domain",
            ["customerserveic@booktime.domain"],
            fail_silently=False
        )
