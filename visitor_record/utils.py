from .models import *
from django.utils import timezone
from ipware import get_client_ip
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
    '''if 'HTTP_X_FORWARDED_FOR' in request.META:  # 获取ip
        client_ip = request.META['HTTP_X_FORWARDED_FOR']
        client_ip = client_ip.split(",")[0]  # 所以这里是真实的ip
    elif 'REMOTE_ADDR' in request.META:
        client_ip = request.META['REMOTE_ADDR']  # 这里获得代理ip
    else:
        client_ip = request.META['HTTP_CLIENT_IP']'''
    client_ip, is_routable = get_client_ip(request)
    ip_exist, created= Userip.objects.get_or_create(ip=str(client_ip))
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
    data['cookie']=key
    data['client_ip']=client_ip
    return(data)