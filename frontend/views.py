from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import Question
from .forms import CreateQuestionForm
# Create your views here.


class IndexView(ListView):
	template_name = 'frontend/index.html'
	model = Question
	def get_queryset(self):
		return Question.objects.all()


class CreateQuestionView(CreateView):
	template_name = 'frontend/createq.html'
	model = Question
	form_class = CreateQuestionForm



