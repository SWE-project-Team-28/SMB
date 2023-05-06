# Students Message Board

## Team members 
Ketan (CS20BTECH11043)  \
Shashidhar (ES20BTECH11036) \
Tejaswi (ES20BTECH11027)  \
Sreeya (ES20BTECH11030)   


## Introduction
Students Message Board is a web-based application where the community of IITH can discuss any campus-related queries that includes academics, non-
academics and also projects. The application also allows users to upload images and codes. It is developed by Team-28 of SWE course.

## Installation
1. git clone repository: git clone https://github.com/tejaswi1508/project1.git
2. going to working directory: cd stackprj
3. creating virtual envirnoment: python3 -m venv venv \
                                 source venv/bin/activate 
4. Installing requirements: pip install django \
                            pip install django-crispy_forms \
                            pip install django-ckeditor \
                            pip install django-taggit \
                            pip insatll crispy_bootstrap4 \
                            pip install Pillow \
                            pip install django-ckeditor_uploader 
5. Viewing webpage: python3 manage.py migrate  \
                   python3 manage.py makemigrations \
                   python3 manage.py runserver 

## Fuctions of apps

1. smb_base : This django app is related to questions and tags. Means all the use cases related to questions and tags s.t. posting question,answering question,etc functionalities are done by stackbase for this it has some templates like question_list,question_detail,etc .

2. smb_users : This django app is related to profile. Means all the use cases related to profile and updating profile with soem functionalities are taken care by Stackusers. It also has some templates login,profile, profiel_update,etc.

