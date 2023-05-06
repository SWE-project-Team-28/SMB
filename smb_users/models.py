from django.db import models
from django.contrib.auth.models import User
from PIL import ImageOps
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to="profile_pic")
    occupation = models.CharField(max_length=50,default='Student')

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            max_size = (300, 300)
            # Using the PIL-SIMD library for resizing the image
            img = ImageOps.fit(img, max_size, Image.ANTIALIAS)
            img.save(self.image.path)
