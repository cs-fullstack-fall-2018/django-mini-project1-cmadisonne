from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# from .forms import PostForm
from .models import Post

def post_list(request):
    posts = Post.objects.filter(entry_date__lte=timezone.now()).order_by('entry_date')
    return render(request, 'teach_app/teacher_list.html', {'posts': posts})
    # return HttpResponse("test")

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'teach_app/teacher_detail.html', {'post': post})