from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
# Create your views here.

def blog_view(request):
    now = timezone.now()
    posts = Post.objects.filter(published_date__lte=now,status=1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)
    
def blog_single(request,pid):
    now = timezone.now()
    post = get_object_or_404(Post, published_date__lte=now, pk=pid, status=1)
    post.counted_views += 1
    post.save()
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)
    

