from django.core.exceptions import ValidationError

def file_size(value):
	filesize = value.size
	if filesize > 1258291200:
		raise ValidationError('maximum size is 150 mb')
