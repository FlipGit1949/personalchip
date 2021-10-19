from django.db import models
import uuid
from validators import file_size
from ckeditor_uploader.fields import RichTextUploadingField

class Project(models.Model):
	title = models.CharField(max_length=200)
	thumbnail = models.ImageField(null=True)
	body = RichTextUploadingField()
	slug = models.SlugField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	def __str__(self):
		return self.title

class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.body[0:50]

class Skill(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True, default="Chip_2.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Message(models.Model):
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	subject = models.CharField(max_length=200, null=True)
	body = models.TextField()
	is_read = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	def __str__(self):
		return self.name

class Video(models.Model):
	caption = models.CharField(max_length=200)
	video = models.FileField(upload_to="video/%y", validators=[file_size])
	
	def __str__(self):
		return self.caption
