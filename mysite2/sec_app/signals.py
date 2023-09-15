from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.conf import settings
from sec_app.models import Movement
from sec_app.forms import mat_mov
from django.urls import reverse
from django.template.loader import render_to_string

@receiver(post_save, sender=Movement)
def send_verification_emails(sender, instance, **kwargs):
    # Accessing fields of the instance
    level_one_approval = instance.Level_one_approval
    level_two_approval = instance.Level_two_approval

    # Create an instance of the form and populate it with data
    form = mat_mov(instance=instance)

    # Render the form as HTML content
    form_html = form.as_table()

    # Create HTML content for the buttons with relative URLs
    verify_url = f"/verify/{instance.id}/"
    reject_url = f"/reject/{instance.id}/"
    button_html = f'<a href="{verify_url}">Verify</a> | <a href="{reject_url}">Reject</a>'

    # Combine the form content and buttons
    email_html = f'{form_html}<br>{button_html}'

    # Create an EmailMultiAlternatives object
    subject = 'Verification Email'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [level_one_approval, level_two_approval]

    # Create a plain text version of the email content
    text_message = 'Please verify your submission.'

    # Create the email message
    msg = EmailMultiAlternatives(subject, text_message, from_email, recipient_list)

    # Attach the email content as HTML
    msg.attach_alternative(email_html, "text/html")

    # Send the email
    msg.send()

    print("Verification email sent")