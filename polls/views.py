### -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Context
from polls.models import url_db,type_db
from django.template import loader,Context,RequestContext
from bs4 import BeautifulSoup
import urllib2,urllib
import time,datetime
import re


def shoucang(request):
	now =datetime.datetime.now()
	typeall=type_db.objects.all()
	urlall=url_db.objects.order_by("-add_time").exclude(urltype=99).exclude(title="")
	t = get_template('url.html')
	html=t.render(Context({'title':now,'item_list':typeall,'url_list':urlall}))
	return HttpResponse(html)

def urladd(request):
	url = request.POST.get('f_url')
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windos NT)'
	#urllib.request.urlencode(user_agent)
	headers = {'User-Agent': user_agent}    
	#req = urllib.request.Request(url, headers=headers)
	#response = urllib.request.urlopen(req)
	#print(response)
	#data = response.read()
	#
    #url=request.POST[f_url]
 	#url = request.POST.get('f_url')
	urltype = request.POST.get('type')
	req = urllib2.Request(url,headers=headers)
 	resp = urllib2.urlopen(req)
 	respHtml = resp.read()
 	#body = data.decode('utf-8')
	#foundLabel = respHtml.findAll("label")
	soup = BeautifulSoup(respHtml)
	title = soup.title.string 
	
	

	strinfo = re.compile('\r\n')
	title = strinfo.sub(' ',title)

	now = time.strftime("%Y%m%d %H:%M:%S",time.localtime())
	add = url_db(url=url,title=title,add_time=now,urltype=urltype,user="pkhtml",view_count=0)
	add.save()
	t = get_template('show.html')
	html=t.render(Context({'title':title,'url':'../../url/'}))
	return HttpResponse(html)


def urldel(request):
	url_id = request.GET.get('id')
	urldel = url_db.objects.get(id = url_id)
	urldel.urltype=99
	urldel.save()
	t = get_template('show.html')
	html=t.render(Context({'title':'删除成功','url':'../../url/'}))
	return HttpResponse(html)



# ss =type_db(type='1',type_name='证件',user='pkhtml')
# ss.save()
#  dd=type_db.objects.all()
#  print([e.user for e in all])
