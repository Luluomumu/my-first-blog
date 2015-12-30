from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
import datetime

# Create your views here.
def homeview(request):
    now = datetime.datetime.now()
    string = "<h1>Hello World it is now %s</h1><hr>" %now
    posts = Post.objects.all()
    
    for post in posts:
        title = post.title
        date = post.created_date
        content = "<h5>%s - %s</h5>" % (title, date)
        string += content
        
    
    return HttpResponse(string)
