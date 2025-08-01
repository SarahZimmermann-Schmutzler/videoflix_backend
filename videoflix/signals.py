from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
import os, ssl, smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
from videoflix.models import Video
from videoflix.tasks import convert_1080p, convert_720p, convert_480p
import django_rq


@receiver(post_save, sender=Video)
def video_post_safe(sender, instance, created, **kwargs):
    # which instance (Model) sent it; video itself (Object); boolean that indicates whether Object was newly created;
    """
    After a video is uploaded, it's automatically converted in 1080p, 720p and 480p.
    """
    print('Video wurde gespeichert')
    # is always executed when saved
    if created:
        print('New video created')
        # is executed when Object is created
        if instance.video_file:
            # Convert in the background
            queue = django_rq.get_queue('default', autocommit=True)
            queue.enqueue(convert_1080p, instance.video_file.path)
            queue.enqueue(convert_720p, instance.video_file.path)
            queue.enqueue(convert_480p, instance.video_file.path)
            # Convert in the foreground
            # convert_1080p(instance.video_file.path)
            # convert_720p(instance.video_file.path)
            # convert_480p(instance.video_file.path)


@receiver(post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    After a video is deleted, it's automatically deleted from the media folder.
    """
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)
    
    if instance.preview_img:
        os.remove(instance.preview_img.path)


@receiver(post_save, sender=User)
def activate_account(sender, instance, created, **kwargs):
    """
    After a User is registered, it sends an activation mail.
    """
    load_dotenv()

    if created:
        # create activation link
        user = instance
        encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
        # activation_url = f'http://localhost:4200/activateAccount/{encoded_pk}'
        activation_url = f'https://{os.getenv('ACTIVATION_URL')}/activateAccount/{encoded_pk}'
        # url from frontend
        print('url', activation_url)

        # send mail with link to new user
        email_sender=os.getenv('EMAIL_SENDER')
        
        email_password=os.getenv('GMAIL_PWD')
        email_receiver=user.email
        subject='VIDEOFLIX Team'
        body=f'Hi {user.username}, here is your activation Link for your VIDEOFLIX Account: {activation_url}' 

        em=EmailMessage()
        em['From']=email_sender
        em['To']=email_receiver
        em['Subject']=subject
        em.set_content(body)
        
        context=ssl.create_default_context()

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls(context=context)
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())