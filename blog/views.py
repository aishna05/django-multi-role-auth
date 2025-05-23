from django.shortcuts import render, redirect , get_object_or_404
from .models import BlogPost , CATEGORY_CHOICES
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from authentication.models import CustomUser  # this is fine

@login_required
def create_blog_post(request):
    if request.user.user_type != 'doctor':  # Fix here
        return redirect('home')

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog:doctor_posts')
    else:
        form = BlogPostForm()
    return render(request, 'createPost.html', {'form': form})


@login_required
def doctor_posts(request):
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'doctorPost.html', {'posts': posts})


@login_required
def blog_post_list(request):
    categories = {}
    for category, _ in CATEGORY_CHOICES:
        posts = BlogPost.objects.filter(category=category, is_draft=False).order_by('-created_at')
        categories[category] = posts

    return render(request, 'postList.html', {'categories': categories})

@login_required
def edit_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, author=request.user)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:doctor_posts')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'edit_blog_post.html', {'form': form, 'post': post})

@login_required
def toggle_draft_status(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, author=request.user)
    post.is_draft = not post.is_draft
    post.save()
    return redirect('blog:doctor_posts')

@login_required
def delete_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, author=request.user)
    post.delete()
    return redirect('blog:doctor_posts')

@login_required
def blog_post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, is_draft=False)
    return render(request, 'postDetail.html', {'post': post})

