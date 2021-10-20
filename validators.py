from django.core.exceptions import ValidationError

def file_size(value):
	filesize = value.size
	if filesize > 2097152000:
		raise ValidationError('maximum size is 250 mb')
