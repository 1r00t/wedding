from django.db import models
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField


class Image(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="images"
    )
    file = ResizedImageField(
        size=[1920, None],
        quality=75,
        keep_meta=True,
        upload_to="images",
        force_format="jpeg",
    )
