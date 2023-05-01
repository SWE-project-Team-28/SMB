from django.db import models
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Question, Comment , Like
from .forms import CommentForm
from django.urls import reverse, reverse_lazy
from taggit.models import Tag
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect


def home(request):
    return render(request, 'home.html')

# Create your views here.

class TagListView(ListView):
    template_name = 'stackbase/tag_list.html'
    context_object_name = 'tag_list'
    model = Tag
    def tag_list(request):
        tag_list = Tag.objects.all()
        return render(request, 'stackbase:tag-list', {'tag_list': tag_list})
      
class QuestionListByTagView(ListView):
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

class QuestionUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['title', 'content','tag']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        questions = self.get_object()
        if self.request.user == questions.user:
            return True
        return False

class QuestionDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Question
    context_object_name =  'question'
    success_url = "/"

    def test_func(self):
        questions = self.get_object()
        if self.request.user == questions.user:
            return True
        return False

class CommentDetailView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'stackbase/question-detail.html'
    
    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('stackbase:question-detail')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    
    template_name = 'stackbase/question-answer.html'

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('stackbase:question-lists')    
     
@login_required
@csrf_protect

def like_comment(request):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        is_like = request.POST.get('is_like')
        comment = get_object_or_404(Comment, pk=comment_id)
        user = request.user
        if is_like == 'true':
            Like.objects.create(user=user, comment=comment, is_like=True)
        else:
            Like.objects.create(user=user, comment=comment, is_like=False)
        likes_count = Like.objects.filter(comment=comment).count()
        return JsonResponse({'success': True, 'likes_count': likes_count})
    else:
        return JsonResponse({'success': False})
