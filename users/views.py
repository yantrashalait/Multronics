from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm
from django.shortcuts import render, redirect
from users.models import UserProfile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=False
            user.save()
            # profile = UserProfile()
            # profile.user = user
            # image = request.FILES.get("image")
            # if image:
            #     profile.image = image
            # else:
            #     image = 'default.jpg'
            #     profile.image = image
            # profile.save()
            # username = form.cleaned_data.get('username')
            # messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
    else:        
        form = UserRegisterForm()        
    return render(request, 'users/register.html', {'form': form})