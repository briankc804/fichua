import email
from django.db import models
# from django.contrib.auth.models  import User

from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField


User = get_user_model()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', blank=True)
    name = models.CharField(blank=True, max_length=120)
    bio = models.TextField(blank=True, max_length=500)
    location = models.CharField(max_length=60, blank=True)
    # contact = models.IntegerField(null=True)
    email = models.EmailField(max_length=200)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        
      
        
        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)

