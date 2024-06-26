"""
URL configuration for shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from app_admin import views
urlpatterns = [
    path('', views.index,name='index'),
    path('addAdmin/', views.addAdmin,name='addAdmin'),
    path('viewData/', views.viewData,name='viewData'),
    path('updateData/<int:admin_id>/', views.updateData,name='updateData'),
    path('deleteData/<int:admin_id>', views.deleteData,name='deleteData'),
    path('viewdataall',views.viewdataall),
    path('insertdata',views.insertdata),
     path('updatedata/<id>',views.updatedata),
     path('deletedata/<id>',views.deletedata),
     path('insertCategory',views.insertCategory),
     path('insertbook',views.insertbook),
     path('viewdatabook',views.viewdatabook),
     path('send_otp',views.send_otp)
     

]
