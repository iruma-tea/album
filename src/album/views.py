from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Tag, Photo
from django.urls import reverse_lazy

# Create your views here.


class PhotoListView(ListView):
    model = Photo
    template_name = "album/photo_list.html"
    context_object_name = "photos"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["tags"] = Tag.objects.all()
        return context


class PhotoDetailView(DetailView):
    model = Photo
    template_name = "album/photo_detail.html"
    context_object_name = "photo"


# class TagPhotoListView(ListView):
#     model = Photo
#     template_name = "album/tag_photo.html"
#     context_object_name = "photos"

#     def get_queryset(self, **kwargs):
#         tag_name = self.kwargs["tag"]
#         tag = get_object_or_404(Tag, name=tag_name)
#         return super().get_queryset().filter(tags=tag)

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)

#         context["tag"] = self.kwargs["tag"]
#         return context

class TagPhotoListView(ListView):
    model = Photo
    template_name = "album/tag_photo.html"
    context_object_name = 'photos'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        tag_name = self.kwargs["tag"]
        tag_name = get_object_or_404(Tag, name=tag_name)
        photos = Photo.objects.filter(tags=tag_name)

        context["tag"] = tag_name
        context["photos"] = photos

        return context


class PhotoCreateView(CreateView):
    model = Photo
    template_name = "album/photo_create.html"
    fields = "__all__"
    success_url = reverse_lazy("photo-list")
