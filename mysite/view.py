### -*- coding: utf-8 -*-


from django.http import HttpResponse
import datetime
#import psutil

def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp)/1000

#获取cpu使用率
def getCPUstate(interval=1):
    return (" CPU: " + str(psutil.cpu_percent(interval)) + "%")    

#获取内存情况    
def getMemorystate(): 
        phymem = psutil.virtual_memory()
        line = "内存: %5s%% %6s/%s"%(
            phymem.percent,
            str(int(phymem.used/1024/1024))+"M",
            str(int(phymem.total/1024/1024))+"M"
            )
        return line  

def hello(request):
    hello="你好，世界"
    now=datetime.datetime.now()
    html_1="<br> %s <br><br>"% hello
    html_2="现在时间 %s <br><br>"% now
    html_3="CPU温度"+str(get_cpu_temp())
#    html_4="CPU使用率%s<br><br>%s"%(getCPUstate(),getMemorystate)
    html=html_1 + html_2 + html_3 
    return HttpResponse(html)
