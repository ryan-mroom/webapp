from django.shortcuts import Http404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


def get_tags(post_tags):
    return post_tags.split(" ")


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(approved=True).order_by('-date_posted')

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        for post in data['object_list']:
            post.tags = get_tags(post.tags)

            word_list = post.content.split()
            if len(word_list) > 100:
                post.content = ' '.join(word_list[:80]) + '...read more'

        return data


class PostPendingListView(ListView):
    model = Post
    template_name = 'newsfeed/post_pending_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        if self.request.user.username != 'MushroomOfficial':
            raise Http404()
        return Post.objects.filter(approved=False).order_by('date_posted')

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        for post in data['object_list']:
            post.tags = get_tags(post.tags)

            word_list = post.content.split()
            if len(word_list) > 100:
                post.content = ' '.join(word_list[:80]) + '...read more'

        return data

    def test_func(self):
        return self.request.user.username == 'MushroomOfficial'


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
        form.instance.approved = False

        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostApprovalView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'source', 'link_url', 'link_title', 'tags', 'image', 'approved']
    success_url = '/pending'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.username == 'MushroomOfficial'


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = 'users-dashboard'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
