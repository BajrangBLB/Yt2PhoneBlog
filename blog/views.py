from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import AddPostForm, EditPostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "blog/home.html"
    ordering = ['-pub_date']
    # ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

def CategoryView(request, category):
    category_posts = Post.objects.filter(category=category.replace('-', ' ').title())
    if len(category_posts) == 0:
        category_posts = Post.objects.filter(category=category)

    return render(request, 'blog/categories.html', {'category':category.title().replace('-', ' '), 'category_posts':category_posts})

def CategoryListView(request):
    category_menu_list = Category.objects.all()
    return render(request, 'blog/category_list.html', {'category_list':category_menu_list})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_details', args=[str(pk)]))

def AddComment(request, pk):
    if request.method == 'POST':
        name = request.POST.get('comment_name')
        email = request.POST.get('comment_email')
        
        if name == None:
            print("If block is being executed")
            name = request.user.username
            email = request.user.email

        body = request.POST.get('comment_body')
        post = get_object_or_404(Post, id=request.POST.get('post_id'))

        comment = Comment(post=post, name=name, email=email, body=body)
        comment.save()

        return redirect(f"/blog/article/{pk}")
    else:
        return HttpResponse("Bad Request")

    

class ArticleDetailView(DetailView):
    model = Post
    template_name = "blog/article_details.html"

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        
        post_like = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post_like.total_likes()
        
        liked = False
        if post_like.likes.filter(id=self.request.user.id).exists():
            liked = True

        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = "blog/add_post.html"
    # fields = '__all__'

class AddCategoryView(CreateView):
    model = Category
    template_name = "blog/add_category.html"
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'blog/update_post.html'
    # fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')
