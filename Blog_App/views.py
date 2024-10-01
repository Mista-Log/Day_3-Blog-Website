from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.



def index(request):
    posts = Post.objects.all()
    post = get_object_or_404(Post, pk=1)
    post1 = get_object_or_404(Post, pk=2)
    post2 = get_object_or_404(Post, pk=3)
    post3 = get_object_or_404(Post, pk=4)

    post4 = get_object_or_404(Post, pk=6)
    post5 = get_object_or_404(Post, pk=7)
    post6 = get_object_or_404(Post, pk=8)
    post7 = get_object_or_404(Post, pk=9)

    post8 = get_object_or_404(Post, pk=11)
    post9 = get_object_or_404(Post, pk=12)
    post10 = get_object_or_404(Post, pk=13)


    tri_business = Post.objects.all()[6:9]
    tri_lifestyle = Post.objects.all()[10:13]
    tri_lifestyle2 = Post.objects.all()[11:15]

    trending = Post.objects.all()[4:8]
    culture = Post.objects.all()[0:5]
    business = Post.objects.all()[6:11]
    lifestyle = Post.objects.all()[11:16]
    context = {'posts': posts, 'lifestyle': lifestyle, 'post1': post1, 'tri_lifestyle2': tri_lifestyle2, 'culture': culture, 'post5': post5, 'post6': post6, 'post7': post7,  'post4': post4, 'post2': post2, 'post3': post3, 'post': post, 'post8': post8, 'post9': post9, 'post10': post10, 'tri_lifestyle': tri_lifestyle, 'tri_business': tri_business, 'business': business, 'trending': trending}
    return render(request, 'index.html', context)

def single_post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'single-post.html', {'posts': posts})