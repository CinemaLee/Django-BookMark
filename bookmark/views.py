from django.shortcuts import render
from .models import Bookmark
# Create your views here.

def home(request):

    # select * form bookmark_bookmark order by title  => 이 쿼리가 내부적으로 실행된다는 것. 장고는 함수로 해결한다는 것 뿐.
    urlList = Bookmark.objects.order_by("-title")

    urlCount = Bookmark.objects.all().count()

    return render(request, 'bookmark/list.html', {'urlList':urlList, 'urlCount':urlCount})


def detail(request):

    addr = request.GET['url']

    dto = Bookmark.objects.get(url=addr)

    return render(request, 'bookmark/detail.html', {'dto':dto})



