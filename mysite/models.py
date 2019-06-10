from django.db import models
from django.utils import timezone

class Data (models.Model):
    data_id = models.AutoField(primary_key=True)

    nickname = models.CharField(max_length=200)
    contact = models.CharField(max_length=50, null=True)

    location = models.CharField(max_length=300)
    moving_date = models.CharField(max_length=100, blank=True, null=True)
    deal_type = models.CharField(max_length=100,help_text='거주유형')
    residence_type = models.CharField(max_length=100,help_text='건물형태')
    room_type = models.CharField(max_length=100)
    roomfloor = models.CharField(max_length=100)
    room_size = models.CharField(max_length=100)
    option = models.CharField(max_length=300)

    deposit = models.CharField(max_length=200,help_text='보증금')
    monthly_price = models.CharField(max_length=200,help_text='월세')
    manage_price = models.CharField(max_length=100)

    age = models.CharField(max_length=100, null=True)


    """sex_type = (
        ('m','남자'),
        ('f','여자'),
        )

    sex = models.CharField(max_length=1, choices=sex_type, null=True)"""
    sex = models.CharField(max_length=30, null=True)
    job = models.CharField(max_length=50, null=True)

    detail = models.TextField(null=True)

    enroll_date = models.DateTimeField(
            default=timezone.now)

    class Meta:
        ordering = ['-enroll_date']

    def __str__(self):
        return self.nickname
