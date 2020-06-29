from django.shortcuts import render
from AppFour.models import UserInfo

def user_page(request):
    list = UserInfo.objects.order_by('first_name')
    dict = {'user_list':list}
    return render(request, 'AppFour/index.html', context=dict)

def home_page(request):
    return render(request, 'AppFour/index.html')
