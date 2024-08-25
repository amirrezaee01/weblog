from django import template
register = template.Library()
from blog.models import Post   
from django.utils import timezone


@register.inclusion_tag('website/latest_post.html')
def latestpost():
    now = timezone.now()
    posts = Post.objects.filter(published_date__lte=now,status=1).order_by('-published_date')[:3]
    return{'posts':posts}

@register.inclusion_tag('website/team.html')
def teampost():
    now = timezone.now()
    posts = Post.objects.filter(published_date__lte=now,status=1).order_by('published_date')[:4]
    return{'posts':posts}