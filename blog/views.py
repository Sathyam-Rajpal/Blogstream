from django.shortcuts import render, get_object_or_404
from django.views.generic import (
                                ListView,
                                DetailView,
                                UpdateView,
                                CreateView,
                                DeleteView)
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import (
            LoginRequiredMixin,
            UserPassesTestMixin,)

# Create your views here.
def home(request):
    context = {
            'feeds':Post.objects.all(),
        }
    return render(request,'blog/home.html',context)

# class based ListView for home
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'feeds'
    # to display the posts in newest to oldest order, we put a (-) sign
    ordering = ['-date_published']
    # we don't need to import Paginator class
    paginate_by = 5

# class based ListView for all posts from a specific user
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'feeds'
    # to display the posts in newest to oldest order, we put a (-) sign
    ''' When overriding the get_queryset() ordering is also overrriden '''
    # ordering = ['-date_published']
    # we don't need to import Paginator class, class based view takes care
    paginate_by = 5
    
    # overriding the the get_queryset() function to filter posts by the specified username
    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(writer = user).order_by('-date_published')
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'
    context_object_name = 'post'

# Field with a form to create posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # Date_Posted is filled in automatically
    fields = ['title','content']    
    template_name = 'blog/create_post.html'
    # Overriding form_valid method to add author of the form
    
    # We need to redirect to some url, so we use reverse method to 
    # let the createview handle redirection for us by itself as it 
    # uses the get_absolute_url method. We make changes in models.py
    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)  

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    # Date_Posted is filled in automatically
    fields = ['title','content']    
    # usind the same template as that of create view
    template_name = 'blog/create_post.html'
    # Overriding form_valid method to add author of the form
    
    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)  
    
    # UserPassesTestMixin() uses this method to check if a certain condition is valid for the user.
    def test_func(self):
        # we need the exact post that user wants to update
        current_post = self.get_object()
        if self.request.user == current_post.writer:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # referring to the homepage, change it to writers' post list view later
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'
    context_object_name = 'post'
    
    # UserPassesTestMixin() uses this method to check if a certain condition is valid for the user.
    def test_func(self):
        # we need the exact post that user wants to update
        current_post = self.get_object()
        if self.request.user == current_post.writer:
            return True
        else:
            return False
    
    # Now we cant use success url method to be redirecteed after successful operation
    
def about(request):
    return render(request,'blog/about.html')
