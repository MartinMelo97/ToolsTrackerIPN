from django import forms, views
from django.shortcuts import render, redirect
from .models import WorkTool
from .forms import ToolForm
from .utils import tools_form_validations

def ListTool(request):
    tools = WorkTool.objects.all()
    tamplate_name = 'worktools/list.html'
    context = {
        'tools' : tools
    }
    return render(request, tamplate_name, context)

def DetailTool(request, id):
    tool = WorkTool.objects.get(id=id)
    tamplate_name = 'worktools/detail.html'
    context = {
        'tool' : tool
    }
    return render(request, tamplate_name, context)

class CreateTool(views.View):
    template_name = 'worktools/form.html'

    def get(self, request):
        form =  ToolForm()
        context = {
            'form' : form
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = ToolForm(data=request.POST)
        if form.is_valid():
            new_tool = form.save(commit=False)
            new_tool = tools_form_validations(form, new_tool)
            new_tool.save()
            return redirect ('worktools:list')
        else:
            context = {
            'form' : form
        }
        return render(request, self.template_name, context)
        
class UpdateTool(views.View):
    template_name = "worktools/form.html"

    def get (self, request, id):
        worktool = WorkTool.objects.get(id=id)
        form = ToolForm(instance=worktool)
        context = {
            'form' : form,
            'worktool' : worktool,
            'is_update' : True
        }

        return render(request, self.template_name, context)

    def post(self, request, id):
        worktool = WorkTool.objects.get(id=id)
        worktool_actual_is_in_maintain_value = worktool.is_in_maintain
        form = ToolForm(instance=worktool, data=request.POST)
        if form.is_valid():
            worktool_updated = form.save(commit= False)
            worktool_updated = tools_form_validations(form, worktool_updated, worktool_actual_is_in_maintain_value)
            worktool_updated.save()
            return redirect('worktools:detail', worktool_updated.id)
        else:
            context={
                'form' :  form
            }
            return render(request, self.template_name,context)
            
def DeleteTool(request):
    worktool = WorkTool.objects.get(id=request.POST['id'])
    worktool.delete()
    return redirect('worktools:list')
