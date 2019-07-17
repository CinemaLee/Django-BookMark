from django.forms import ModelForm
from django import forms
from .models import Guestbook, Fcuser
from django.utils.translation import gettext_lazy as _

# 폼을 사용하는 이유??? 기본적으로 유효성 검사를 쉽게 해주고, 악의적인 데이터를 필터링 해준다.(sanitisation)

class LoginForm(ModelForm):
    class Meta:
        model = Fcuser
        fields = ['username', 'password']

        help_texts = {
            'username':_('아이디를 입력해주세요'),
            'password':_('비밀번호를 입력해주세요'),
        }
        widgets={
            'password':forms.PasswordInput()
        }


class GuestbookForm(ModelForm):
    class Meta:
        model = Guestbook
        fields = ['name', 'email', 'passwd', 'content']

        help_texts = {
            'name':_('이름을 입력해주세요'),
            'email':_('이메일을 입력해주세요'),
            'passwd':_('비밀번호를 입력해주세요'),
            'content':_('내용을 입력해주세요'),
        }

        widgets={
            'passwd':forms.PasswordInput()
        }

        error_messages = {
            'name': {
                'max_length':_('이름이 너무 깁니다. 30자 이하로 해주세요.')
            },
           
            'passwd': {
                'max_length':_('비밀번호가 너무 깁니다. 20자 이하로 해주세요.')
            },
        }


class UpdateGuestbookForm(GuestbookForm):
    class Meta:
        model = Guestbook
        exclude = ['passwd']