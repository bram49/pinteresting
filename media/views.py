from django.views import generic
from .models import Picture
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import View
from .models import Picture
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'media/index.html'
    context_object_name = 'all_pictures'
    def get_queryset(self):
        return Picture.objects.all()

class DetailView(generic.DetailView):
    model = Picture
    template_name = 'media/detail.html'

class PictureCreate(CreateView):
    model = Picture
    fields = ['artist', 'title', 'media']

class PictureUpdate(UpdateView):
    model = Picture
    fields = ['artist', 'title', 'media']

class PictureDelete(DeleteView):
    model = Picture
    success_url = reverse_lazy('media:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'media/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    #process from data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user =  form.save(commit=False)

            #cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('media:index')

        return render(request, self.template_name, {'form': form})




def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'media/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'media/index.html')
            else:
                return render(request, 'media/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'media/login.html', {'error_message': 'Invalid login'})
    return render(request, 'media/login.html')
