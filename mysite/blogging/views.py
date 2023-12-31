from blogging.models import Post 
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView 


class list_view(ListView):
    queryset = Post.objects.order_by('-published_date')
    template_name = 'blogging/list.html'


class detail_view(DetailView):
    model = Post
    template_name = 'blogging/detail.html'
