from django.shortcuts import render,redirect,get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, UpdateView, DetailView
from .models import Guestbook
from .forms import GuestbookForm , UpdateGuestbookForm

# Create your views here.

def list(request):
    itemlist = Guestbook.objects.order_by('-idx')
    itemcount = Guestbook.objects.count()

    context = {
        'itemlist':itemlist, 'itemcount':itemcount
    }
    return render(request,'guestbook/list.html',context)

    

def write(request):
    if request.method== 'GET':
        form = GuestbookForm()
        return render(request,'guestbook/write.html', {'form':form})
    else:
        form = GuestbookForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return redirect('list')


def update(request, id):

    if request.method == 'POST' and 'form_id' in request.POST: # 업데이트가 완료된 데이터가 들어오는 경우.
        # item = Guestbook.objects.get(pk=request.POST.get('id')) # 어떤 놈을 수정하려고 했는지 그 id값을 추출함.
        item = get_object_or_404(Guestbook, pk=request.POST.get('form_id')) # id가 존재하지 않을 경우 페이지 없음이 뜸.
        password = request.POST.get('passwd','') # 비번이 제대로 넘어왔다면 password가 들어가고 없다면 ''이 들어감.
        form = UpdateGuestbookForm(request.POST, instance=item) # 수정이 완료된 폼 데이터가 대입이되고, 이 새로운 데이터는 instance꺼라는 의미. 이 instance가 없다면?? 새로운 pk로 저장됨. 추가가 된다는 뜻.
        if form.is_valid() and password == item.passwd: # 유효하고 비밀번호가 같다면
            item = form.save() # 디비에 수정/저장.
        else:
            return redirect('update', id=id)
        

    elif request.method=='GET': # get으로 들어온 경우. 즉 update화면이 보여지는 경우.
        # item = Guestbook.objects.get(pk=request.GET.get('id')) # /third/update?id=2 이런식으로 직접 들어오는 경우. 
        item = get_object_or_404(Guestbook, pk=id) 
        form = GuestbookForm(instance=item)
        return render(request, 'guestbook/update.html', {'form':form})

    return redirect('list')



def delete(request, id):
    item = get_object_or_404(Guestbook, pk=id)
    # post방식으로 들어올 때
    if request.method == 'POST' and 'password' in request.POST:
        if item.passwd == request.POST.get('password') or item.passwd is None:
            item.delete()
            return redirect('list')
        return redirect('delete', id=id)

    # get방식으로 들어올 때
    return render(request, 'guestbook/delete.html', {'item':item})
    
