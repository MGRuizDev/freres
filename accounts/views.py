from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import UserForm
# Create your views here.
class registerView(View):
    form_class = UserForm
    template = "accounts/registration_form.html"

    def get(self, request):
        form = self.form_class(None)
        context = {
            'form': form,
        }
        return render(request, self.template, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            #This data will be needed for authentication.
            #password is also needed for the set_password method.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            #Return user objects if credentials are correct.
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'wineList/home.html', context)
