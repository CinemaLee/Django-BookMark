
from django.contrib import admin
from django.urls import path, include
from .views import BookmarkList, BookmarkCreate, BookmarkDelete, BookmarkDetail, BookmarkUpdate

# 앱네임 설정으로 다른앱들과 url패턴이 겹치는 것을 방지.
app_name = 'bookmark_2' 

urlpatterns = [
   path('', BookmarkList.as_view(), name='index'),
   path('create/', BookmarkCreate.as_view(), name='create'),
   path('detail/<int:pk>', BookmarkDetail.as_view(), name='detail'), ### 제네릭 뷰 중에서도 디테일,삭제,업데이트는 pk에 의해 불려져야한다. 필수.
   path('delete/<int:pk>', BookmarkDelete.as_view(), name='delete'),
   path('update/<int:pk>', BookmarkUpdate.as_view(), name='update'),
]


