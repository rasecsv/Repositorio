from rest_framework import serializers
from gestion.models import User,Person,Question,Tag,QuestionTag,Answer,ImagenQ,ImagenP


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ( 'id','first_name','last_name','email','username','password')

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = ( 'id','Type','user')

class QuestionSerializer(serializers.ModelSerializer):
 	class Meta: 
 		model = Question
 		fields = ('id', 'qstatement','Score','person')

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('id','Name')

class QuestionTagSerializer(serializers.ModelSerializer):
	class Meta:
		model = QuestionTag
		fields = ('id','question','tag')

class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = ('id','astatement','question','person')

class ImagenQSerializer (serializers.ModelSerializer):
	class Meta:
		model = ImagenQ
		fields = (' id', 'question', 'imagenQ')

class ImagenPSerializer ( serializers.ModelSerializer):
	class Meta:
		model = ImagenP
		fields = ('id','person','imagenP')
