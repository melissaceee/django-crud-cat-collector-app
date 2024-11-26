from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cat, Toy
from .forms import FeedingForm

# Create your views here.

class Home(LoginView):
    template_name = 'home.html'

#Create user
def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )

#about the cat owner
def about(request):
    return render(request, 'about.html')

#Cats index
@login_required
def cat_index(request):
    cats = Cat.objects.filter(user=request.user)
    # You could also retrieve the logged in user's cats like this
    # cats = request.user.cat_set.all()
    return render(request, 'cats/index.html', { 'cats': cats })

#single cat view
@login_required
def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form,
        'toys': toys_cat_doesnt_have,
        })
#associate toy to cat
@login_required
def associate_toy(request, cat_id, toy_id):
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect('cat-detail', cat_id=cat_id)

#remove toy
@login_required
def remove_toy(request, cat_id, toy_id):
    cat = Cat.objects.get(id=cat_id)
    toy = Toy.objects.get(id=toy_id)    
    cat.toys.remove(toy)
    return redirect('cat-detail', cat_id=cat_id)
    


#add-feeding
@login_required
def add_feeding(request, cat_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('cat-detail', cat_id=cat_id)


#Cat creat class
class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

#edit cat
class CatUpdate(LoginRequiredMixin,UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']


#delete cat
class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = '/cats/'


#create toy
class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = '__all__'


#list of all toys
class ToyList(LoginRequiredMixin, ListView):
    model = Toy


#details of a single toy
class ToyDetail(LoginRequiredMixin, DetailView):
    model= Toy


#edit a toy
class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['name', 'color']


#delete a toy
class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys/'
