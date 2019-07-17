from django.shortcuts import render,redirect,get_object_or_404, HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, UpdateView, DetailView
from .models import Guestbook, Fcuser
from .forms import GuestbookForm , UpdateGuestbookForm, LoginForm
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

def home(request):
    user_id = request.session.get('user')
    context={}
    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        context['login'] = fcuser.username
        # return HttpResponse(fcuser.username)
        return render(request, 'guestbook/home.html', context)

    return render(request, 'guestbook/home.html', context)


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
    


def register(request):
    if request.method=='GET':
        return render(request, 'guestbook/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username',None)
        useremail = request.POST.get('useremail',None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re-password',None)

        context={}

        if not (username and useremail and password and re_password):
            context['error'] = '모든 값을 입력해야 합니다.'
        elif password != re_password:
            context['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(username=username, useremail=useremail, password=make_password(password))
            fcuser.save()
            return redirect('list')
        
        return render(request, 'guestbook/register.html', context)



def login(request):
    
    if request.method == 'GET':
        return render(request, 'guestbook/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        context = {}

        if not (username and password):
            context['error'] = '모든 값을 입력해야합니다.'
        else:
            fcuser = Fcuser.objects.get(username=username)
            if check_password(password, fcuser.password):
                request.session['user'] = fcuser.id # 자동생성되는 id(pk)값을 넣어줌. 세션처리 끝.
                return redirect('home')
            else:
                context['error'] = '비밀번호가 틀렸습니다.'

        return render(request, 'guestbook/login.html', context)


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('home')