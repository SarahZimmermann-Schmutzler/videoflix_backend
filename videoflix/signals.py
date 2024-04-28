# from .models import Video
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
import os, ssl, smtplib
from email.message import EmailMessage


# @receiver(post_save, sender=Video)
# soll imer ausgeführt werden, wenn Video hochgeladen wurde
# def video_post_safe(sender, instance, created, **kwargs):
    # welche Instanz (Model) hat es gesendet; Video selber (Object); boolean, das anzeigt, ob Object frisch erstellt wurde;
    # print('Video wurde gespeichert')
    # wird immer ausgeführt, wenn gespeichert
    # if created:
    #     print('New video created')
        # wird ausgeführt, wenn Object erstellt wurde

# Funktion verlinken mit @receiver...

@receiver(post_save, sender=User)
def activate_account(sender, instance, created, **kwargs):
    if created:
        # create activation link
        user = instance
        encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
        activation_url = reverse('activate_account', kwargs={'encoded_pk': encoded_pk})
        activation_url = f'localhost:8000{activation_url}'
        # url from hosting-server or localhost:80000
        print('url', activation_url)

        # send mail with link to new user
        email_sender='sarah.zimmermannschmutzler@gmail.com'
        email_password='fcwm hxgp ozew yhph'
        email_receiver=user.email
        subject='VIDEOFLIX Team'
        body=f'Hi {user.username}, here is your activation Link for your VIDEOFLIX Account: http://{activation_url}' 

        em=EmailMessage()
        em['From']=email_sender
        em['To']=email_receiver
        em['Subject']=subject
        em.set_content(body)
        context=ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())