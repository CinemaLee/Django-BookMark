from django.db import models
from datetime import datetime

# Create your models here.

# 방명록 테이블 생성
class Guestbook(models.Model):
    # 자동 증가 일련번호 필드(int로 저장.)
    idx = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    email = models.EmailField(max_length=100)
    passwd = models.CharField(null=False, max_length=50)
    content = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    post_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class Fcuser(models.Model):
    username = models.CharField(max_length=50)
    useremail = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = '유저'

    