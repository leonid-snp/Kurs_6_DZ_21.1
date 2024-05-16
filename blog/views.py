from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = (
        "title", "slug", "content", "photo",
        "created_at", "is_published", "views_count"
    )
    success_url = reverse_lazy("blog:blog_list")

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = (
        "title", "slug", "content", "photo",
        "created_at", "is_published", "views_count"
    )
    success_url = reverse_lazy("blog:blog_list")


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogDeletelView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")
