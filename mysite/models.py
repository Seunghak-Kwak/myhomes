from django.db import models
from django.utils import timezone


class Data (models.Model):
    auto_increment_id = models.AutoField(primary_key=True)

    nickname = models.CharField(max_length=200)
    age = models.CharField(max_length=100, null=True)
    sex = models.CharField(max_length=50, null=True)
    job = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=50, null=True)

    location = models.CharField(max_length=300)
    moving_date = models.CharField(max_length=100, blank=True, null=True)
    deal_type = models.CharField(max_length=100)
    residence_type = models.CharField(max_length=100)
    room_type = models.CharField(max_length=100)
    roomfloor = models.CharField(max_length=100)
    room_size = models.CharField(max_length=100)
    option = models.CharField(max_length=300)

    deposit = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    manage_price = models.CharField(max_length=100)

    detail = models.TextField(null=True)

    published_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nickname
