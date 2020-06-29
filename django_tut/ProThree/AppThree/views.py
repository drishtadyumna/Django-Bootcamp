from django.shortcuts import render

def help(request):
    mydict = {'help' : 'Help Page'}
    return render(request, 'AppThree/help.html', context=mydict)
