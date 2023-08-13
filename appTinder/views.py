from django.shortcuts import render,redirect
from .models import User
# Create your views here.


def display_all_users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'index.html', context)


def show_user(request, pk):
    user = User.objects.get(pk=pk)

    return render(request, 'person.html', {"user": user})

def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        email_address = request.POST.get('email_address')
        password = request.POST.get('password')
        self_description = request.POST.get('self_description')
        gender = request.POST.get('gender')

        # Create a new User object
        user = User.objects.create(
            name=name,
            surname=surname,
            age=age,
            email_address=email_address,
            password=password,
            self_description=self_description,
            gender=gender
        )


    return render(request, 'registration.html')
