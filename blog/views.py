from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost, CATEGORIES
from .forms import BlogPostForm

from django.shortcuts import render, get_object_or_404
@login_required
def doctor_blog_create(request):
    if not hasattr(request.user, 'user_type') or request.user.user_type != 'Doctor':
        return redirect('login')
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('doctor_blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'doctor_blog_create.html', {'form': form})

@login_required
def doctor_blog_list(request):
    if not hasattr(request.user, 'user_type') or request.user.user_type != 'Doctor':
        return redirect('login')
    blogs = BlogPost.objects.filter(author=request.user)
    return render(request, 'doctor_blog_list.html', {'blogs': blogs})

@login_required
def patient_blog_list(request):
    if not hasattr(request.user, 'user_type') or request.user.user_type != 'Patient':
        return redirect('login')
    blogs_by_category = {}
    for cat, _ in CATEGORIES:
        posts = BlogPost.objects.filter(category=cat, is_draft=False)
        blogs_by_category[cat] = posts
    return render(request, 'patient_blog_list.html', {'blogs_by_category': blogs_by_category})

def blog_detail(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})
