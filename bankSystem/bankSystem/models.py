from django.db import models


class customers_Data(models.Model):
    # sNum = models.IntegerField()
    name = models.CharField(max_length=50)
    emailId = models.CharField(max_length=70)
    accountNumber = models.IntegerField()
    balance = models.FloatField()



class Payment(models.Model):
    userAccountNumber = models.IntegerField()
    amount = models.FloatField()