from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from vote.models import *
from random import randint

class Command(BaseCommand):
    def handle(self, *a, **kw):
        print('Mocking Data for New website')

        # 1. Create User
        USERS = [
            ['a', 'a@ubu.ac.th', 'aaa'],
            ['b', 'b@ubu.ac.th', 'bbb'],
            ['c', 'c@ubu.ac.th', 'ccc'],
            ['d', 'd@ubu.ac.th', 'ddd'],
            ['e', 'e@ubu.ac.th', 'eee'],
        ]
        users = []
        for u in USERS:
            user, created = User.objects.get_or_create(username=u[0], email=u[1])
            user.set_password(u[2])
            user.save()
            users.append(user)

        # 2. create questions
        QUESTIONS = [
            'อาชีพที่คาดหวังหลังจากจบการศึกษา',
            'ทักษะที่ยังขาด',
            'ทักษะที่มีแล้ว',
        ]
        questions = []
        for q in QUESTIONS:
            qq, created = Question.objects.get_or_create(
                user=users[randint(0, len(users)-1)],
                text=q)
            qq.save()
            questions.append(qq)
                
