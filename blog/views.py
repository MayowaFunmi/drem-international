from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views import generic
from . models import Post


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    login_url = 'users:login'


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    login_url = 'users:login'


class PostUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Post
    fields = ('title', 'body',)
    template_name = 'blog/post_edit.html'
    login_url = 'users:login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class PostDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog:post_list')
    login_url = 'users:login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class PostCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ['title', 'body']
    login_url = 'users:login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)