from django.shortcuts import render
from .models import User
from .forms import UserForm
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView


def user_list(request):
    users = User.objects.filter()
    return render(request, 'home.html', {'users': users})


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user_detail.html', {'user': user})


def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'user_edit.html', {'form': form})


def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()

    return redirect('home')


class MyFormView(CreateView):
    form_class = UserForm
    success_url = "/"
    template_name = 'form.html'