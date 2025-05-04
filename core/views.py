from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Group, Code
from .forms import RegisterForm, LoginForm, GroupForm


def register(request):
    form = RegisterForm()

    if request.method == "POST":

        form = RegisterForm(request.POST)
        
        if form.is_valid():

            form.save()

            return redirect('login')
        
    return render(request, 'core/register1.html', {'form': form})
    # return render(request, 'core/register.html', {'form': form})


def login_view(request):
    
    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data= request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username= username , password = password)

            if user is not None:

                login(request, user)

                return redirect("home")

    # return render(request, 'core/login.html' , {'form':form})
    return render(request, 'core/login1.html' , {'form':form})

@login_required
def group_view(request, group_name):
    user = request.user.username

    group = Group.objects.filter(name=group_name).first()
    content = []

    if group:
        content = Code.objects.filter(group= group)

    else:
        group = Group.objects.create(name=group_name)


    # return render(request, 'core/testing.html', {'group_name': group_name, "content" : content, "user" : user})
    return render(request, 'core/dark_working.html', {'group_name': group_name, "content" : content, "user" : user})


@login_required
def logout_view(request):

    logout(request)
    
    return redirect('login')



def homepage(request):
    
    return render(request, 'core/home.html')
    # return render(request, 'core/home2.html')

@login_required
def group_list(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
              # Replace with the appropriate view name
    else:
        form = GroupForm()

    groups = Group.objects.all()

    # return render(request, 'core/group_list.html', {'form': form, "groups" : groups})
    return render(request, 'core/group_list1.html', {'form': form, "groups" : groups})
