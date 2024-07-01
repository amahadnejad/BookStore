from django.shortcuts import render
from django.views.generic.base import TemplateView


class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'
