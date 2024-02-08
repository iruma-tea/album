from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Tag, Photo

# Create your views here.


class PhotoListView(ListView):
    model = Photo
    template_name = "album/photo_list.html"
    context_object_name = "photos"


class PhotoDetailView(DetailView):
    model = Photo
    template_name = "album/photo_detail.html"
    context_object_name = "photo"


class TagPhotoListView(ListView):
    model = Photo
    template_name = "album/tag_photo.html"
    context_object_name = "photos"

    def get_queryset(self, **kwargs):
        tag_name = self.kwargs["tag"]
        tag = get_object_or_404(Tag, name=tag_name)
        return super().get_queryset().filter(tags=tag)
