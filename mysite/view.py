### -*- coding: utf-8 -*-


from django.http import HttpResponse
import datetime

def hello(request):
    hello="你好，世界"
    now=datetime.datetime.now()
    html_1="<br> %s <br><br>"% hello
    html_2="现在时间 %s"% now
    html=html_1 + html_2
    return HttpResponse(html)
