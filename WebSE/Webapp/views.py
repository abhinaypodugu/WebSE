from django.shortcuts import render, redirect
from django.views.generic import View
from .models import FoodDonationModel, EventGallery, ActiveEvent, FaqsModel
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FoodDonationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.core.mail import send_mail
import random
# from WebSE import settings
from django.conf import settings
# from geopy.geocoders import Nominatim
# import folium
# import json
# Create your views here.


def index(request):
    # print("iam Here***********************************")

    events = EventGallery.objects.order_by('id')

    active_event = ActiveEvent.objects.get(pk=1)

    faqs1 = FaqsModel.objects.order_by('pk')[0:3]
    faqs2 = FaqsModel.objects.order_by('pk')[3:6]
    faqs3 = FaqsModel.objects.order_by('pk')[6:9]

    mydict = {'events': events, 'active_event': active_event,
              'faqs1': faqs1, 'faqs2': faqs2, 'faqs3': faqs3}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, '*Invalid Credentials')
            return redirect('login')
        else:
            # print("iam Here====================================")
            login(request, user)
    # print(list(render(request, 'Webapp/zero-hunger/index.html', mydict)))

    return render(request, 'Webapp/zero-hunger/index.html', mydict)


def FoodDonationView(request):

    if request.method == 'POST':

        user = request.user
        name_fd = request.POST.get('name_fd', False)
        phone_fd = request.POST.get('phone_fd', False)
        Location_fd = request.POST.get('Location_fd', False)
        # geolocator = Nominatim(user_agent="Webapp")
        # print(geolocator.geocode(Location_fd))
        Amount_fd = request.POST.get('Amount_fd', False)
        FoodType_fd = request.POST.get('FoodType_fd', False)
        Reason_fd = request.POST.get('Reason_fd', False)
        if(len(str(phone_fd)) == 10):
            if user is not None:
                info = FoodDonationModel(user_name=user, name_fd=name_fd, phone_fd=phone_fd, Location_fd=Location_fd,
                                         Amount_fd=Amount_fd, FoodType_fd=FoodType_fd, Reason_fd=Reason_fd)
            else:
                info = FoodDonationModel(name_fd=name_fd, phone_fd=phone_fd, Location_fd=Location_fd,
                                         Amount_fd=Amount_fd, FoodType_fd=FoodType_fd, Reason_fd=Reason_fd)

            info.save()
            messages.success(
                request, "Form Submission Success!! We will contact you soon...")
        else:
            messages.error(
                request, "Invalid Phone Number!! Fill the form again...")
        # obj = index()
        # result = json.loads(obj.readall().decode('utf-8'))
        # print(result)
    return redirect('/')


def loginPage(request):

    return render(request, 'Webapp/zero-hunger/login.html')


def register(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        acc_type = request.POST['acc_type']

        if(password1 == password2):
            if User.objects.filter(email=email).exists():
                print('Email taken')
                messages.info(request, '*Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=name, last_name=acc_type, password=password1, email=email)
                user.save()
                print('user created')
                return redirect('Webapp')
        else:
            messages.info(request, '*Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'Webapp/zero-hunger/register.html')


def Logout(request):
    logout(request)
    return redirect('Webapp')


def profile(request):

    items = FoodDonationModel.objects.filter(user_name=request.user)

    return render(request, 'Webapp/zero-hunger/profile.html', {'items': items})


random = random.randint(1000, 10000)
email = ''


# def pass_reset(request):

#     if request.method == 'POST':

#         password1 = request.POST['new password']
#         password2 = request.POST['Confirm password']
#         username = request.POST['username']
#         user = User.objects.filter(email=email)
#         if username != str(random):
#             messages.info(request, "Incorrect confirmation code")
#             return redirect('pass_reset')
#         elif len(str(password1)) == 0 or len(str(password2)) == 0:
#             messages.info(request, '*Password field cannot be empty')
#             return redirect('pass_reset')
#         elif password1 == password2:
#             user.set_password(password1)
#             messages.info(request, "Password Changed")
#             return redirect('login')
#         else:
#             messages.info(request, '*Passwords do not match')
#             return redirect('pass_reset')
#     else:

#         return render(request, 'Webapp/zero-hunger/password_reset.html')


# def reset(request):
#     password1 = request.POST['new password']
#     password2 = request.POST['Confirm password']
#     username = request.POST['username']

#     obj = User.objects.filter(email=username)
#     if obj is None:
#         messages.info(request, "User does not exist with this email")
#         return redirect('pass_reset')
#     else:
#         send_mail("Password Reset", "Use thus one time code: " +
#                   random, "zerohunger4896@gmail.com", ["username"])

#     if len(str(password1)) == 0 or len(str(password2)) == 0:
#         messages.info(request, '*Password field cannot be empty')
#         return redirect('pass_reset')
#     elif password1 == password2:

#         return redirect('login')
#     else:
#         messages.info(request, '*Passwords do not match')
#         return redirect('pass_reset')


# def verification(request):

#     subject = 'Password Reset'
#     message = "Use this one time code: " + str(random)
#     email_from = settings.EMAIL_HOST_USER

#     if request.method == 'POST':

#         email = request.POST['email']
#         recipient_list = [email, ]
#         # obj = User.objects.filter(email=email)
#         # print((list(obj)))
#         # print(obj.email)
#         if not User.objects.filter(email=email).exists():
#             messages.info(request, "User does not exist with this email")
#             return redirect('verification')
#         else:
#             send_mail(subject, message, email_from, recipient_list)
#             messages.info(request, "mail sent")
#             return redirect('pass_reset')
#     else:
#         return render(request, 'Webapp/zero-hunger/verification.html')
