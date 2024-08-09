from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import Publications, Hashtags


class HomeView(TemplateView):
   template_name = 'index.html'

   def get_context_data(self, **kwargs):
      context = {

         'publication': Publications.objects.filter(is_active=True)

      }
      return context


class ContactView(TemplateView):
   template_name = 'contact.html'

class PublicDetailView(TemplateView):
   template_name = 'publication-detail.html'

   def get_context_data(self, **kwargs):
      publication_pk = kwargs['pk']
      context = {

         'publication': Publications.objects.get(id = publication_pk)

      }
      return context

