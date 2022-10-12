from django.core.exceptions import ValidationError
import cv2
import datetime


def validate_post_duration(post_value):
    data = cv2.VideoCapture(post_value.path)
    # #
    # frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
    # fps = data.get(cv2.CAP_PROP_FPS)
    # print(frames)
    # print(fps)
    #
    # seconds = round(frames / fps)
    # video_time = datetime.timedelta(seconds=seconds)
    # print(video_time)
    # if seconds > 20:
    #     raise ValidationError("Duration should be 20 seconds")
    # else:
    #     return


def validate_story_size(value):
    filesize = value.size

    if filesize > 52428800:
        raise ValidationError("File size cannot be above 50MB")
    else:
        return value


def validate_devotion_size(value):
    filesize = value.size

    if filesize > 52428800:
        raise ValidationError("File size cannot be above 50MB")
    else:
        return value
