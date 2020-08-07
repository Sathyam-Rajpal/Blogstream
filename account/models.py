from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
# ALWAYS REGISTER YOUR MODEL IN 'admin.py'
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # creating an image field, upload_to: creates a directory of same name in root of project to store images
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics',)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    # Overriding the save method of the model and then saving the resized image
    # Necessary to pass  *args, **kwargs otherwise 'force_save' error
    '''
    WE have removed the resize functionality as using pillow on s3 bucket causes error
    We will use aws lambda functions to resize if need be
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # getting the profile picture 
        img = Image.open(self.image.path)
        # resizing the image, maybe more efficient methods present but for production server
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    '''