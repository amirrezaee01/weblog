from django import template
from blog.models import Post,Category,Comment


register = template.Library()

    
@register.inclusion_tag('blog/blog-recent.html')
def latestpost():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:3]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-category.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        post_count = posts.filter(category=name).count()
        
        cat_dict[name] = post_count
    
    return {'categories': cat_dict}