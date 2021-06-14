from django import forms, views
from django.shortcuts import render, redirect
from .models import WorkTool
from .forms import ToolForm
from .utils import tools_form_validations, remove_tools_by_id_list

from accounts.models import WorkerUser

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


# -------------------- Assign tools to user views -----------------------------

class AssignTool(views.View):

    template_name = 'assign/assign_to_user.html'
    users = WorkerUser.objects.filter(is_staff=False, is_active=True, is_superuser=False)
    available_tools = WorkTool.objects.filter(is_in_maintain=False)
    context = {
        'users': users,
        'available_tools': available_tools
    }

    def get (self, request):
        return render(request, self.template_name, self.context)

    def post (self, request):
        user_id = request.POST.get('user_id')
        tools_id = request.POST.get('tools_id')

        if user_id == None or tools_id == None:
            return render(request, self.template_name, self.context)

        user = WorkerUser.objects.get(id=user_id)

        tools_id_list = tools_id.split(',')
        tools = WorkTool.objects.filter(id__in=tools_id_list)

        for tool in tools:
            tool.user_id = user
            tool.save()

        return redirect('accounts:detail', user.id)

class UnassignTools(views.View):
    template_name = 'assign/unassign_to_user.html'

    def get(self, request, id):
        user = WorkerUser.objects.get(id=id)
        context = {
            'user': user
        }
        return render(request, self.template_name, context)

    def post (self, request, id):
        user = WorkerUser.objects.get(id=id)
        new_tools_id = request.POST.get('tools_id')

        actual_tools_id = []

        for actual_tool in user.tools.all():
            actual_tools_id.append(actual_tool.id)

        new_tools = list(map(int, new_tools_id))

        removed_tools_id = remove_tools_by_id_list(actual_tools_id, new_tools)

        removed_tools = WorkTool.objects.filter(id__in=removed_tools_id)

        for tool in removed_tools:
            tool.user_id = None
            tool.save()

        return redirect('accounts:detail', user.id)
