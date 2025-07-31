from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import LibraryUser
from django import forms

# --------- FORM ---------
class LibraryUserForm(forms.ModelForm):
    class Meta:
        model = LibraryUser
        fields = ['name', 'email', 'age']

# --------- CREATE & LIST ---------
def user_list_create(request):
    users = LibraryUser.objects.all()
    form = LibraryUserForm()

    if request.method == 'POST':
        form = LibraryUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')

    return render(request, 'user_list.html', {'form': form, 'users': users})

# --------- UPDATE ---------
def user_update(request, pk):
    user = get_object_or_404(LibraryUser, pk=pk)
    form = LibraryUserForm(instance=user)

    if request.method == 'POST':
        form = LibraryUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')

    return render(request, 'user_edit.html', {'form': form})

# --------- DELETE ---------
def user_delete(request, pk):
    user = get_object_or_404(LibraryUser, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_delete.html', {'user': user})
