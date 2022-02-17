from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import NewComment
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
def home(request):

    posts =Post.objects.all()
    paginator =Paginator(posts,2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context ={
        'title' : 'الصفحة الرئيسية',
        'posts' : posts,
        'page' : page,
    }
    return render(request, 'blog/index.html', context)

def about(request):
        context ={
        'title' : 'من انا',
    }
        return render(request, 'blog/about.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)


    #comments is rekated name of model class Comment
    comments = post.comments.filter(active=True)

    
    #check before save data from comment form
    if request.method == 'POST':
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            new_comment = NewComment()
    else:
        comment_form = NewComment()
        
    context = { 
        'title': post,
        'post' : post,
        'comments' :comments,
        'comment_form' :comment_form,
    }
    return render(request, 'blog/detail.html', context)
