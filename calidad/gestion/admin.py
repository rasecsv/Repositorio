# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from gestion.models import User, Person,Question,Tag,QuestionTag,Answer,ImagenQ,ImagenP

# Register your models here.
admin.site.register(User);
admin.site.register(Person);
admin.site.register(Question);
admin.site.register(Tag);
admin.site.register(QuestionTag);
admin.site.register(Answer);
admin.site.register(ImagenQ);
admin.site.register(ImagenP);
