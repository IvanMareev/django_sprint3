from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils.timezone import now
from .models import Post, Category


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 10
    ordering = 'id'

    def get_queryset(self):
        return Post.objects.filter(
            category__is_published=True,
            is_published=True,
            pub_date__lte=now()
        ).order_by(self.ordering)[:5]


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True)
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        created_at__lte=now(),
        pub_date__lte=now())
    context = {'category': category, 'post_list': posts}
    return render(request, 'blog/category.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_object(self):
        return get_object_or_404(Post.objects.filter(
            category__is_published=True,
            is_published=True,
            pub_date__lte=now()
        ), pk=self.kwargs['pk'])
