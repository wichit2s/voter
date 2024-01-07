from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from vote.models import *
from openpyxl import load_workbook

class Command(BaseCommand):
    def load_users(self, sheetname='User'):
        ### 'username', 'email', 'password', 'is_staff', 'is_superuser'
        # ['a', 'a@ubu.ac.th', 'aaa', 1, 1 ],
        # ['b', 'b@ubu.ac.th', 'bbb', 1, 0 ],
        # ['c', 'c@ubu.ac.th', 'ccc', 0, 0 ],
        # ['d', 'd@ubu.ac.th', 'ddd', 0, 0 ],
        # ['e', 'e@ubu.ac.th', 'eee', 0, 0 ],
        sh = self.wb[sheetname]
        obj_list = []
        for row in sh:
            values = [ cell.value for cell in row ]
            print(values)
            obj, created = User.objects.get_or_create(username=values[0], email=values[1])
            obj.set_password(values[2])
            if bool(values[3]): # 1, 0
                obj.is_staff = True
            if bool(values[4]): # 1, 0
                obj.is_superuser = True
            obj.save()
            obj_list.append(obj)
        return obj_list
        
    def load_questions(self, sheetname='Question'):
        ### 'user', text'
        # 'a', 'อาชีพที่คาดหวังหลังจากจบการศึกษา',
        # 'a', 'ทักษะที่ยังขาด',
        # 'b', 'ทักษะที่มีแล้ว',
        sh = self.wb[sheetname]
        obj_list = []
        for row in sh:
            values = [ cell.value for cell in row ]
            print(values)
            obj, created = Question.objects.get_or_create(
                user=User.objects.filter(username=values[0]).first(),
                text=values[1])
            obj.save()
            obj_list.append(obj)
        return obj_list

    def load_answers(self, sheetname='Answer'):
        ### 'user', question', 'text', 'count'
        # [1, 1, 'programmer', 2],
        # [2, 1, 'data scientist', 3],
        # [3, 1, 'web developer', 1],
        # [2, 2, 'C#', 2],
        # [4, 2, 'JavaScript', 4],
        sh = self.wb[sheetname]
        obj_list = []
        for row in sh:
            values = [ cell.value for cell in row ]
            print(values)
            u = User.objects.get(pk=values[0])
            q = Question.objects.get(pk=values[1])
            obj, created = Answer.objects.get_or_create(user=u, question=q, text=values[2])
            obj.count = values[3]
            obj.save()
            obj_list.append(obj)
        return obj_list

    def handle(self, *a, **kw):
        print('Loading Data from "vote/fixtures/data.xlsx" ')
        self.wb = load_workbook('vote/fixtures/data.xlsx')
        self.users = self.load_users()
        self.questions = self.load_questions()
        self.answers = self.load_answers()

