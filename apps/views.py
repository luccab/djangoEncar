from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpResponse

#class FormView(generic.DetailView):
#    template_name = 'app/form.html'

def index(request):
    return HttpResponse("Hello, world.")

def form(request):
    return render_to_response('apps/form.html')
