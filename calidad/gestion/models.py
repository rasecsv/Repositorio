# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User ( models.Model):
	first_name = models.CharField(max_length=30, blank=True , default='')
	last_name = models.CharField(max_length=30, blank=True, default='')
	email = models.CharField(max_length=30, blank= True,default='')
	username = models.CharField(max_length=20, blank=True, default='')
	password = models.CharField(max_length=30, blank=True , default=' ')
		
	class Meta:
		ordering = ('first_name',)

class Person ( models.Model):
	Type = models.CharField(max_length=30, blank=True , default='')
	user = models.ForeignKey(User)
	
	class Meta:
		ordering = ('Type',)


class Question ( models.Model):
	qstatement = models.CharField(max_length = 100, blank= True, default='')
	Score =  models.IntegerField()
	person = models.ForeignKey(Person)

	class Meta:
		ordering = ('qstatement',)

class Tag ( models.Model):
	Name = models.CharField(max_length = 50 , blank=True, default='')
	class Meta:
		ordering = ('Name',)

 	
class QuestionTag ( models.Model):
 	question = models.ForeignKey(Question)
 	tag = models.ForeignKey(Tag)

class Answer ( models.Model):
    astatement = models.CharField(max_length =50 , blank =True , default ='')
    question= models.ForeignKey(Question)
    person = models.ForeignKey(Person)

    class Meta:
    	ordering = ('astatement',)

    
