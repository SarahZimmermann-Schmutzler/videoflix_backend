from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
import os, ssl, smtplib
from email.message import EmailMessage
from videoflix.models import Video
from videoflix.tasks import convert_1080p, convert_720p, convert_480p
import django_rq


@receiver(post_save, sender=Video)
# soll imer ausgeführt werden, wenn Video hochgeladen wurde
def video_post_safe(sender, instance, created, **kwargs):
    # welche Instanz (Model) hat es gesendet; Video selber (Object); boolean, das anzeigt, ob Object frisch erstellt wurde;
    print('Video wurde gespeichert')
    # wird immer ausgeführt, wenn gespeichert
    if created:
        print('New video created')
        # wird ausgeführt, wenn Object erstellt wurde
        if instance.video_file:
            # im Hintergrund konvertieren
            queue = django_rq.get_queue('default', autocommit=True)
            queue.enqueue(convert_1080p, instance.video_file.path)
            queue.enqueue(convert_720p, instance.video_file.path)
            queue.enqueue(convert_480p, instance.video_file.path)
            # im Vordergrund konvertieren
            # convert_1080p(instance.video_file.path)
            # convert_720p(instance.video_file.path)
            # convert_480p(instance.video_file.path)



# deletes media from hard disk after video was deleted from server/backend
@receiver(post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)
    
    if instance.preview_img:
        os.remove(instance.preview_img.path)


# sends activation mail after new user was registered
@receiver(post_save, sender=User)
def activate_account(sender, instance, created, **kwargs):
    if created:
        # create activation link
        user = instance
        encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
        # activation_url = f'http://localhost:4200/activateAccount/{encoded_pk}'
        activation_url = f'https://videoflix.s-zimmermann-schmutzler.de/activateAccount/{encoded_pk}'
        # url from frontend
        print('url', activation_url)

        # send mail with link to new user
        email_sender='sarah.zimmermannschmutzler@gmail.com'
        email_password=os.environ.get('GMAIL_PWD')
        email_receiver=user.email
        subject='VIDEOFLIX Team'
        body=f'Hi {user.username}, here is your activation Link for your VIDEOFLIX Account: {activation_url}' 

        em=EmailMessage()
        em['From']=email_sender
        em['To']=email_receiver
        em['Subject']=subject
        em.set_content(body)
        context=ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())