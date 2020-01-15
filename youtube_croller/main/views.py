#크롤링을 위한 import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.parse
import time
from youtube_croller import parse


from django.shortcuts import render,redirect, HttpResponse
from .models import Result,Search

# Create your views here.

def main(request):
    if request.method == 'POST':
        search = request.POST.get('search_youtube')
        condition = request.POST.get('condition')
        condition = int(condition)
        result_list = parse.croller(search)
        i = 1
        for node in result_list:
            result = Result()
            result.id = i
            result.channel_name = node.channel_name
            result.subscriber_num = node.subscriber_num
            result.not_int_subscriber_num = node.not_int_subscriber_num
            result.ten_avg_visit_num = node.channel_avg_visit_num
            result.profile_url = node.profile_url
            result.save()
            i +=1
        result_all = Result.objects.all()
        return render(request,'youtube_result.html',{'search':search, 'result':result_all, 'condition':condition})
    return render(request,'main.html')


def go_back_and_clean(request):
    old_result = Result.objects.all()
    old_result.delete()
    return redirect('home')

    

    



        














