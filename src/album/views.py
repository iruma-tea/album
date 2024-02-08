from django.views.generic import ListView
from .models import Photo

# Create your views here.


class PhotoListView(ListView):
    model = Photo
    template_name = "album/photo_list.html"
    context_object_name = "photos"
