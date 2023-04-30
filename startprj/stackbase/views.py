from django.shortcuts import render
from taggit.models import Tag



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

      
