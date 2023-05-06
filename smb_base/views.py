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
