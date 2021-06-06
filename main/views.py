from django.shortcuts import render, redirect
from django import views

class main(views.View):

    def get(self, request):

        template_name = 'main/main.html'
        return render(request, template_name)