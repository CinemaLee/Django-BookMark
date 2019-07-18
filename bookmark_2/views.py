from django.shortcuts import render
from .models import Bookmark
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView

from django.utils.translation import gettext_lazy as _

# Create your views here.

# 클래스형 뷰의 특징. 특별한 로직이 필요없음. 안에 다 내장되어있음.

class BookmarkList(ListView): # object_list 반환
    model = Bookmark


class BookmarkCreate(CreateView): # form 반환
    model = Bookmark
    fields = ['site_name', 'url', 'content']
    template_name_suffix = '_create' # 이후 연결될 템플릿 이름은 bookmark_create일 것이다라고 장고에게 알려주는 부분.
    success_url = '/bookmark_2' # 성공하면 메인 페이지로 돌아가도록 연결한다.


class BookmarkDetail(DetailView): # 특정 pk로 object를 반환.
    model = Bookmark
    template_name_suffix = '_detail'


class BookmarkUpdate(UpdateView): # 특정 pk로 form을 반환.
    model = Bookmark
    fields = ['site_name', 'url', 'content']
    template_name_suffix = '_update'
    success_url = '/bookmark_2'

class BookmarkDelete(DeleteView): # 특정 pk로 object를 반환.
    model = Bookmark
    template_name_suffix = '_delete'
    success_url = '/bookmark_2'