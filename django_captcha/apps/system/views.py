from django.shortcuts import render,get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, DetailView,FormView , ListView

from .models import Pregunta
from .forms import Add_Question_Form

class Home(ListView):
	template_name = 'home.html'
	context_object_name = 'questions'

	def get_queryset(self):
		return Pregunta.objects.all()

class Pregunta_Detalle(DetailView):
	model = Pregunta
	template_name = 'question.html'
	context_object_name = 'question'
	slug_url = 'pk'

	def get_object(self):
		return get_object_or_404(Pregunta, id=self.kwargs['pk'])

class Pregunta_Nueva(FormView):
	template_name = 'new_question.html'
	form_class = Add_Question_Form
	success_url = '/'

	def dispatch(self, *args, **kwargs):
		return super(Pregunta_Nueva, self).dispatch(*args, **kwargs)

	def form_valid(self, form):
		form.save()
		return super(Pregunta_Nueva, self).form_valid(form)
