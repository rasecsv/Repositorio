# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from gestion.models import User, Person,Question,Tag,QuestionTag,Answer
from gestion.serializers import UserSerializer,PersonSerializer,QuestionSerializer,TagSerializer,QuestionTagSerializer,AnswerSerializer

class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class PersonList(generics.ListCreateAPIView):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer

class QuestionList(generics.ListCreateAPIView):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer


class TagList(generics.ListCreateAPIView):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer

class QuestionTagList(generics.ListCreateAPIView):
	queryset = QuestionTag.objects.all()
	serializer_class = QuestionTagSerializer

class QuestionTagDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = QuestionTag.objects.all()
	serializer_class = QuestionTagSerializer

class AnswerList(generics.ListCreateAPIView):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer