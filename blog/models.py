from django.db import models
from django.utils import timezone
# The default django user utility
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# Register the models too in the admin.py

class Post(models.Model):
    title = models.CharField(max_length=100)
    # we left text_field empty because we want it to be unrestricted text
    content = models.TextField()
    # auto_now always edits when the object is modified
    # auto_now_add never lets edits the time which is set to the time when the object was created.
    date_published = models.DateTimeField(default=timezone.now)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # we are creating a url same as that of the post_details to get redirected to the post details page after creating
        
        # We may also use a success url for the redirection to home_page or simply provide 'home' url
        # BOTH WORKS
        return reverse('home')