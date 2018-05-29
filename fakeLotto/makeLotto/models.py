# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now


# Create your models here.
class LottoThisWeek(models.Model):
    number1 = models.IntegerField(default=0)
    number2 = models.IntegerField(default=0)
    number3 = models.IntegerField(default=0)
    number4 = models.IntegerField(default=0)
    number5 = models.IntegerField(default=0)
    number6 = models.IntegerField(default=0)
    isWin = models.IntegerField(default=0)
    createDate = models.DateTimeField(default=now, blank=True)