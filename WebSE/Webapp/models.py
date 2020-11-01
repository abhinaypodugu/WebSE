from django.db import models
import datetime
# Create your models here.
class FoodDonationModel(models.Model):
    name_fd = models.CharField(max_length=256)
    phone_fd = models.IntegerField()
    Location_fd = models.TextField()
    Amount_fd  = models.IntegerField()
    FoodType_fd = models.CharField(max_length=256)
    Reason_fd = models.CharField(max_length=256)

    def __str__(self):
        return self.name_fd

class EventGallery(models.Model):
    image = models.ImageField(upload_to='pics')
    des = models.CharField(max_length=256)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.date)

class ActiveEvent(models.Model):
    event_name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='eventpics')
    file = models.FileField(upload_to='eventfiles',default="/media/eventfiles/def.pdf")
    place = models.CharField(max_length=128)
    message = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.event_name
