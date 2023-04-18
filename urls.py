"""resturant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp import views
from resturant import settings

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testingPage/',views.test),
    path('homePage/',views.home,name='index'),
    path('blogsPage/',views.blogs,name='blogs'),
    path('contactusPage/',views.contactus,name='contactus'),
    path('galleryPage/',views.gallery,name='gallery'),
    path('loginPage/',views.login,name='login'),
    path('registerPage/',views.register,name='register'),
    path('aboutusPage/',views.home,name='aboutus'),
    path('inqueryPage/',views.inquery,name='inquery'),
    path('fullblogsPage/<int:blogid>',views.fullblogs,name='fullblogs'),
    path('getdirectionsPage/',views.getdirections,name='getdirections'),
    path('changepasswordPage/',views.changepassword,name='changepassword'),
    path('myprofilePage/',views.myprofile,name='myprofile'),
    path('forgetpasswordPage/',views.forgetpasssword,name='forgetpassword'),
    path('logoutPage/',views.logout,name='logout'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)