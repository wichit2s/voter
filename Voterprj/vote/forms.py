from django import forms
from voter.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
