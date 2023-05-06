from django.db import models
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Question, Comment 
from .forms import Answer_Form
from django.urls import reverse, reverse_lazy
from taggit.models import Tag
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.utils.decorators import method_decorator

class Tag_List_View(ListView):
    template_name = 'smb_base/tag_list.html'
    context_object_name = 'tag_list'
    model = Tag
    def tag_list(request):
        tag_list = Tag.objects.all()
        return render(request, 'smb_base:tag-list', {'tag_list': tag_list})
    
class Question_List_By_Tag_View(ListView):
    template_name = 'questions_by_tag.html'
    context_object_name = 'questions'

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        queryset = Question.objects.filter(tag__name__in=[tag_name])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.kwargs['tag_name']
        return context
    
class Question_Detail_View(DetailView):

    model = Question


      
@method_decorator(login_required, name='dispatch')
class Question_Comment_View(CreateView):
    """
    View for adding a new comment to a question.
    """
    template_name = 'smb_base/question-answer.html'
    model = Comment
    form_class = Answer_Form

    def form_valid(self, form):
        """
        If the form is valid, set the question ID for the new comment and save it.
        """
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        """
        Returns the URL to redirect to after a successful form submission.
        """
        return reverse_lazy('smb_base:question-lists')
