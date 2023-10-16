from django.shortcuts import render
from django.views.generic import TemplateView

from forum.models import Area, Post, Secao, SubSecao,Topico

class ForumIndexView(TemplateView):
    template_name="base.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)