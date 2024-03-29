from django.db import models
from django.contrib.auth.models import User
from PIL import Image # Pillow

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True)
    image = models.ImageField(upload_to = "profile_pictures/", default='kiwi.jpg')
    cv = models.FileField(upload_to = "cvs/", null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # resizes image (thumbnails are reduced-size versions of pictures)
            img.save(self.image.path)
