from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from vote.models import *
from random import randint

class Command(BaseCommand):
<<<<<<< HEAD

    def handle(self, *a, **kw):
        print('Mocking Data for New website')
        # 1. create users
        USERS = [
=======
    def handle(self, *a, **kw):
        print('Mocking Data for New website')
        # 1. Create User
        users = [
>>>>>>> 069a687a8466ced61d59dca31d2c3200254ad792
            ['a', 'a@ubu.ac.th', 'aaa'],
            ['b', 'b@ubu.ac.th', 'bbb'],
            ['c', 'c@ubu.ac.th', 'ccc'],
            ['d', 'd@ubu.ac.th', 'ddd'],
            ['e', 'e@ubu.ac.th', 'eee'],
        ]
        users = []
<<<<<<< HEAD
        for u in USERS:
            user = User.objects.create_user(u[0], u[1], u[2])
            users.append(user)
        # 2. create questions
        QUESTIONS = [
            'อาชีพที่คาดหวังหลังจากจบการศึกษา',
            'ทักษะที่ยังขาด',
            'ทักษะที่มีแล้ว',
=======
        for u in users:
            user = User.objects.create_user(u[0], u[1], u[2])
            users.append(user)

        # Create Questions
        QUESTIONS = [
            'อาชีพที่คาดหวังหลังจากจบการศึกษา'
            'ทักษะที่ยังขาด'
            'ทักษะที่มีแล้ว'
>>>>>>> 069a687a8466ced61d59dca31d2c3200254ad792
        ]
        questions = []
        for q in QUESTIONS:
            qq = Question(
<<<<<<< HEAD
                user=users[randint(0, len(users)-1)],
                text=q)
            qq.save()
            questions.append(qq)
                



=======
                user = users[randint(len(users))],
                text=q)
            qq.save()
            questions.append(qq)
>>>>>>> 069a687a8466ced61d59dca31d2c3200254ad792
