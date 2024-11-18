from django.shortcuts import render  # type: ignore
from .models import Post
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

def filter_post(post):
    if post.is_published:
        return True
    return False

def post_detail(request, pk):
    # Найдите пост по id
    post = next((post for post in posts if post['id'] == pk), None)
    if post is None:
        return render(request, '404.html', status=404)
    return render(request, 'blog/detail.html', {'post': post})


class PostListView(ListView):
    model = Post
    ordering = 'id'
    paginate_by = 10
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        # Возвращаем только те посты, где is_pub=True
        return Post.objects.filter(is_published=True).order_by(self.ordering)


def category_posts(request, category_slug):
    context = {'category_slug': category_slug}
    return render(request, 'blog/category.html', context)
