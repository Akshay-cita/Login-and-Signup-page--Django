from django.shortcuts import render
from secondapp.forms import UserForm,UserProfileInfoform
from secondapp.models import UserProfileInfo

# Create your views here.
def first_view(request):
    return render(request,'first.html')

def second_view(request):
    registered='False'
    
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoform(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            registered='True'
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoform()
    return render(request,'third.html', {'user_form':user_form,
                                     'profile_form':profile_form,
                                     'registered':registered})
