from django.core.mail import EmailMessage
from django.conf import settings as conf_settings
from django.template.loader import render_to_string
from django.core.mail import send_mail 
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
import uuid
import threading
import random
from .models import *

class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class Util:
    
    @staticmethod
    def send_email(request,user):
        mail_from = conf_settings.EMAIL_HOST_USER
        mail_to = user
        context_data = {
        'mail_from':mail_from,
        'mail_to': mail_to,
        }
        text_content = render_to_string('{0}/templates/webapp/singup_email.html'.format(conf_settings.BASE_DIR), context=context_data)
        email = EmailMultiAlternatives("Thank you for enquiry", text_content, conf_settings.EMAIL_HOST_USER, [mail_to])
        print('ggkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk',email)
        email.attach_alternative(text_content, 'text/html')
        EmailThread(email).start()


        mail_from = conf_settings.EMAIL_HOST_USER
        mail_to = "mohitpatidar.1998.24@gmail.com"
        context_data = {
        'mail_from':mail_from,
        'mail_to': mail_to,
        }
        text_content = render_to_string('{0}/templates/webapp/singup_email.html'.format(conf_settings.BASE_DIR), context=context_data)
        email = EmailMultiAlternatives("Thank you for enquiry", text_content, conf_settings.EMAIL_HOST_USER, [mail_to])
        print('ggkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk',email)
        email.attach_alternative(text_content, 'text/html')
        EmailThread(email).start()

    @staticmethod
    def forget_email(data):
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        EmailThread(email).start()
    


    @staticmethod
    def user_email_verfication(request,user,otp):
        mail_from = conf_settings.EMAIL_HOST_USER
        mail_to = user.email
        
        context_data = {
        'mail_from':mail_from,
        'mail_to': mail_to,
         'otp':otp,
    
        }
        text_content = render_to_string('{0}/templates/client/email/otp_mail.html'.format(conf_settings.BASE_DIR), context=context_data)
        email = EmailMultiAlternatives("Email Verification ", text_content, conf_settings.EMAIL_HOST_USER, [mail_to])
        email.attach_alternative(text_content, 'text/html')
        EmailThread(email).start()
    


    @staticmethod
    def email_verfication(request,user,otp):
        mail_from = conf_settings.EMAIL_HOST_USER
        mail_to = user
        
        context_data = {
        'mail_from':mail_from,
        'mail_to': mail_to,
         'otp':otp,
    
        }
        text_content = render_to_string('{0}/templates/client/email/otp_mail.html'.format(conf_settings.BASE_DIR), context=context_data)
        email = EmailMultiAlternatives("Email Verification ", text_content, conf_settings.EMAIL_HOST_USER, [mail_to])
        email.attach_alternative(text_content, 'text/html')
        EmailThread(email).start()



      
   

    @staticmethod
    def depositotp(request,user,otp):
         
         mail_from = conf_settings.EMAIL_HOST_USER
         mail_to = user
         context_data = {
        'mail_from':mail_from,
        'mail_to': mail_to,
         'otp':otp,
          }
         text_content = render_to_string('{0}/templates/client/email/otp_mail.html'.format(conf_settings.BASE_DIR), context=context_data)
         email = EmailMultiAlternatives("Email Verification ", text_content, conf_settings.EMAIL_HOST_USER, [mail_to])
         email.attach_alternative(text_content, 'text/html')
         EmailThread(email).start()

       

   






