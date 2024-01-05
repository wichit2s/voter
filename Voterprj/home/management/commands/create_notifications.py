from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from vote.models import *
from home.models import *
from random import randint
from time import sleep

class Command(BaseCommand):
    def handle(self, *a, **kw):
        print('generating sample notifications for user "b"')
        b = User.objects.filter(username='b').first()
        for q in Question.objects.filter(user=b):
            for i in range(3):
                text = f'มีคนโหวตคำถาม "{q.text}" เพิ่ม'
                n = Notification(user=b, text=text)
                n.save()
                print(text)
                sleep(1)
        

