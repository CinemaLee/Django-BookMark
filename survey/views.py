from django.shortcuts import render
from .models import Survey,Answer

# Create your views here.

def home(request):
    survey = Survey.objects.filter(status='y').order_by('-survey_idx')[0]

    return render(request, 'survey/home.html', {'survey':survey})


def save_survey(request):

    # 문제 번호와 응답번호를 Answer객체에 저장.
    dto = Answer(survey_idx = request.POST['survey_idx'], num=request.POST['num'])
    # insert query가 호출되어 db에 쌓임.
    dto.save()
    return render(request,'survey/success.html')