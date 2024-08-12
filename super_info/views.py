from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .models import Publications, Hashtags, Contacts


class HomeView(TemplateView):
   template_name = 'index.html'

   def get_context_data(self, **kwargs):
      context = {

         'publication': Publications.objects.all(),
         'publications': Publications.objects.filter(is_active=True)


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

def client_contact(request):
   print(request.POST)

   name = request.POST['name']
   email = request.POST['email']
   subject = request.POST['subject']
   message = request.POST['message']

   Contacts.objects.create(name=name, email=email, subject=subject, message=message)

   return redirect('contact-list')
