from django.views.generic import ListView, DetailView
from .models import Photo

# Create your views here.


class PhotoListView(ListView):
    model = Photo
    template_name = "album/photo_list.html"
    context_object_name = "photos"


class PhotoDetailView(DetailView):
    model = Photo
    template_name = "album/photo_detail.html"
    context_object_name = "photo"
