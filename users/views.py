from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from . forms  import UserRegistrationForm
from django.contrib.auth.models import User

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             return redirect('/')
#
#     else :
#         form = UserRegistrationForm()
#     return render(request,'users/register.html',{'form':form})
#



def register_V2(request):
    errorMessage = ''

    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName  = request.POST.get('LastName')
        email     = request.POST.get('email')
        userName  = request.POST.get('UserName')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print(f' Пароли {password1} {password2}')

        if password1 != password2 :
            errorMessage = "Пароли не совпадают"
        else :

            newUser = User(first_name = firstName,
                            last_name = lastName,
                            email = email,
                            username = userName)

            newUser.set_password(password1)
            newUser.save()




    return render(request,'users/register.html',{'Wrong_Password':errorMessage})
