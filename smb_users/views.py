from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Profile_Update_Form, Registeration_Form
from smb_base.models import Question
from django.shortcuts import render, get_object_or_404
import sweetify
