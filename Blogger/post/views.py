from django.forms import BaseModelForm
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, comment
from .forms import Writeform, Updateform, Writecommentform
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from django.shortcuts import render, redirect
from django.http import HttpResponse

def LikeView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    likes=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True

    return HttpResponseRedirect(reverse('singlepost', args=[str(pk)]))

class popular(ListView):
    model = Post
    template_name="popular.html"
    ordering = ['-likes']
    

def number_user(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "CALL no_user();"
        )
        no_user=list(cursor.fetchall())
    return render(request, 'num_user.html', {'num' : no_user[0]})


class singlepost(DetailView):
    model = Post
    template_name="singlepost.html"

    def get_context_data(self, *args, **kwargs):
        context = super(singlepost, self).get_context_data(*args, **kwargs)
         
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True

        context["total_likes"] = total_likes
        context["liked"] = liked 
        return context


class write(CreateView):
    model = Post
    form_class = Writeform
    template_name="write.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class writecomment(CreateView):
    model = comment
    form_class = Writecommentform
    template_name="addcomment.html"
    success_url = reverse_lazy('singlepost')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('singlepost', kwargs={'pk': self.kwargs['pk']})
    
class update(UpdateView):
    model = Post
    form_class = Updateform
    template_name="update.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class delete(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy('popular')
