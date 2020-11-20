from django.contrib import admin
from Webapp.models import FoodDonationModel,EventGallery,ActiveEvent,FaqsModel

# Register your models here.

admin.site.register(FoodDonationModel)
admin.site.register(EventGallery)
admin.site.register(ActiveEvent)
admin.site.register(FaqsModel)
