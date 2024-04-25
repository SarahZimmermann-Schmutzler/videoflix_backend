# from .models import Video
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# @receiver(post_save, sender=Video)
# soll imer ausgeführt werden, wenn Video hochgeladen wurde
# def video_post_safe(sender, instance, created, **kwargs):
    # welche Instanz (Model) hat es gesendet; Video selber (Object); boolean, das anzeigt, ob Object frisch erstellt wurde;
    # print('Video wurde gespeichert')
    # wird immer ausgeführt, wenn gespeichert
    # if created:
    #     print('New video created')
        # wird ausgeführt, wenn Object erstellt wurde

# Funktion verlinken
