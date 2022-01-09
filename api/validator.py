from django.core.exceptions import ValidationError

def validate_story_size(value):
    filesize = value.size

    if filesize > 20971520:
        raise ValidationError("File size cannot be above 5MB")
    else:
        return value

