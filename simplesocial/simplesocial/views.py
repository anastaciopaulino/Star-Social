from django.views.generic import TemplateView
from django.urls import reverse_lazy


class TestePage(TemplateView):
    template_name = 'teste.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'