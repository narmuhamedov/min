from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, FormView
from . import parser, models, forms

class ParserView(ListView):
    model = models.AllMedApartment
    template_name = 'med_list.html'
    def get_queryset(self):
        return models.AllMedApartment.objects.all()



class ParserFormView(FormView):
    template_name = 'parser.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('parser good')
            # return redirect(reversed("parse:list_objects"))
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)