from django.db import models
from django.contrib.auth.models import User
import datetime
from django.conf import settings

# Create your models here.


class FoodDonationModel(models.Model):
    name_fd = models.CharField(max_length=256)
    phone_fd = models.IntegerField()
    Location_fd = models.TextField()
    Amount_fd = models.IntegerField()
    FoodType_fd = models.CharField(max_length=256)
    Reason_fd = models.CharField(max_length=256)
    user_name = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name_fd


class FoodRequestModel(models.Model):
    name_req = models.CharField(max_length=256)
    phone_req = models.IntegerField()
    Location_req = models.TextField()
    persons_req = models.IntegerField()
    user_name = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name_req


class EventGallery(models.Model):
    image = models.ImageField(upload_to='pics')
    des = models.CharField(max_length=256)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.date)


class ActiveEvent(models.Model):
    event_name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='eventpics')
    file = models.FileField(upload_to='eventfiles',
                            default="/media/eventfiles/def.pdf")
    place = models.CharField(max_length=128)
    message = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.event_name


class FaqsModel(models.Model):
    question = models.CharField(max_length=512)
    answer = models.TextField()
    tag = models.CharField(max_length=128, default="One")

    def __str__(self):
        return str(self.id)
