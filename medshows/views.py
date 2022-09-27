from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms

def show_all_med(request):
    med_img_post = models.MedicalShows.objects.all()
    return render(request, "medpost.html", {'post':med_img_post})

#Получение
def show_all_med_detail(request, id):
    shows = get_object_or_404(models.MedicalShows, id=id)
    return render(request, "medical_post_list_detail.html", {'shows': shows})

#Добавление
def add_med_shows(request):
    method = request.method
    if method == "POST":
        form = forms.MedShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('med show created')
    else:
        form = forms.MedShowForm()
    return render(request, "add_med_show_form.html", {'med_form': form})

#Обновление
def show_update(request, id):
    show_object = get_object_or_404(models.MedicalShows, id=id)
    if request.method == 'POST':
        form = forms.MedShowForm(instance=show_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Show good update')
    else:
        form = forms.MedShowForm(instance=show_object)
    return render(request, 'show_update.html', {'form': form, 'object': show_object})

#Удаление
def show_delete(request, id):
    show_object = get_object_or_404(models.MedicalShows, id=id)
    show_object.delete()
    return HttpResponse('Med Show deleted')