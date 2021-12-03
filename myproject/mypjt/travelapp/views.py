from django.shortcuts import render
from .models import Place
from .models import People


# Create your views here.
def ind(request):
    obj=Place.objects.all()


    return render(request, "index.html",{'result':obj})
def ind(request):
    obj1=People.objects.all()
    return render(request, "index.html", {'result1': obj1})



