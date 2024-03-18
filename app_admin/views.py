from django.shortcuts import render,redirect
from .models import *


# Create your views here.

def index(request):
    return render(request,"index.html")


def addAdmin(request):
    if request.method=="POST":
        if request.POST['id']!="":
            admin_id = request.POST['id']
            select_row = Admin.objects.get(id=admin_id)
            str_lan = ",".join(str(element) for element in request.POST.getlist("language[]"))
            select_row.name = request.POST['name']
            select_row.email = request.POST['email']
            select_row.password = request.POST['password']
            select_row.language = str_lan
            select_row.gender = request.POST['gender']
            select_row.save()
            return redirect('viewData')
        else:
            str_lan = ",".join(str(element) for element in request.POST.getlist("language[]"))
            Admin.objects.create(
                name = request.POST['name'],
                email = request.POST['email'],
                password = request.POST['password'],
                language = str_lan,
                gender = request.POST['gender'],
            )
            return render(request,"index.html",{"success_msg":"Insert Successfully"})
    else:
        return render(request,"index.html",{"fail_msg":"invalid root"})
    
def viewData(request):
    all_admin = Admin.objects.all()
   
    return render(request,"view_admin.html",{"all_admin":all_admin})

def updateData(request,admin_id):
    select_row = Admin.objects.get(id=admin_id)
    return render(request,"index.html",{"select_row":select_row})
        

def deleteData(request,admin_id):
   select_row = Admin.objects.get(id=admin_id)
   select_row.delete()
   return redirect('viewData')



