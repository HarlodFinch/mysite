import datetime
from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache
from django.urls import reverse
from read_statistics.utils import get_seven_days_read_data,get_today_hot_data,get_yesterday_hot_data
from blog.models import Blog

def get_7_days_hot_blogs():
    today=timezone.now().date()
    date=today-datetime.timedelta(days=7)
    blogs=Blog.objects \
              .filter(read_details__date__lt=today,read_details__date__gte=date) \
              .values('id','title') \
              .annotate(read_time_sum=Sum('read_details__read_time')) \
              .order_by('-read_time_sum')
    return blogs[:7]

def home(request):
    blog_content_type=ContentType.objects.get_for_model(Blog)
    dates,read_times=get_seven_days_read_data(blog_content_type)

    hot_blogs_7_days=cache.get('hot_blogs_7_days')
    if hot_blogs_7_days is None:
        hot_blogs_7_days=get_7_days_hot_blogs()
        hot_blogs_7_days=cache.set('hot_blogs_7_days',hot_blogs_7_days,3600)


    context={}
    context['dates']=dates
    context['read_times']=read_times
    context['today_hot_data']=get_today_hot_data(blog_content_type)
    context['yesterday_hot_data']=get_yesterday_hot_data(blog_content_type)
    context['hot_blogs_7_days']=hot_blogs_7_days
    return render(request,'home.html',context)

