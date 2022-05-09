import struct, sys, os, time
from xml.etree.ElementInclude import include

from .ip2Region import Ip2Region
from .models import *
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
 
#自定义的函数，不是视图
def count_visits(request, obj):       #修改网站访问量和访问ip等信息
    # 每一次访问，网站总访问次数加一
    data={}
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" % (ct.model, obj.pk)
    count_nums, created = VisitNumber.objects.get_or_create(id=1)
    if not request.COOKIES.get(key):      
        count_nums.count += 1
        count_nums.save()
    
    # 记录访问ip和每个ip的次数
    if 'X-Real-IP' in request.META:
        client_ip = request.META['X-Real-IP']
    elif 'HTTP_X_FORWARDED_FOR' in request.META:  # 获取ip
        client_ip = request.META['HTTP_X_FORWARDED_FOR']
        client_ip = client_ip.split(",")[0]  # 所以这里是真实的ip
    elif 'REMOTE_ADDR' in request.META:
        client_ip = request.META['REMOTE_ADDR']  # 这里获得代理ip
    else:
        client_ip = request.META['HTTP_CLIENT_IP']
  
    ip_exist, created= Userip.objects.get_or_create(ip=str(client_ip))
    if created:
        dbfile = './visitor_record/data/ip2region.db'
        algorithm = 'b-tree'
        searcher = Ip2Region(dbfile)
        if searcher.isip(client_ip):
            if algorithm == "binary":
                data = searcher.binarySearch(client_ip)
            elif algorithm == "memory":
                data = searcher.memorySearch(client_ip)
            else:
                data = searcher.btreeSearch(client_ip)
            location = f"{data['city_id']}|{ data['region'].decode('utf-8')}"
            searcher.close()
            if location == '':
                ip_exist.location =  'Unknown location'
            else:
                ip_exist.location = location
    if not request.COOKIES.get(key):
        ip_exist.count += 1
    ip_exist.save()


    # 增加今日访问次数
    date = timezone.now().date()
    today, created = DayNumber.objects.get_or_create(day=date)
    today.count += 1
    today.save()
    data['requestMETA']=request.META
    data['total_hits'] = count_nums.count
    data['total_vistors'] = Userip.objects.all().count()
    data['location'] = ip_exist.location
    data['cookie']=key
    data['client_ip']=client_ip
    return(data)