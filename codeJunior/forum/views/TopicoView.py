from django.views.generic import DetailView

from forum.models import Topico, Post

class TopicoView(DetailView):
    model = Topico
    template_name = "Topico.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        self.object = self.get_object()

        posts = Post.objects.filter(topico=self.object)

        context['posts'] = posts

        # print(f'Context: {context}')

        return context
    
