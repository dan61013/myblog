from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    # 當User被刪除時，Profile的相關資料也會被刪除
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            ouput_size = (300, 300)
            img.thumbnail(ouput_size)
            img.save(self.image.path)
