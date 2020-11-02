from django.shortcuts import render,redirect
from django.views.generic import View
from Webapp.models import FoodDonationModel,EventGallery,ActiveEvent,FaqsModel
from django.http import HttpResponse,HttpResponseRedirect
from .forms import FoodDonationForm
from django.contrib import messages

# Create your views here.
def index(request):
    # TODO: get image elements and make page dynamic
    events = EventGallery.objects.order_by('id')

    active_event = ActiveEvent.objects.get(pk=1)

    faqs1 = FaqsModel.objects.order_by('pk')[0:3]
    faqs2 = FaqsModel.objects.order_by('pk')[3:6]
    faqs3 = FaqsModel.objects.order_by('pk')[6:9]

    return render(request,'Webapp/zero-hunger/index.html',{'events':events, 'active_event':active_event , 'faqs1':faqs1, 'faqs2':faqs2, 'faqs3':faqs3})

def FoodDonationView(request):

    name_fd = request.POST.get('name_fd',False)
    phone_fd = request.POST.get('phone_fd',False)
    Location_fd = request.POST.get('Location_fd',False)
    Amount_fd = request.POST.get('Amount_fd',False)
    FoodType_fd = request.POST.get('FoodType_fd',False)
    Reason_fd = request.POST.get('Reason_fd',False)
    if(len(str(phone_fd))==10):
        info = FoodDonationModel(name_fd=name_fd , phone_fd=phone_fd , Location_fd=Location_fd , Amount_fd=Amount_fd , FoodType_fd = FoodType_fd , Reason_fd = Reason_fd)
        info.save()
        messages.success(request,"Form Submission Success!! We will contact you soon...")
    else:
        messages.error(request,"Invalid Phone Number!! Fill the form again...")
    return redirect('/')
