from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # You can also log the user in at this point if desired

            return redirect('login')  # Redirect to the login page after successful registration

    else:
        form = RegistrationForm()

    return render(request, 'amanda/registro.html', {'form': form})
