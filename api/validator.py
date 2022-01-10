from django.core.exceptions import ValidationError

def validate_story_size(value):
    filesize = value.size

    if filesize > 52428800:
        raise ValidationError("File size cannot be above 50MB")
    else:
        return value

