from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from vote.models import *
from random import randint

class Command(BaseCommand):

    def handle(self, *a, **kw):
        print('Mocking Data for New website')
        # 1. create users
        USERS = [
            ['a', 'a@ubu.ac.th', 'aaa'],
            ['b', 'b@ubu.ac.th', 'bbb'],
            ['c', 'c@ubu.ac.th', 'ccc'],
            ['d', 'd@ubu.ac.th', 'ddd'],
            ['e', 'e@ubu.ac.th', 'eee'],
        ]
        users = []
        for u in USERS:
            user = User.objects.create_user(u[0], u[1], u[2])
            users.append(user)
        # 2. create questions
        QUESTIONS = [
            'อาชีพที่คาดหวังหลังจากจบการศึกษา',
            'ทักษะที่ยังขาด',
            'ทักษะที่มีแล้ว',
        ]
        questions = []
        for q in QUESTIONS:
            qq = Question(
                user=users[randint(0, len(users)-1)],
                text=q)
            qq.save()
            questions.append(qq)
                



