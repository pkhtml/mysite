### -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Context
from polls.models import url_db,type_db
from django.template import loader,Context,RequestContext
from bs4 import BeautifulSoup,SoupStrainer
import urllib2,urllib
import time,datetime
import re
import hashlib
from django.utils.encoding import smart_str, smart_unicode
from xml.etree import ElementTree as etree


def shoucang(request):
	now =datetime.datetime.now()
	typeall=type_db.objects.all()
	urlall=url_db.objects.order_by("-add_time").exclude(urltype=99).exclude(title="")
	t = get_template('url.html')
	html=t.render(Context({'title':now,'item_list':typeall,'url_list':urlall}))
	return HttpResponse(html)

def gettitle(url):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windos NT)'
        headers = {'User-Agent': user_agent}
        req = urllib2.Request(url,headers=headers)
        resp = urllib2.urlopen(req)
        respHtml = resp.read()
        only_title = SoupStrainer("title")
        soup = BeautifulSoup(respHtml,"lxml",parse_only=only_title)
        title = soup.title.string
        if title == None:
                soup=BeautifulSoup(respHtml,"lxml",parse_only=only_title,from_encoding="gbk")
                title=soup.title.string
        strinfo = re.compile('[\r\n\t]')
        title = strinfo.sub('',title)
        return title


def urladd(request):
	url = request.POST.get('f_url')
	urltype = request.POST.get('type')
	title = gettitle(url)
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

def weixin(request):
        if request.method=='GET':
                response=HttpResponse(check(request))
                return response
        else:
                xmlstr= smart_str(request.body)
                xml = etree.fromstring(xmlstr)

                ToUserName = xml.find('ToUserName').text
                FromUserName = xml.find('FromUserName').text
                CreateTime = xml.find('CreateTime').text
                MsgType = xml.find('MsgType').text
                Content = xml.find('Content').text
                MsgId = xml.find('MsgId').text
                if Content[0:4]=='http':
                    title = gettitle(Content)
                    reply_xml = """<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                    </xml>"""%(FromUserName,ToUserName,CreateTime,title)
                    now = time.strftime("%Y%m%d %H:%M:%S",time.localtime())
                    add = url_db(url=Content,title=title,add_time=now,urltype=1,user=FromUserName,view_count=0)
                    add.save()
                else:
                    reply_xml = """<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                    </xml>"""%(FromUserName,ToUserName,CreateTime,Content)               
                return HttpResponse(reply_xml)


def check(request):
	signature = request.GET.get('signature')
	timestamp = request.GET.get('timestamp')
	nonce = request.GET.get('nonce')
	echostr = request.GET.get('echostr')
	token = 'TKm7trSVOQ9'
	
	tmpArr = [token,timestamp,nonce]
	tmpArr.sort()
	tmpArr = tmpArr[0]+tmpArr[1]+tmpArr[2]
	tmpstr = hashlib.sha1(tmpArr).hexdigest()

	if tmpstr == signature:
                return echostr
        else:
                return None
        

#微信接口地址http://pkrasp.tunnel.qydev.com/weixin/
# Token TKm7trSVOQ9
# EncodingAESKey Dr7QeserhEGC88p2xTKm7trSVOQ9eS9lhdPTEVSJFPY
# ss =type_db(type='1',type_name='证件',user='pkhtml')
# ss.save()
#  dd=type_db.objects.all()
#  print([e.user for e in all])
