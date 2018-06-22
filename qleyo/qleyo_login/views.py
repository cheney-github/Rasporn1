from django.shortcuts import render
from django.http import HttpResponse
from .models import qadmin
from django.shortcuts import redirect
# Create your views here.


def login(request):
    if request.method == "POST":
        input_user = request.POST['User_id']
        input_pwd = request.POST['password']

        if input_user == 'admin' and input_pwd == "123":
            return redirect("/home")
        else:
            return render(request, 'index.html', {'error': 'User_name invalue！'})


    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')