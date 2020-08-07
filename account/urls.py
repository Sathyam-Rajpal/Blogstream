from django.urls import path
from . import views
urlpatterns = [
    # localhost:8000/signup/
    path('',views.signup, name='signup'),    
]
