from django.shortcuts import render
# from AppFour.models import UserInfo
from AppFour.forms import NewUserForm

def user_page(request):
    
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'AppFour/index.html')

        else:
            print('ERROR FORM INVALID')

    return render(request, 'AppFour/index.html', {'form':form})

def home_page(request):
    return render(request, 'AppFour/index.html')
