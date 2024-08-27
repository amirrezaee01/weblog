from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404

def blog_view(request, **kwargs):
    now = timezone.now()
    posts = Post.objects.filter(published_date__lte=now, status=1)
    
    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])
        
    if kwargs.get('author_username') is not None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') is not None:
        posts = posts.filter(tag__name__in=[kwargs['tag_name']])
    
        
    paginator = Paginator(posts, 6)
    
    try:
        page_number = request.GET.get('page')
        posts = paginator.page(page_number)  
    except PageNotAnInteger:
        posts = paginator.page(1)  
    except EmptyPage:
        posts = paginator.page(1)  
        
    
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request,pid):
    now = timezone.now()

    post = get_object_or_404(Post, published_date__lte=now, pk=pid, status=1)
    post.counted_views += 1
    post.save()

    posts = Post.objects.filter(status=1, published_date__lte=now).order_by('published_date')
    
    post_ids = list(posts.values_list('id', flat=True))
    current_index = post_ids.index(post.id)

    prev_post = posts[current_index - 1] if current_index > 0 else None
    next_post = posts[current_index + 1] if current_index < len(post_ids) - 1 else None
    
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
    }
    return render(request,'blog/blog-single.html',context)
    

