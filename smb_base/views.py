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

def home(request):
    return render(request, 'home.html')

class Tag_List_View(ListView):
    template_name = 'smb_base/tag_list.html'
    context_object_name = 'tag_list'
    model = Tag
    def tag_list(request):
        tag_list = Tag.objects.all()
        return render(request, 'smb_base:tag-list', {'tag_list': tag_list})
    
class Question_Create_View(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['title', 'content' , 'tag']
    context_object_name =  'question'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
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
    
class Question_List_View(ListView):
    model = Question
    context_object_name = 'questions'
    ordering = ['-date_created']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        inPut = self.request.GET.get('search-area') or ''
        if inPut:
            data['questions'] = data['questions'].filter(Q(title__icontains = inPut) | Q(tag__name__icontains= inPut)).distinct()
            data['inPut'] = inPut
        return data

      
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
    
class Question_Delete_View(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Question
    context_object_name =  'question'
    success_url = "/"

    def test_func(self):
        questions = self.get_object()
        if self.request.user != questions.user:
            return False
        return True
    
    @login_required
    def delete_question(request, pk):
        question = get_object_or_404(Question, pk=pk)
        if request.method == 'POST' and request.user == question.user:
            question.delete()
            return redirect('smb_base:index')
        return render(request, 'smb_base/question_confirm_delete.html', {'question': question})

class Question_Update_View(UserPassesTestMixin, LoginRequiredMixin, UpdateView):

    model = Question
    fields = ['title', 'content','tag']

    def isvalid(self, form):
        form.instance.user = self.request.user
        return super().isvalid(form)

    def test_func(self):
        questions = self.get_object()
        if self.request.user != questions.user:
            return False
        return True
    
def comment_like(request,pk):

    comment = get_object_or_404(Comment, id=request.POST.get('comment_id'))

    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)

    else:
        comment.likes.add(request.user)

    return HttpResponseRedirect(reverse('smb_base:question-detail', args=[str(pk)]))
