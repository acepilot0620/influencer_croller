from django.db import models

# Create your models here.

class Search(models.Model):
    search = models.CharField(max_length = 20)

class Youtube_result(models.Model):
    channel_name = models.CharField(max_length = 100)
    subscriber_num =  models.FloatField() 
    not_int_subscriber_num = models.CharField(max_length = 100)
    ten_avg_visit_num = models.CharField(max_length = 100)
    profile_url = models.CharField(max_length = 100)

class Instagram_result(models.Model):
    insta_id = models.CharField(max_length=50)
    profile_url = models.CharField(max_length=100)

    
