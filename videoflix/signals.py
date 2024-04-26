# from .models import Video
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

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
        user = instance
        print('NewUser angelegt', user.email)
        encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
        activation_url = reverse('activate_account', kwargs={'encoded_pk': encoded_pk})
        activation_url = f'localhost:8000{activation_url}'
        print('url', activation_url)