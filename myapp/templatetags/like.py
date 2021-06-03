from django import template
from myapp.models import *

register=template.Library()

@register.filter(name='likeCounter')
def likeCounter(post,ipost):
    like=Like.objects.all()
    for i in like:
        post=Post.objects.get(pid=i.post.pid)
        if(ipost==post):
            return i.counter
    return 0

@register.filter(name='likedone')
def likedone(ipost,iuser):
    like=Like.objects.all()
    user=AccountUser.objects.get(username=iuser)
    for i in like:
        post=Post.objects.get(pid=i.post.pid)
        if(ipost==post):
            lusers=i.user.all()
            if(user in lusers):
                return True
    return False


