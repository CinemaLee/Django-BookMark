from django.forms import ModelForm
from django import forms
from .models import Guestbook
from django.utils.translation import gettext_lazy as _



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