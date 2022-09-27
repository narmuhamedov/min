from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django . views import generic

class MedShowListView(generic.ListView):
    template_name = 'medpost.html'
    queryset = models.MedicalShows.objects.all()
    def get_queryset(self):
        return models.MedicalShows.objects.all()


# def show_all_med(request):
#     med_img_post = models.MedicalShows.objects.all()
#     return render(request, "medpost.html", {'post':med_img_post})

#Получение
class MedShowsDetailView(generic.DetailView):
    template_name = 'medical_post_list_detail.html'

    def get_object(self, **kwargs):
        medshows_id = self.kwargs.get('id')
        return get_object_or_404(models.MedicalShows, id=medshows_id)


# def show_all_med_detail(request, id):
#     shows = get_object_or_404(models.MedicalShows, id=id)
#     return render(request, "medical_post_list_detail.html", {'shows': shows})

#Добавление
class MedShowsCreateView(generic.CreateView):
    template_name = 'add_med_show_form.html'
    form_class = forms.MedShowForm
    queryset = models.MedicalShows.objects.all()
    success_url = '/medshows/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(MedShowsCreateView, self).form_valid(form=form)



# def add_med_shows(request):
#     method = request.method
#     if method == "POST":
#         form = forms.MedShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('med show created')
#     else:
#         form = forms.MedShowForm()
#     return render(request, "add_med_show_form.html", {'med_form': form})

#Обновление
class MedShowUpdateView(generic.UpdateView):
    template_name = 'show_update.html'
    form_class = forms.MedShowForm
    success_url = '/medshows/'

    def get_object(self, **kwargs):
        medshows_id = self.kwargs.get('id')
        return get_object_or_404(models.MedicalShows, id=medshows_id)
    def form_valid(self, form):
        return super(MedShowUpdateView,self).form_valid(form=form)






# def show_update(request, id):
#     show_object = get_object_or_404(models.MedicalShows, id=id)
#     if request.method == 'POST':
#         form = forms.MedShowForm(instance=show_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Show good update')
#     else:
#         form = forms.MedShowForm(instance=show_object)
#     return render(request, 'show_update.html', {'form': form, 'object': show_object})

#Удаление
class MedShowsDeleteView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/medshows/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.MedicalShows,id=show_id)

# def show_delete(request, id):
#     show_object = get_object_or_404(models.MedicalShows, id=id)
#     show_object.delete()
#     return HttpResponse('Med Show deleted')