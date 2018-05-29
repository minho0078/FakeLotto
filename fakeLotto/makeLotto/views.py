# -*- coding: utf-8 -*-
from .models import *
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import json


# Create your views here.
def index(request):
    name = 'minho'
    return render(request, 'makeLotto/index.html', {'name':name})


def insert(request):
    print(request.GET.get("number1"))

    lotto = LottoThisWeek(number1=request.GET.get("number1"),
                          number2=request.GET.get("number2"),
                          number3=request.GET.get("number3"),
                          number4=request.GET.get("number4"),
                          number5=request.GET.get("number5"),
                          number6=request.GET.get("number6"),
                          isWin=0,
                          createDate=datetime.now())
    lotto.save()

    return HttpResponse("success")


def winner(request):
    soup = parser("http://www.nlotto.co.kr/gameResult.do?method=byWin")
    lotto = soup.select("p[class=number]").__getitem__(0).find_all("img", attrs={"alt":True})
    lotto_numbers = []
    for imgTag in lotto:
        lotto_numbers.append(imgTag.get("alt"))

    return HttpResponse(json.dumps(lotto_numbers, sort_keys=True))


def no_view(request):
    soup = parser("http://www.nlotto.co.kr/gameResult.do?method=noViewNumber&sltPeriod="+request.GET.get('period'))
    array_td = soup.select("tbody")[0].findChildren("img", attrs={"alt":True})
    no_view_lotto_numbers = []

    for imgTag in array_td:

        no_view_lotto_numbers.append(str(imgTag.get("alt")).replace("번", ""))
    print(array_td[0].get("alt"))
    return HttpResponse(json.dumps(no_view_lotto_numbers, sort_keys=True))

def parser(url):
    html = requests.get(url).text
    return BeautifulSoup(html, 'html.parser')