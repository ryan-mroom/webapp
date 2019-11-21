from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


def get_tags(post_tags):
    return post_tags.split(" ")


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        for post in data['object_list']:
            post.tags = get_tags(post.tags)
        return data


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['post'].tags = get_tags(data['post'].tags)
        return data


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'source', 'link_url', 'link_title', 'tags', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'source', 'link_url', 'link_title', 'tags', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = 'users-dashboard'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
