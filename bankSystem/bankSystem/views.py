from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import customers_Data, Payment
from django.db import transaction

def home(request):
    return render(request,'index.html')


def customersData(request):
    saveCustomerData = customers_Data.objects.all()
    return render(request,'customersData.html', {'data':saveCustomerData})


def transferMoney(request):
    if request.method == "POST":
        try:
            sender = request.POST.get("sender")
            receiver = request.POST.get("receiver")
            amount = request.POST.get("amount")

            with transaction.atomic():
                sender_obj = customers_Data.objects.get(accountNumber = sender)
                sender_obj.balance -= float(amount)
                sender_obj.save()


                receiver_obj =  customers_Data.objects.get(accountNumber = receiver)
                receiver_obj.balance += float(amount)
                receiver_obj.save()
                messages.success(request, "Your amount is Transfered")

        except Exception as e:
            print(e)
            messages.success(request,"Something went Wrong")

        return redirect('/transferMoney')

        
    return render(request,'transferMoney.html')




def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')


def newCustomer(request):
    if request.method == "POST":
        Name = request.POST ["name"]
        Email = request.POST ["email"]
        AccountNum = request.POST ["account-no"]
        addMoney = request.POST ["add-money"]
        addMoney = float(addMoney)


        saveCustomerData = customers_Data(name = Name , emailId = Email , accountNumber = AccountNum, balance = addMoney)
        saveCustomerData.save()
        # print(Name,Email,AccountNum,AddMoney)
        return redirect('/customersData')
    return render(request,'newCustomer.html' )

def updatedata(request,id):
    e = customers_Data.objects.get(id=id)
    if request.method == "POST":
        Name = request.POST ["name"]
        Email = request.POST ["email"]
        AccountNum = request.POST ["account-no"]
        addMoney = request.POST ["add-money"]
        addMoney = float(addMoney)


        e = customers_Data.objects.filter(id=id).update(name = Name , emailId = Email , accountNumber = AccountNum, balance = addMoney)
        
        return redirect('/customersData')
    return render(request,'updatedata.html', {'data':e})

def deletedata(request,id):
    deleteCData = customers_Data.objects.get(id=id)
    deleteCData.delete()
    return redirect('/customersData')

