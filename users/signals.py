from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

# 當接收到New User被建立後，就為其建立Profile
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):

    if hasattr(instance, 'profile') and instance.profile.image and instance.profile.image.name != 'default.jpg':
        try:

            img = Image.open(instance.profile.image)

            # 檢查圖片是否需要縮放
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)

                temp_thumb = BytesIO()
                img.save(temp_thumb, format=img.format if img.format else 'JPEG')
                temp_thumb.seek(0)

                instance.profile.image.save(
                    instance.profile.image.name,
                    ContentFile(temp_thumb.read()),
                    save=False
                )
        except Exception as e:
            print(f"Error processing image for user {instance.username}: {e}")
