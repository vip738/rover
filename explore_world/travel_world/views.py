from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
class Authentication(View):
    template_name = 'travel_world/login.html'
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        pass
