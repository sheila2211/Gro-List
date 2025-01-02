from django.views.generic import TemplateView, FormView

from .models import Post
from .forms import PostForm

class HomePageView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.all().order_by('post_type')
        return context
    

class AddPostView(FormView):
    template_name = "new_post.html"
    form_class = PostForm 
    success_url = "post/"
    