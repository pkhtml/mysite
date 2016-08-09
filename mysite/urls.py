"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mysite.view import hello
from polls.views import shoucang,urladd,urldel,weixin,updatetitle



urlpatterns = [
   # url(r'^admin/', admin.site.urls),
    url(r'^$',hello),
    url(r'^url/$',shoucang),
    url(r'^url/add/',urladd),
    url(r'^url/del/',urldel),
    url(r'^url/upt/',updatetitle),
    url(r'^weixin/',weixin),
    # url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}) 
]
