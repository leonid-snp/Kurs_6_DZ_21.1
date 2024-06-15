from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.form import BlogForm, BlogContentManagerForm
from blog.models import Blog
from config.settings import EMAIL_HOST_USER, EMAIL_TO


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    class_form = BlogForm
    fields = ('title', 'content', 'photo')
    success_url = reverse_lazy("blog:blog_list")

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    class_form = BlogForm

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser:
            return BlogForm
        elif user.has_perm('blog.change_content_blog') and user.has_perm('blog.change_title_blog') and user.has_perm('blog.unpublish_a_blog'):
            return BlogContentManagerForm
        else:
            raise PermissionDenied


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog

    def get_object(self, queryset=None):
        user = self.request.user
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        if self.object.views_count == 100:
            send_mail(
                subject='Поздравляю!',
                message=f'Поздравляю ваша статья '
                        f'{self.object.title} набрала '
                        f'{self.object.views_count} просмотров!!!',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email, EMAIL_TO]
            )
        return self.object


class BlogDeletelView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")
