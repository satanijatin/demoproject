from django.shortcuts import render,redirect
from rest_framework.response import Response
from .models import *
from django.http import JsonResponse
from .serializer import *
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.conf import settings

import http.client

# Create your views here.

def send_otp(request):
    print("FUNCTION CALLED")
    conn = http.client.HTTPSConnection("api.msg91.com")
    authkey = settings.AUTH_KEY 
    headers = { 'content-type': "application/json" }
    url = "http://control.msg91.com/api/sendotp.php?otp=1258"+"&message="+"Your otp is 1258" +"&mobile=8866502411"+"&authkey="+authkey+"&country=91"
    url = url.replace(" ", "%20")

    conn.request("GET", url , headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data)
    return JsonResponse({"data":"success"})





@api_view(['GET'])
def viewdatabook(request):
    datas=Book.objects.all()
    serializers=BookSerializer(datas,many=True)
    return Response({"Status":202,"data":serializers.data})

@api_view(['POST'])
def insertCategory(request):
     data = request.data
     serializer = CategorySerializer(data=request.data)
     if not serializer.is_valid():
          return Response({"status": "403","message":"Something Went Wrong","error":serializer.errors})
     
     serializer.save()
     return Response({"status": "200","message":"Save Successfully"})

@api_view(['POST'])
def insertbook(request):
     data = request.data
     serializer = BookSerializer1(data=request.data)
     if not serializer.is_valid():
          return Response({"status": "403","message":"Something Went Wrong","error":serializer.errors})
     
     serializer.save()
     return Response({"status": "200","message":"Save Successfully"})

@api_view(['GET'])
def viewdataall(request):
    datas=Admin.objects.all()
    serializers=AdminSerializer(datas,many=True)
    return Response({"Status":202,"data":serializers.data})


@api_view(['POST'])
def insertdata(request):
     data = request.data
     serializer = AdminSerializer(data=request.data)
     if not serializer.is_valid():
          return Response({"status": "403","message":"Something Went Wrong","error":serializer.errors})
     
     serializer.save()
     return Response({"status": "200","message":"Save Successfully"})

@api_view(['POST'])
def updatedata(request,id):
     
    try:
            admin_id=Admin.objects.get(id=id)

            serializer = AdminSerializer(admin_id,data=request.data,partial=True)
            if not serializer.is_valid():
                return Response({"status": "403","message":"Something Went Wrong","error":serializer.errors})
     
            serializer.save()
            return Response({"status": "200","message":"Update Successfully"})
    except :
            return Response({"status": "403","message":"Invalid id"})
    
@api_view(['DELETE'])
def deletedata(request,id):
     
    try:
            admin_id=Admin.objects.get(id=id)
              
            admin_id.delete()
            return Response({"status": "200","message":"Delete Successfully"})
    except :
            return Response({"status": "403","message":"Invalid id"})


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



