from django import views
from django.shortcuts import render, redirect
from .models import WorkerUser
from .forms import WorkerUserForm, WorkerUserFormEdit

def ListUsers(request):
    supervisors = WorkerUser.objects.filter(is_staff=True, is_active=True, is_superuser=False)
    technicians = WorkerUser.objects.filter(is_staff=False, is_active=True, is_superuser=False)
    template_name = 'accounts/list.html'
    context = {
        'supervisors': supervisors,
        'technicians': technicians
    }
    return render(request, template_name, context)

def UserDetail(request, id):
    user = WorkerUser.objects.get(id=id)
    template_name = 'accounts/detail.html'
    context = {
        'user': user
    }
    return render(request, template_name, context)

class CreateUser(views.View):
    template_name = 'accounts/form.html'

    def get(self, request):
        form = WorkerUserForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = WorkerUserForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('accounts:list')
        else:
            return render(request, self.template_name, {})

class UpdateUser(views.View):
    template_name = 'accounts/form.html'

    def get(self, request, id):
        user = WorkerUser.objects.get(id=id)
        form = WorkerUserFormEdit(instance=user)
        context = {
            'is_update': True,
            'user_id': user.id,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        user = WorkerUser.objects.get(id=id)
        form = WorkerUserFormEdit(data=request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:detail', user.id)
        else:
            context = {
                'form': form
            }
            return render(request, self.template_name, context)

def DeleteUser(request):
    user = WorkerUser.objects.get(id=request.POST['id'])
    user.delete()
    return redirect('accounts:list')
    