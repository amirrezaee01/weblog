from django import template
from blog.models import Post


register = template.Library()

@register.inclusion_tag('blog/blog-recent.html')
def latestpost():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:3]
    return {'posts':posts}

